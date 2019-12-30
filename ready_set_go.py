# Copyright 2017 Amazon Web Services, Inc. or its affiliates. All rights
# reserved.

import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import sys

def get_bucket_count():
    print("============================================")
    print("Welcome to the AWS Boto3 SDK! Ready, Set, Go!")
    print("============================================")

    try:
        s3 = boto3.resource('s3')
    except NoCredentialsError:
        print("@InvalidCredentials")
        sys.exit()

    try:
        no_of_buckets_l = len(list(s3.buckets.all()))
        bucket_list = list(s3.buckets.all())
        for bucket in bucket_list:
            print(bucket.name)
        return no_of_buckets_l
    except ClientError as ex:
        print(ex)
        return 0

####################  Main #############


if __name__ == '__main__':
    no_of_buckets = get_bucket_count()
    print("You have", str(no_of_buckets), "Amazon S3 buckets.")
