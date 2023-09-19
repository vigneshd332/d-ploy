"""
Models for Docker API
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class ContainerOperations(BaseModel):
    """Model for start/stop/kill/restart containers"""
    daemon_id: str = Field(..., description="Daemon ID")


class CreateContainerRequest(BaseModel):
    """Model for create container request"""
    daemon_id: str = Field(..., description="Daemon ID")
    image: str = Field(..., description="Image name")
    name: str = Field(..., description="Container name")
    ports: Optional[dict[str, int]] = Field(
        None, description="Container ports")


class ContainerDetails(BaseModel):
    """Details of a Single Docker Container"""
    daemon_id: str = Field(..., description="Daemon ID")
    id: str = Field(..., description="Container ID")
    name: str = Field(..., description="Container Name")
    status: str = Field(..., description="Container Status")
    image: List[str] = Field(None, description="Image Name")
    ports: dict[str, List[dict[str, str]]] = Field(
        None, description="Container Ports")
    created: str = Field(..., description="Container Creation Time")


class ContainerDeleteRequest(BaseModel):
    """Model for delete request"""
    daemon_id: str = Field(..., description="Daemon ID")
    container_id: str = Field(..., description="Container ID")
    force: bool = Field(False, description="Force delete")
    v: bool = Field(False, description="Remove volumes")
