from typing import Optional

from fastapi import HTTPException


class Docker:
    def create_container(self, image: str, name: str, ports: Optional[dict[str, int]]):
        """
        Create a container
        """
        response = self.http_client.post('/docker/containers/create', {
            'image': image,
            'name': name,
            'ports': ports
        })
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not create container - ' + response.json()['detail'])
        return response.json()

    def get_container_details(self, container_id: str):
        """
        Get container details
        """
        response = self.http_client.get(f'/docker/containers/{container_id}')
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not get container details - ' + response.json()['detail'])
        return response.json()

    def delete_container(self, container_id: str, force: bool = False, v: bool = False):
        """
        Delete a container
        """
        response = self.http_client.post(f'/docker/containers/delete', {
            'container_id': container_id,
            'force': force,
            'v': v
        })
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not delete container - ' + response.json()['detail'])
        return response.json()

    def start_container(self, container_id: str):
        """
        Start a container
        """
        response = self.http_client.post(
            f'/docker/containers/{container_id}/start')
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not start container - ' + response.json()['detail'])
        return response.json()

    def stop_container(self, container_id: str):
        """
        Stop a container
        """
        response = self.http_client.post(
            f'/docker/containers/{container_id}/stop')
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not stop container - ' + response.json()['detail'])
        return response.json()

    def restart_container(self, container_id: str):
        """
        Restart a container
        """
        response = self.http_client.post(
            f'/docker/containers/{container_id}/restart')
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not restart container - ' + response.json()['detail'])
        return response.json()

    def kill_container(self, container_id: str):
        """
        Kill a container
        """
        response = self.http_client.post(
            f'/docker/containers/{container_id}/kill')
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not kill container - ' + response.json()['detail'])
        return response.json()
