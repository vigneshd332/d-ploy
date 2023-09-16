from functools import lru_cache
from fastapi import HTTPException, logger
from dploy.daemon.controllers.deployments import Deployments
from dploy.daemon.controllers.docker import Docker
from dploy.utils.http_client import HTTPClient


class Daemon(Deployments, Docker):

    def __init__(self, id: str, url: str, auth_key: str):
        self.id = id
        self.url = url
        self.http_client = HTTPClient(
            url, headers={'X-Dploy-Daemon-ID': id, 'X-Dploy-Daemon-Secret': auth_key})

        heartbeat = self.http_client.get('/')
        if heartbeat.status_code != 200:
            logger.error(f'Could not connect to daemon {id} at {url}')

    def __repr__(self) -> str:
        return f'<Daemon id={self.id} url={self.url}>'


@lru_cache()
def get_daemon(id: str, url: str, auth_key: str):
    return Daemon(id, url, auth_key)
