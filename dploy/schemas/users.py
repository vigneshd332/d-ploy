"""
Users Schema
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from dploy.database.base import Base

class Users(Base):
    """Users Schema"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    mobile_number = Column(String(255))
    password = Column(String(255))

    aws_key = relationship("AWS_Keys", back_populates="owner")
    aws_instances = relationship("AWS_Instances",back_populates="user")

    def __init__(self, name, email, mobile_number, password):
        self.name = name
        self.email = email
        self.mobile_number = mobile_number
        self.password = password

    def __repr__(self):
        """Representation of the object"""
        return f"""<Name: '{self.name}', Email: '{self.email}',
        Mobile: '{self.mobile_number}', Password: '{self.passwrod}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "mobile": self.mobile_number,
            "password": self.password,
        }