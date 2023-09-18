"""
Router for Daemon routes
"""

from typing import List
import uuid
import random
import string
import logging
from fastapi import APIRouter, Depends, HTTPException
from dploy.daemon.main import get_daemon
from dploy.database.session import get_database

from dploy.models.daemons import RegisterModel
from dploy.models.error import SuccessResponse
from dploy.schemas.daemons import DaemonSchema

router = APIRouter(
    prefix='/daemon',
    tags=['daemon']
)


@router.post('/register', responses={
    200: {
        'description': 'Daemon registered successfully'
    },
    400: {
        'description': 'Daemon already registered'
    },
    500: {
        'description': 'Internal server error'
    }
})
async def register(
    register_request: RegisterModel,
    database=Depends(get_database)
):
    """
    Register a new daemon
    """
    try:
        daemon = database.query(DaemonSchema).filter_by(
            uuid=register_request.url).first()
        if daemon:
            raise HTTPException(
                status_code=400, detail='Daemon with URL already registered')
        daemon = database.query(DaemonSchema).filter_by(
            name=register_request.name).first()
        if daemon:
            raise HTTPException(
                status_code=400, detail='Daemon with name already exists')

        random_uuid = str(uuid.uuid4())
        auth_key = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=32))
        daemon = get_daemon(random_uuid, register_request.url, auth_key)
        daemon.register_daemon()
        daemon = DaemonSchema(
            name=register_request.name,
            url=register_request.url,
            uuid=random_uuid,
            auth_key=auth_key
        )
        database.add(daemon)
        database.commit()
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")

    return SuccessResponse(message='Daemon registered successfully')


@router.get('/list', response_model=List[dict[str, str]], responses={
    200: {
        'description': 'List of daemons'
    },
    500: {
        'description': 'Internal server error'
    }
})
async def list_daemons(database=Depends(get_database)) -> List[dict[str, str]]:
    """
    List all the registered daemons
    """
    try:
        daemons = database.query(
            DaemonSchema.uuid, DaemonSchema.url, DaemonSchema.name).all()
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="Internal server error")
    return daemons
