import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

security_group = client.create_security_group(
    GroupName='mern-sg',
    Description='Security group for MERN app'
)

instances = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your-key-pair',
    SecurityGroupIds=[security_group['GroupId']],
    UserData="""#!/bin/bash
    yum update -y
    yum install docker -y
    service docker start
    docker run -d -p 5000:5000 your-ecr-repo-uri/backend
    """
)