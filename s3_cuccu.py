import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

my_bucket = list(s3.buckets.all())
my_bucket = my_bucket[0].name

'''
# Upload a new file
data = open('pippo.txt.gpg', 'rb')
s3.Bucket(my_bucket).put_object(Key='pippo.txt.gpg', Body=data)
'''

# Download a new file
obj = s3.Object(bucket_name=my_bucket,key='pippo.txt.gpg')
response = obj.get()
data = response['Body'].read()

f = open('my_downloaded_file', 'w+')
f.write(data)
f.close()
