__author__ = 'akkaashgoel'

from boto import ec2
from boto.ec2.instance import Instance
from pprint import pprint

regions = ec2.regions()
# print regions

ec2_client = ec2.connect_to_region('us-west-1')

# images = ec2_client.get_all_images(owners='amazon', filters={'architecture': 'x86_64', 'virtualization_type': 'hvm'})
# print images

image_id = 'ami-4b6f650e'
instance_type = 't2.micro'
key_name = 'demo1'

# reservation = ec2_client.run_instances(image_id=image_id, instance_type=instance_type, key_name=key_name)
# instance = reservation.instances[0]

instance_id = 'i-268ebeee'

reservations = ec2_client.get_all_reservations(instance_ids=[instance_id])

instance = reservations[0].instances[0]
assert isinstance(instance, Instance)

pprint(vars(instance))