import boto3
import os

machine_tag = "yourname"
num_instances = 1
keyName = "user00"
imageid = 'ami-01154c8b2e9a14885'
instancetype = 't2.micro'
print("Creating Instance: ", machine_tag)
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
                ImageId=imageid,
                MinCount=1,
                MaxCount=num_instances,
                InstanceType=instancetype,
                KeyName=keyName )
for x1 in instance: 
  x1.create_tags(Tags=[{"Key": "Name", "Value": machine_tag}])

for x1 in instance:
  print("Waiting for running state")
  x1.wait_until_running()
  print("State: ",x1.state)
  print("Details: ",x1.instance_id, x1.public_ip_address)
