import boto3
ec2= boto3.resource('ec2')
instances= ec2.meta.client.describe_instances()
for x1 in instances['Reservations']: print(">>>>",x1['Instances'][0]['InstanceId'], x1['Instances'][0].get('Tags','NA') )
