"""
AWS Keys Schema
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from dploy.database.base import Base

class AWS_Keys(Base):
    """AWS_Keys Schema"""

    __tablename__ = "aws_keys"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    access_key = Column(String(255))
    secret_access_key = Column(String(255))

    owner = relationship("Users", back_populates="aws_key")

    def __init__(self, user_id, access_key, secret_access_key):
        self.user_id = user_id
        self.access_key = access_key
        self.secret_access_key = secret_access_key

    def __repr__(self):
        """Representation of the object"""
        return f"""<Access Key: '{self.access_key}', Secret Access key: '{self.secret_access_key}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "user_id": self.id,
            "access_key": self.access_key,
            "secret_access_key": self.secret_access_key,
        }