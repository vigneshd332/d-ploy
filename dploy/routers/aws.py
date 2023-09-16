from fastapi import APIRouter,Depends
import logging
from dploy.database.session import get_database
from dploy.crud.aws import get_images_details, get_appropiate_instances, create_instances
from dploy.models.aws import InstanceRequestModel, InstanceCreationRequestModel

router = APIRouter(
    prefix="/aws"
)


logger = logging.getLogger(__name__)

@router.get(
        "/all-images",
        )
def gets_all_images(database = Depends(get_database)):
    user_id = 1
    images,_,_ = get_images_details(database, user_id)
    return {
        "images": images
    }


# Gets all the possible instances a user can create
@router.post(
        "/all-instances",
       )
def gets_all_instances(image_id:InstanceRequestModel,database = Depends(get_database)):
    user_id = 1
    instances = get_appropiate_instances(database,user_id,image_id.image_id)
    return {
        "instances": instances
    }

# Have route to get users keys.
# We should also store AWS Access key and Secret Access Key as well, per user.
@router.post("/register-aws")
def register_aws():
    pass

#gets all instances the user has
@router.get("/instances")
def get_instances():
    pass

#creates an instance and runs the daemon inside it.
@router.post("/create-instance")
def create_instance(instance_details:InstanceCreationRequestModel,database=Depends(get_database)):
    user_id = 1
    instance = create_instances(database,user_id,instance_details.image_id,instance_details.instance_type,instance_details.key_name)
    return {
        "instance": instance
    }


#stops a running instance which the user already created.
@router.get("/stop-instance")
def stop_instance():
    pass

#starts a running instance which the user already created
@router.get("/start-instance")
def start_instance():
    pass

#restarts a running instance, the user already created.
@router.get("/reboot-instance")
def reboot_instance():
    pass

