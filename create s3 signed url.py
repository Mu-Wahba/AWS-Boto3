#Generate pre-signed URL to access a file on AWS s3


import boto
from boto.s3.key import Key 

connection = boto.connect_s3()
#create a bucket
connection.create_bucket('mybucket')

#create an object
Bucket = connection.get_bucket('mybucket')

#create file object by Key
key = Key(Bucket)

#assign a name to the file
key.key = 'file.txt'

#put a content into the file
key.set_contents_from_string('Hello World')

#generate signed URL (TTL,method,Bucketname,objectname)
temp_url = connection.generate_url(60,'GET','mybucket','file.txt')
