CSC591_DevOps_HW1
=================

## HW #1 Provisioning Servers Using Amazon Web Services

In this program I have used [boto](http://docs.pythonboto.org/) which is Python interface for AWS.

Boto Config File
----------------
The boto config file is used to store the AWS credentials instead of having to add the secure credentials into the code. 
The format of the config file is:
    
    [Credentials]
    aws_access_key_id = <AWS Access Key Here>
    aws_secret_access_key = <AWS Secret Key Here>


Listing EC2 regions
-------------------
To list all the available regions for the EC2 service, use the following call

    regions = ec2.regions()
    
Connecting to a available region
--------------------------------
To connect to available region we use the `ec2.connect_to_region()` function. Here I am connecting to the `us-west-1` region. 

    ec2_client = ec2.connect_to_region('us-west-1')
This returns a EC2Connection object which can be used to perform further EC2 client related API calls.
 
List available images
---------------------
To list all available images in a region, I used the following call:

    images = ec2_client.get_all_images(owners='amazon', filters={'architecture': 'x86_64', 'virtualization_type': 'hvm'})
Here I am only retrieving images owned by Amazon. Further, I filter the results and only retrieve images which are 64-bit and virtual machines.
These filters can be found [here](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html)
 
Launching an Instance
---------------------
To launch an instance, use the following API call:

    reservation = ec2_client.run_instances(image_id=image_id, instance_type=instance_type, key_name=key_name)
This will return a Reservation object.
This object contains list of instance objects. 
In the program, I have only launched a single instance and this this list has only one element in the instances list. 
We can get this instance using `instance = reservation.instances[0]`
From this I can extract the instance ID using `instance_id = instance.id`. For example, `instance_id = 'i-268ebeee'`

View instance information
-------------------------
To view instance information for one or more instance IDs, use the following API call:

    reservations = ec2_client.get_all_reservations(instance_ids=[instance_id])
    instance = reservations[0].instances[0]

I then print all the variables associated with this instance using `pprint(vars(instance))`


## Screen shot of AWS Management Console:
![Screen shot of AWS Management Console](https://github.ncsu.edu/agoel3/CSC591_DevOps_HW1/raw/master/Content/screen_shot.png)
