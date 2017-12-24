import boto3
import sys

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
     print(bucket.name)
     for obj in bucket.objects.all():
          print(obj.key)
