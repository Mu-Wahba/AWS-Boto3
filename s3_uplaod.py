import boto3
import argparse
import botocore
'''
To execute and  upload file to your s3 bucket:

     s3_uplaod.py -u filepath -b bucket_name -n object_name
'''

parser = argparse.ArgumentParser(description='upload object in AWS S3 bucket',epilog='')
parser.add_argument('-u','--upload',type=str,metavar='',help='file path',require=True)
parser.add_argument('-b','--bucket',type=str,metavar='',help='bucket name',require=True)
parser.add_argument('-n','--objname',type=str,metavar='',help='object name')
args = parser.parse_args()

s3_resource = boto3.resource('s3')

try:
     if args.objname:
          with open (args.upload,'rb') as file:
               s3_resource.Object(args.bucket,args.objname ).put(Body=file)
               print('successfully Uploaded)

     else:
          args.objname = args.upload.split('/')[-1]
          with open (args.upload,'rb') as file:
               s3_resource.Object(args.bucket,args.objname).put(Body=file)
               print('successfully Uploaded)

except botocore.exceptions.ClientError as e:
     print(e.response['Error']['Code'])
