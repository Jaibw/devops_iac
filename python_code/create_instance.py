import boto3
import os

machine_tag = "yourname"
num_instances = 1
keyName = "user00"
imageid = 'ami-01154c8b2e9a14885'
instancetype = 't2.micro'

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
                ImageId=imageid,
                MinCount=1,
                MaxCount=num_instances,
                InstanceType=instancetype,
                KeyName=keyName )

instance.create_tags(Tags=[{"Key": "Name", "Value": machine_tag}])

instance.wait_until_running()
print(instance.state)
print(instance.instance_id, instance.public_ip_address)
