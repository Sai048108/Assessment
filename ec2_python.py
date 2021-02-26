import boto3
import yaml
import os
from botocore.exceptions import ClientError

# Create EC2 Key pair
ec2 = boto3.client('ec2')
response = ec2.create_key_pair(KeyName='Python_KEY')
print(response)


# # Create Security Group 
ec2 = boto3.client('ec2')
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

try:
    response = ec2.create_security_group(GroupName='PYTHON_SECURITY_GROUP',
                                         Description='DESCRIPTION',
                                         VpcId='vpc-bd5adad6')
    security_group_id = response['GroupId']
    print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
        ])
    print('Ingress Successfully Set %s' % data)
except ClientError as e:
    print(e)

# Create EC2 instance
client = boto3.resource('ec2')
with open('ec2.yaml','rt') as f:
   data = yaml.safe_load(f)
   print (data)
ec2 = client.create_Instance(data)

# Creating EC2 Instance and SSH to EC2 Instance
ec2 = boto3.resource('ec2')
with open('ec2.yaml') as f:
   data = yaml.load(f,Loader= yaml.FullLoader)
   print(data)
print(type(data))
response = ec2.create_instances(**data)
for instance in ec2.instances.all():
    print (instance.id , instance.state)

# Copy file into EC2 Instance
os.system('scp -i Python_KEY1 ec2-user@instance_ip:~/Sharing' % (./test.txt, /))
os.system('scp -i Python_KEY1 root@instance_ip:~/Sharing' % (./test.txt, /data))