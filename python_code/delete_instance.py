import boto3
newlist=[]
ec2= boto3.resource('ec2')
instances= ec2.meta.client.describe_instances()
for x1 in instances['Reservations']: newlist.append(x1['Instances'][0]['InstanceId'])
ec2.terminate_instances(InstanceIds=(newlist))
