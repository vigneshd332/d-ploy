"""
Firewall API Routes
"""

from fastapi import APIRouter, Depends
from dploy.daemon.main import get_daemon
from dploy.database.session import get_database

from dploy.schemas.daemons import DaemonSchema

router = APIRouter(
    prefix='/firewall',
    tags=['firewall']
)


@router.get('/get-all-zones', responses={
    200: {
        'description': 'Successfully retrieved all zones'
    },
    500: {
        'description': 'Internal server error'
    }
})
def get_all_zones(daemon_id: str, database=Depends(get_database)):
    """
    Get all zones
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.get_all_zones()


@router.get('/get-zone-config', responses={
    200: {
        'description': 'Successfully retrieved zone config'
    },
    500: {
        'description': 'Internal server error'
    }
})
def get_zone_config(daemon_id: str, zone: str, database=Depends(get_database)):
    """
    Get zone config
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.get_zone_config(zone)


@router.post('/add-service', responses={
    200: {
        'description': 'Successfully added service'
    },
    500: {
        'description': 'Internal server error'
    }
})
def add_service(daemon_id: str, service_name: str, database=Depends(get_database)):
    """
    Add service
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.add_service(service_name)


@router.post('/remove-service', responses={
    200: {
        'description': 'Successfully removed service'
    },
    500: {
        'description': 'Internal server error'
    }
})
def remove_service(daemon_id: str, service_name: str, database=Depends(get_database)):
    """
    Remove service
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.remove_service(service_name)


@router.post('/add-ports', responses={
    200: {
        'description': 'Successfully added ports'
    },
    500: {
        'description': 'Internal server error'
    }
})
def add_ports(daemon_id: str, port_protocol: str, database=Depends(get_database)):
    """
    Add ports
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.add_ports(port_protocol)


@router.post('/remove-ports', responses={
    200: {
        'description': 'Successfully removed ports'
    },
    500: {
        'description': 'Internal server error'
    }
})
def remove_ports(daemon_id: str, port_protocol: str, database=Depends(get_database)):
    """
    Remove ports
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.remove_ports(port_protocol)


@router.post('/add-port-forwarding', responses={
    200: {
        'description': 'Successfully added port forwarding'
    },
    500: {
        'description': 'Internal server error'
    }
})
def add_port_forwarding(daemon_id: str, port: str, protocol: str, to_port: str, database=Depends(get_database)):
    """
    Add port forwarding
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.add_port_forwarding(port, protocol, to_port)


@router.post('/remove-port-forwarding', responses={
    200: {
        'description': 'Successfully removed port forwarding'
    },
    500: {
        'description': 'Internal server error'
    }
})
def remove_port_forwarding(daemon_id: str, port: str, protocol: str, to_port: str, database=Depends(get_database)):
    """
    Remove port forwarding
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.remove_port_forwarding(port, protocol, to_port)


@router.post('/add-source-wtlst', responses={
    200: {
        'description': 'Successfully added source whitelist'
    },
    500: {
        'description': 'Internal server error'
    }
})
def add_source_wtlst(daemon_id: str, source_address: str, database=Depends(get_database)):
    """
    Add source whitelist
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.add_source_wtlst(source_address)


@router.post('/remove-source-wtlst', responses={
    200: {
        'description': 'Successfully removed source whitelist'
    },
    500: {
        'description': 'Internal server error'
    }
})
def remove_source_wtlst(daemon_id: str, source_address: str, database=Depends(get_database)):
    """
    Remove source whitelist
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.remove_source_wtlst(source_address)


@router.post('/add-source-blklst', responses={
    200: {
        'description': 'Successfully added source blacklist'
    },
    500: {
        'description': 'Internal server error'
    }
})
def add_source_blklst(daemon_id: str, source_address: str, database=Depends(get_database)):
    """
    Add source blacklist
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.add_source_blklst(source_address)


@router.post('/remove-source-blklst', responses={
    200: {
        'description': 'Successfully removed source blacklist'
    },
    500: {
        'description': 'Internal server error'
    }
})
def remove_source_blklst(daemon_id: str, source_address: str, database=Depends(get_database)):
    """
    Remove source blacklist
    """
    daemon_creds: DaemonSchema = database.query(DaemonSchema).filter_by(
        uuid=daemon_id).first()
    daemon = get_daemon(daemon_id, daemon_creds.url, daemon_creds.auth_key)
    return daemon.remove_source_blklst(source_address)
