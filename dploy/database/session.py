"""
Contains the database configuration and functions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
from dploy.config import settings

sqlalchemy_database_url = settings.database_url

engine = create_engine(sqlalchemy_database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = logging.getLogger(__name__)


async def get_database():
    database = SessionLocal()
    try:
        yield database
        database.commit()
    except:
        database.rollback()
    finally:
        database.close()
