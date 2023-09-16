import boto3
import tempfile
import os

from sqlalchemy.orm import Session
from botocore.exceptions import ClientError
from dploy.schemas.aws_instance_keys import AWS_Instance_Keys
from dploy.schemas.aws_instances import AWS_Instances
from dploy.schemas.aws_keys import AWS_Keys

import logging

logger = logging.getLogger(__name__)


def create_client(access_key,secret_access_key,client_type):
    cli = boto3.client(
        client_type,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key,
        region_name='us-east-1'
        )
    return cli

def get_keys(db:Session, user_id):
    try:
        access_keys =  db.query(AWS_Keys).filter(AWS_Keys.user_id==user_id).first()
    except Exception as Err:
        print(Err)
    print(f"Hi {access_keys}")
    return access_keys

def get_images(db:Session,user_id,image_ids):
    access_keys = get_keys(db,user_id)
    ec2_client = create_client(access_keys.access_key,access_keys.secret_access_key,"ec2")
    
    try:
        images = ec2_client.describe_images(ImageIds=image_ids)
    except ClientError as err:
        print(  "Couldn't get images. Here's why: %s: %s",
                err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    except Exception as err:
        print(err)
        raise
    else:
        return images, ec2_client

#finds only micro and small instances
def get_appropiate_instances(db:Session,user_id,image_id):
    access_keys = get_keys(db,user_id)
    ec2_client = create_client(access_keys.access_key,access_keys.secret_access_key,"ec2")
    
    try:
        image = ec2_client.describe_images(ImageIds=[image_id])
        print(f"image details: {image}")
        inst_types = []
        it_paginator = ec2_client.get_paginator('describe_instance_types')
        image_deets = image["Images"][0]
        architecture = image_deets["Architecture"]
        for page in it_paginator.paginate(Filters=[
                    {'Name': 'processor-info.supported-architecture', 'Values': [architecture]},
                    {'Name': 'instance-type', 'Values': ['*.micro', '*.small']}]):
                a = page["InstanceTypes"]
                inst_types += a
    except ClientError as err:
        print( "Couldn't Find Appropiate Instances. Here's why: %s: %s", err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    except Exception as err:
        print(err)
        raise
    else:
        return inst_types


def create_instances(db:Session,user_id,image_id,instance_type, key_name):
    key_pair = create_key_pair(db,user_id,key_name)
    access_keys = get_keys(db,user_id)
    ec2_client = create_client(access_keys.access_key,access_keys.secret_access_key,"ec2")
    try:
        instance_params = {
            'ImageId': image_id, 'InstanceType': instance_type, 'KeyName': key_pair["KeyName"]
        }
        instance = ec2_client.run_instances(**instance_params, MinCount=1, MaxCount=1)
        instance_obj = instance["Instances"][0]
        new_instance = AWS_Instances(user_id,instance_obj["InstanceId"])
        db.add(new_instance)
        new_instance_key_pair = AWS_Instance_Keys(new_instance.id,key_pair["KeyName"],key_pair["KeyMaterial"])
        db.add(new_instance_key_pair)
        # Store the name,private key with user id and instance id in a separate table
    except ClientError as err:
        print("Couldn't create instance with image %s, instance type %s, and key %s. "
                "Here's why: %s: %s", image_id, instance_type, key_pair.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
        raise
    except Exception as err:
        print(err)
    else:
        return instance
    

def get_images_details(db:Session,user_id):
    access_keys = get_keys(db,user_id)
    logger.info(access_keys)
    try:
        ssm_client = create_client(access_keys.access_key,access_keys.secret_access_key,"ssm")
        ami_options = []
        ami_paginator = ssm_client.get_paginator('get_parameters_by_path')
        for page in ami_paginator.paginate(Path='/aws/service/ami-amazon-linux-latest'):
            # print(page['Parameters'])
            ami_options += page['Parameters']
        image_ids = [opt['Value'] for opt in ami_options]
        images, ec2_client = get_images(db,user_id,image_ids)
        return images, ec2_client, ssm_client
    except Exception as err:
        print(err)

def create_key_pair(db:Session,user_id,key_name):
    access_keys = get_keys(db,user_id)
    ec2_client = create_client(access_keys.access_key,access_keys.secret_access_key,"ec2")
    try:
        key_pair = ec2_client.create_key_pair(KeyName=key_name)
    except ClientError as err:
        print("Couldn't Create Key Pair. Here's why: %s: %s", err.response["Error"]['Code'], err.response['Error']['Message'])
    else:
        return key_pair



