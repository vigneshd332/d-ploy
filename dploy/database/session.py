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
    logger.info("Hi")
    database = SessionLocal()
    logger.info("Hi")
    try:
        yield database
        database.commit()
        logger.info("Hi1")
    except:
        database.rollback()
        logger.info("Hi2")
    finally:
        database.close()
        logger.info("Hi3")