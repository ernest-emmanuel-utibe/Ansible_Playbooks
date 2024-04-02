import botocore.utils

# Create a boto3 client for EC2
ec2 = botocore.BOTOCORE_ROOT('ec2')

# Call describe_instances() to list instances
response = ec2.describe_instances()

# Print instance information
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
