import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call the S3 client's list_buckets method
response = s3.list_buckets()

# Iterate over the list of buckets returned by the API
for bucket in response['Buckets']:
    print(bucket['Name'])
