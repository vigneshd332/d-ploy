from fastapi import HTTPException


class DockerCompose:
    def docker_compose_up(self, compose_file: str, deployment_name: str, service: str,  build: bool, no_cache: bool):
        """
        Docker Compose up
        """
        response = self.http_client.post('/docker-compose/up', {
            'compose_file': compose_file,
            'deployment_name': deployment_name,
            'service': service,
            'build': build,
            'no_cache': no_cache
        })
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not start deployment - ' + response.json()['detail'])
        return response.json()

    def docker_compose_down(self, compose_file: str, deployment_name: str, service: str):
        """
        Docker Compose down
        """
        response = self.http_client.post('/docker-compose/down', {
            'compose_file': compose_file,
            'deployment_name': deployment_name,
            'service': service
        })
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not stop deployment - ' + response.json()['detail'])
        return response.json()
