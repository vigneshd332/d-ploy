
from fastapi import HTTPException


class Deployments:
    def create_deploy_using_git_https(self, username: str, password: str, remote_url: str, branch: str = None):
        """
        Create a deploy using git https
        """
        response = self.http_client.post('/deployments/create-with-git-https', {
            'username': username,
            'password': password,
            'repo_url': remote_url,
            'repo_branch': branch
        })
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not create deployment - ' + response.json()['detail'])
        return response.json()
