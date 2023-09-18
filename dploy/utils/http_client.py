"""
HTTP Client Class
"""
import requests


class HTTPClient():
    """HTTP client."""

    def __init__(self, base_url, headers=None):
        """Initialize HTTP client."""
        self.base_url = base_url
        self.headers = headers

    def get(self, path, params=None):
        """Perform GET request."""
        return self._request('GET', path, params=params)

    def post(self, path, data=None):
        """Perform POST request."""
        return self._request('POST', path, data=data)

    def _request(self, method, path, params=None, data=None):
        """Perform HTTP request."""
        url = self.base_url + path
        response = requests.request(
            method,
            url,
            params=params,
            json=data,
            headers=self.headers,
            timeout=10,
        )
        return response
