import requests
from requests.auth import HTTPBasicAuth
import os
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()

class WooCommerceClient:
    def __init__(self):
        self.store_url = os.getenv('WOO_STORE_URL')
        self.consumer_key = os.getenv('WOO_CONSUMER_KEY')
        self.consumer_secret = os.getenv('WOO_CONSUMER_SECRET')
        self.base_url = f"{self.store_url}/wp-json/wc/v3"
        # Server Basic Auth (для доступа к сайту)
        self.server_user = os.getenv('WOO_SERVER_USER')
        self.server_password = os.getenv('WOO_SERVER_PASSWORD')
        self.server_auth = HTTPBasicAuth(self.server_user, self.server_password)

    def _get_params(self, extra: dict = None) -> dict:
        # WooCommerce ключи как query параметры
        params = {
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret,
        }
        if extra:
            params.update(extra)
        return params

    def get_products(self, limit: int = 10, orderby: str = 'date') -> List[Dict[str, Any]]:
        endpoint = f"{self.base_url}/products"
        params = self._get_params({'per_page': limit, 'orderby': orderby})
        response = requests.get(endpoint, auth=self.server_auth, params=params)
        response.raise_for_status()
        return response.json()

    def get_orders(self, limit: int = 10, status: str = 'any') -> List[Dict[str, Any]]:
        endpoint = f"{self.base_url}/orders"
        params = self._get_params({'per_page': limit, 'status': status})
        response = requests.get(endpoint, auth=self.server_auth, params=params)
        response.raise_for_status()
        return response.json()