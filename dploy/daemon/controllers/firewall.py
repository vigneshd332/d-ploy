
from fastapi import HTTPException


class Firewall:
    def get_all_zones(self):
        """
        Get all zones
        """
        response = self.http_client.get('/firewall/get-all-zones')
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not get all zones - ' + response.json()['detail'])
        return response.json()

    def get_zone_config(self, zone: str):
        """
        Get zone config
        """
        response = self.http_client.get(
            f'/firewall/get-zone-config?zone={zone}')
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not get zone config - ' + response.json()['detail'])
        return response.json()

    def add_service(self, service_name: str):
        """
        Add service
        """
        response = self.http_client.post(
            f'/firewall/add-service', {'service_name': service_name})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not add service - ' + response.json()['detail'])
        return response.json()

    def remove_service(self, service_name):
        """
        Remove service
        """
        response = self.http_client.post(
            f'/firewall/remove-service', {'service_name': service_name})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not remove service - ' + response.json()['detail'])
        return response.json()

    def add_ports(self, port_protocol: str):
        """
        Add ports
        """
        response = self.http_client.post(
            f'/firewall/add-ports', {'port_protocol': port_protocol})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not add ports - ' + response.json()['detail'])
        return response.json()

    def remove_ports(self, port_protocol: str):
        """
        Remove ports
        """
        response = self.http_client.post(
            f'/firewall/remove-ports', {'port_protocol': port_protocol})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not remove ports - ' + response.json()['detail'])
        return response.json()

    def add_port_forwarding(self, port: str, protocol: str, to_port: str):
        """
        Add port forwarding
        """
        response = self.http_client.post(
            f'/firewall/add-port-forwarding', {'port': port, 'protocol': protocol, 'to_port': to_port})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not add port forwarding - ' + response.json()['detail'])
        return response.json()

    def remove_port_forwarding(self, port: str, protocol: str, to_port: str):
        """
        Remove port forwarding
        """
        response = self.http_client.post(
            f'/firewall/remove-port-forwarding', {'port': port, 'protocol': protocol, 'to_port': to_port})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not remove port forwarding - ' + response.json()['detail'])
        return response.json()

    def add_source_wtlst(self, source_address: str):
        """
        Add source whitelist
        """
        response = self.http_client.post(
            f'/firewall/add-source-wtlst', {'source_address': source_address})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not add source whitelist - ' + response.json()['detail'])
        return response.json()

    def remove_source_wtlst(self, source_address: str):
        """
        Remove source whitelist
        """
        response = self.http_client.post(
            f'/firewall/remove-source-wtlst', {'source_address': source_address})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not remove source whitelist - ' + response.json()['detail'])
        return response.json()

    def add_source_blklst(self, source_address: str):
        """
        Add source blacklist
        """
        response = self.http_client.post(
            f'/firewall/add-source-blklst', {'source_address': source_address})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not add source blacklist - ' + response.json()['detail'])
        return response.json()

    def remove_source_blklst(self, source_address: str):
        """
        Remove source blacklist
        """
        response = self.http_client.post(
            f'/firewall/remove-source-blklst', {'source_address': source_address})
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail='Could not remove source blacklist - ' + response.json()['detail'])
        return response.json()
