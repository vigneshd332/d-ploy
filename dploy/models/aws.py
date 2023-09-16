from pydantic import BaseModel
from pydantic.fields import Field

class InstanceRequestModel(BaseModel):

    image_id: str = Field(
        title="Image Id"
    )


class InstanceCreationRequestModel(BaseModel):

    image_id: str = Field(
        title="Image ID"
    )

    instance_type: str = Field(
        title="Instance Type"
    )

    key_name: str = Field(
        title="Key Name"
    )