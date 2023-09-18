"""
Daemon API models
"""
from pydantic import BaseModel
from pydantic.fields import Field


class RegisterModel(BaseModel):
    """
    Model for registering a new daemon
    """
    name: str = Field(..., title="Daemon Name")
    url: str = Field(..., title="Daemon URL")
