from dploy.database.base import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class AWS_Instance_Keys(Base):
    """AWS_Instances' Keys Schema"""

    __tablename__ = "aws_instance_keys"
    id = Column(Integer, primary_key=True)
    instance_id = Column(Integer, ForeignKey('aws_instances.id'))
    key_name = Column(String(255))
    key_material = Column(String(255))

    instance = relationship("AWS_Instances", back_populates="keys")

    def __init__(self,instance_id,key_name, key_material):
        self.key_name = key_name
        self.key_material = key_material
        self.instance_id = instance_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<Key Name: '{self.key_name}', Instance ID: '{self.instance_id}', Key Material: '{self.key_material}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "key_name": self.key_name,
            "instance_id": self.instance_id,
        }