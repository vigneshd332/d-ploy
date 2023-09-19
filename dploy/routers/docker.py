"""
Docker API Routes
"""

from fastapi import APIRouter, Depends
from dploy.daemon.main import get_daemon
from dploy.database.session import get_database
from dploy.models.docker import ContainerDeleteRequest, ContainerOperations, CreateContainerRequest, ContainerDetails

from dploy.schemas.daemons import DaemonSchema

router = APIRouter(
    prefix='/docker',
    tags=['docker']
)


@router.post('/container/create', responses={
    200: {
        'description': 'Successfully created container'
    },
    500: {
        'description': 'Internal server error'
    }
})
def create_container(create_request: CreateContainerRequest, database=Depends(get_database)):
    """
    Create a new container
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=create_request.daemon_id).first()
    daemon = get_daemon(create_request.daemon_id,
                        daemon_creds.url, daemon_creds.auth_key)
    return daemon.create_container(create_request.image, create_request.name, create_request.ports)


@router.get('/containers/{container}', responses={
    200: {
        'description': 'Successfully retrieved container details'
    },
    500: {
        'description': 'Internal server error'
    }
})
def get_container_details(container_ops_request: ContainerOperations, container_id: str, database=Depends(get_database)):
    """
    Get container details
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=container_ops_request.daemon_id).first()
    daemon = get_daemon(container_ops_request.daemon_id,
                        daemon_creds.url, daemon_creds.auth_key)
    return daemon.get_container_details(container_id)


@router.post('/containers/delete', responses={
    200: {
        'description': 'Successfully deleted container'
    },
    500: {
        'description': 'Internal server error'
    }
})
def delete_container(container_delete_request: ContainerDeleteRequest, database=Depends(get_database)):
    """
    Delete container
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=container_delete_request.daemon_id).first()
    daemon = get_daemon(container_delete_request.daemon_id,
                        daemon_creds.url, daemon_creds.auth_key)
    return daemon.delete_container(container_delete_request.container_id, container_delete_request.force, container_delete_request.v)


@router.post('/containers/{container_id}/start', responses={
    200: {
        'description': 'Successfully started container'
    },
    500: {
        'description': 'Internal server error'
    }
})
def start_container(container_ops_request: ContainerOperations, container_id: str, database=Depends(get_database)):
    """
    Start container
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=container_ops_request.daemon_id).first()
    daemon = get_daemon(container_ops_request.daemon_id,
                        daemon_creds.url, daemon_creds.auth_key)
    return daemon.start_container(container_id)


@router.post('/containers/{container_id}/stop', responses={
    200: {
        'description': 'Successfully stopped container'
    },
    500: {
        'description': 'Internal server error'
    }
})
def stop_container(container_ops_request: ContainerOperations, container_id: str, database=Depends(get_database)):
    """
    Stop container
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=container_ops_request.daemon_id).first()
    daemon = get_daemon(container_ops_request.daemon_id,
                        daemon_creds.url, daemon_creds.auth_key)
    return daemon.stop_container(container_id)


@router.post('/containers/{container_id}/kill', responses={
    200: {
        'description': 'Successfully killed container'
    },
    500: {
        'description': 'Internal server error'
    }
})
def kill_container(container_ops_request: ContainerOperations, container_id: str, database=Depends(get_database)):
    """
    Kill container
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=container_ops_request.daemon_id).first()
    daemon = get_daemon(container_ops_request.daemon_id,
                        daemon_creds.url, daemon_creds.auth_key)
    return daemon.kill_container(container_id)


@router.post('/containers/{container_id}/restart', responses={
    200: {
        'description': 'Successfully restarted container'
    },
    500: {
        'description': 'Internal server error'
    }
})
def restart_container(container_ops_request: ContainerOperations, container_id: str, database=Depends(get_database)):
    """
    Restart container
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=container_ops_request.daemon_id).first()
    daemon = get_daemon(container_ops_request.daemon_id,
                        daemon_creds.url, daemon_creds.auth_key)
    return daemon.restart_container(container_id)
