from __future__ import absolute_import, division, print_function, unicode_literals

import os, sys, argparse, json
from datetime import datetime, timedelta
from collections import defaultdict

import boto3
from botocore.exceptions import ClientError

from . import register_parser, logger
from .ls import filter_collection, register_filtering_parser
from .util.aws import ARN, resources, clients, expect_error_codes, get_cloudwatch_metric_stats
from .util.printing import page_output, tabulate, format_number

def buckets(args):
    buckets_parser.print_help()

buckets_parser = register_parser(buckets, help="Manage S3 buckets", description=__doc__)

def ls(args):
    """
    List S3 buckets. See also "aws s3 ls". Use "aws s3 ls NAME" to list bucket contents.
    """
    table = []
    for bucket in filter_collection(resources.s3.buckets, args):
        bucket.LocationConstraint = clients.s3.get_bucket_location(Bucket=bucket.name)["LocationConstraint"]
        cloudwatch = resources.cloudwatch
        bucket_region = bucket.LocationConstraint or "us-east-1"
        if bucket_region != cloudwatch.meta.client.meta.region_name:
            cloudwatch = boto3.Session(region_name=bucket_region).resource("cloudwatch")
        data = get_cloudwatch_metric_stats("AWS/S3", "NumberOfObjects",
                                           start_time=datetime.utcnow() - timedelta(days=2),
                                           end_time=datetime.utcnow(), period=3600, BucketName=bucket.name,
                                           StorageType="AllStorageTypes", resource=cloudwatch)
        bucket.NumberOfObjects = int(data["Datapoints"][-1]["Average"]) if data["Datapoints"] else None
        data = get_cloudwatch_metric_stats("AWS/S3", "BucketSizeBytes",
                                           start_time=datetime.utcnow() - timedelta(days=2),
                                           end_time=datetime.utcnow(), period=3600, BucketName=bucket.name,
                                           StorageType="StandardStorage", resource=cloudwatch)
        bucket.BucketSizeBytes = format_number(data["Datapoints"][-1]["Average"]) if data["Datapoints"] else None
        table.append(bucket)
    page_output(tabulate(table, args))

parser = register_filtering_parser(ls, parent=buckets_parser)

def lifecycle(args):
    if args.delete:
        return resources.s3.BucketLifecycle(args.bucket_name).delete()
    rule = defaultdict(list, Prefix=args.prefix, Status="Enabled")
    if args.transition_to_infrequent_access is not None:
        rule["Transitions"].append(dict(StorageClass="STANDARD_IA", Days=args.transition_to_infrequent_access))
    if args.transition_to_glacier is not None:
        rule["Transitions"].append(dict(StorageClass="GLACIER", Days=args.transition_to_glacier))
    if args.expire is not None:
        rule["Expiration"] = dict(Days=args.expire)
    if args.abort_incomplete_multipart_upload is not None:
        rule["AbortIncompleteMultipartUpload"] = dict(DaysAfterInitiation=args.abort_incomplete_multipart_upload)
    if len(rule) > 2:
        clients.s3.put_bucket_lifecycle_configuration(Bucket=args.bucket_name,
                                                      LifecycleConfiguration=dict(Rules=[rule]))
    try:
        for rule in resources.s3.BucketLifecycle(args.bucket_name).rules:
            print(json.dumps(rule))
    except ClientError as e:
        expect_error_codes(e, "NoSuchLifecycleConfiguration")
        logger.error("No lifecycle configuration for bucket %s", args.bucket_name)

parser = register_parser(lifecycle, parent=buckets_parser)
parser.add_argument("bucket_name")
parser.add_argument("--delete", action="store_true")
parser.add_argument("--prefix", default="")
parser.add_argument("--transition-to-infrequent-access", type=int, metavar="DAYS")
parser.add_argument("--transition-to-glacier", type=int, metavar="DAYS")
parser.add_argument("--expire", type=int, metavar="DAYS")
parser.add_argument("--abort-incomplete-multipart-upload", type=int, metavar="DAYS")

def cors(args):
    raise NotImplementedError()

parser = register_parser(cors, parent=buckets_parser)
parser.add_argument("bucket_name")
