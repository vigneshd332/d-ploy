"""
Daemon Schema
"""

from sqlalchemy import Column, Integer, String

from dploy.database.base import Base


class DaemonSchema(Base):
    """
    Daemon Schema
    """

    __tablename__ = "daemons"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    url = Column(String(255))
    uuid = Column(String(255))
    auth_key = Column(String(255))

    def __init__(self, name, url, uuid, auth_key):
        self.name = name
        self.url = url
        self.uuid = uuid
        self.auth_key = auth_key

    def __repr__(self):
        """Representation of the object"""
        return f"""<Name: '{self.name}', URL: '{self.url}',
        UUID: '{self.uuid}', Auth Key: '{self.auth_key}' >"""

    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "uuid": self.uuid,
            "auth_key": self.auth_key,
        }
