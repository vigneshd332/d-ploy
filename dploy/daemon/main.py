from functools import lru_cache
from fastapi import HTTPException
import logging
from dploy.daemon.controllers.deployments import Deployments
from dploy.daemon.controllers.docker import Docker
from dploy.daemon.controllers.docker_compose import DockerCompose
from dploy.utils.http_client import HTTPClient


class Daemon(Deployments, Docker, DockerCompose):

    def __init__(self, id: str, url: str, auth_key: str):
        self.id = id
        self.url = url
        self.auth_key = auth_key
        self.http_client = HTTPClient(
            url, headers={'X-Dploy-Daemon-ID': id, 'X-Dploy-Daemon-Secret': auth_key})

        heartbeat = self.http_client.get('/')
        if heartbeat.status_code != 200:
            logging.error(f'Could not connect to daemon {id} at {url}')

    def __repr__(self) -> str:
        return f'<Daemon id={self.id} url={self.url}>'

    def register_daemon(self):
        """
        Register daemon
        """
        response = self.http_client.post('/register', data={
            'id': self.id,
            'auth_key': self.auth_key
        })
        if response.status_code != 200:
            print(response.json())
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not register daemon - ' + response.json()['detail'])
        return response.json()


@lru_cache()
def get_daemon(id: str, url: str, auth_key: str):
    return Daemon(id, url, auth_key)
