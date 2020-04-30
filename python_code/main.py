import boto3
import os

class EC2:
    def __init__(self, client_name='demo', num_instances=1, keypair="ec2-keypair"):
        self.client_name = client_name
        self.num_instances = num_instances
        self.keyName = keypair
        self.imageid = 'ami-009110a2bf8d7dd0a'
        self.instancetype = 't2.micro'
        self.ec2 = boto3.resource('ec2')
        self.instances = []

    def update_tags(self):
        i = 1
        for instance in self.instances:
            iname = self.client_name + "-" + str(i)
            instance.create_tags(Tags=[{"Key": "Name", "Value": iname}])
            i = i+1

    def create(self):
        self.instances = self.ec2.create_instances(
                ImageId=self.imageid,
                MinCount=1,
                MaxCount=self.num_instances,
                InstanceType=self.instancetype,
                KeyName=self.keyName
        )
        self.update_tags()

    def get_details(self):
        for instance in self.instances:
            instance.wait_until_running()
            print(instance.state)
            print(instance.instance_id, instance.public_ip_address)


if __name__ == "__main__":
    customer_name = os.getenv('CUSTOMER')
    instance_count = int(os.getenv('COUNT'))
    t1 = EC2(customer_name,instance_count)
    t1.create()
    t1.get_details()

