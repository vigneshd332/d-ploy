"""
AWS Instances Schema
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from dploy.database.base import Base

class AWS_Instances(Base):
    """AWS_Instances Schema"""

    __tablename__ = "aws_instances"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    instance_id = Column(Integer)

    user = relationship("Users", back_populates="aws_instances")
    keys = relationship("AWS_Instance_Keys", back_populates="instance")

    def __init__(self, user_id, instance_id):
        self.user_id = user_id
        self.instance_id = instance_id

    def __repr__(self):
        """Representation of the object"""
        return f"""<User Id: '{self.user_id}', Instance ID: '{self.instance_id}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "user_id": self.id,
            "instance_id": self.instance_id,
        }