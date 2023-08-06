import hashlib
import hmac
import json
from numbers import Number
from typing import Any, Dict, List, Optional, Union

import arrow
import requests
from furl import furl
from requests import Session

from .utils.constants import CRYPTO_LIST, IONOMY_URL_V1
from .utils.functions import get_price_uri


class Ionomy(object):
    def __init__(self, api_key: str, api_secret: str) -> None:
        if not api_secret: raise Exception('API SECRET must be provided')
        if not api_key: raise Exception('API KEY must be provided')

        self.api_key = api_key
        self.api_secret = api_secret

        self.base_url: str = IONOMY_URL_V1
        self.client: Session = requests.Session()
        self.market_names = [data["market"] for data in self._request('public/markets')]
    
    def _get_signature(self, endpoint: str, params: dict, timestamp: str) -> str:
        api_furl = furl(self.base_url + endpoint)
        api_furl.args = params
        url_ts = (api_furl.url + timestamp).encode('utf-8')
        return hmac.new(self.api_secret.encode('utf-8'), url_ts, hashlib.sha512 ).hexdigest()

    def _request(self, endpoint: str, params: dict={}, timestamp: str=str(arrow.utcnow().timestamp)):
        headers = {
            'api-auth-time': timestamp,
            'api-auth-key': self.api_key,
            'api-auth-token': self._get_signature(endpoint, params, timestamp)
        }

        response = self.client.get(self.base_url + endpoint, params=params, headers=headers)
        data = json.loads(response.content)

        if not data['success']:
            raise Exception(data['message'])
        return data['data']

    def markets(self) -> List[Dict[str, Any]]:
        return self._request('public/markets')

    def currencies(self) -> list:
        return self._request('public/currencies')
        
    def order_book(self, market: str) -> dict:
        return self._request('public/orderbook', {'market': market, 'type': 'both'})

    def market_summaries(self) -> list:
        return self._request('public/markets-summaries')

    def market_summary(self, market: str) -> dict:
        return self._request('public/market-summary', {'market': market})

    def market_history(self, market: str) -> list:
        return self._request('public/market-history', {'market': market})

    def limit_buy(self, market: str, amount: Union[int, float], price: Union[int, float]) -> dict:
        params = {
            'market': market,
            'amount': f'{amount:.8f}',
            'price': f'{price:.8f}'
        }
        return self._request('market/buy-limit', params)
    
    def limit_sell(self, market: str, amount: Union[int, float], price: Union[int, float]) -> dict:
        params = {
            'market': market,
            'amount': f'{amount:.8f}',
            'price': f'{price:.8f}'
        }
        return self._request('market/sell-limit', params)

    def cancel_order(self, orderId: str) -> str:
        failed = self._request('market/cancel-order', {'orderId': orderId})
        return '' if not failed else failed

    def open_orders(self, market: str) -> list:
        return self._request('market/open-orders', {'market': market})

    def balances(self) -> list:
        return self._request('account/balances')

    def balance(self, currency: str) -> dict:
        return self._request('account/balance', {'currency': currency})

    def deposit_address(self, currency: str) -> dict:
        return self._request('account/deposit-address', {'currency': currency})

    def deposit_history(self, currency: str) -> list:
        return self._request('account/deposit-history', {'currency': currency})

    def withdrawal_history(self, currency: str) -> dict:
        return self._request('account/withdrawal-history', {'currency': currency})

    def get_order_status(self, orderId: str) -> dict:
        return self._request('account/order', {'orderId': orderId})

    def get_spot_price(self, crypto: str="HIVE", currency: str='USD') -> float:
        data = self.client.get(get_price_uri(crypto, currency)).json()
        return data[crypto][currency]
