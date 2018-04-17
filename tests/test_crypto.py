import json
import unittest
from tests import BaseTestCase
from unittest.mock import Mock, patch

crypto_currencies = [
    {'24h_volume_usd': '14439800.0',
     'available_supply': '135787539.0',
     'id': 'storj',
     'last_updated': '1523939652',
     'market_cap_usd': '129282637.0',
     'max_supply': None,
     'name': 'Storj',
     'percent_change_1h': '0.05',
     'percent_change_24h': '-1.13',
     'percent_change_7d': '28.56',
     'price_btc': '0.00011904',
     'price_usd': '0.952095',
     'rank': '99',
     'symbol': 'STORJ',
     'total_supply': '424999998.0'},
    {'24h_volume_usd': '2893510.0',
     'available_supply': '8048879.0',
     'id': 'skycoin',
     'last_updated': '1523939652',
     'market_cap_usd': '128903602.0',
     'max_supply': '100000000.0',
     'name': 'Skycoin',
     'percent_change_1h': '0.64',
     'percent_change_24h': '-2.54',
     'percent_change_7d': '2.78',
     'price_btc': '0.00200231',
     'price_usd': '16.0151',
     'rank': '100',
     'symbol': 'SKY',
     'total_supply': '25000000.0'}
]


class CryptoTestCases(BaseTestCase):
    """Crypto Test cases"""

    @classmethod
    def setUpClass(cls):
        cls.mock_get_patcher = patch("app.mod_crypto.services.requests.get")
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.mock_get_patcher.stop()

    def test_get_all_prices_returns_200_on_get_request(self):
        self.mock_get.return_value = Mock(ok = True)
        self.mock_get.return_value.json.return_value = crypto_currencies

        response = self.client.get("/crypto/all", follow_redirects=True)
        self.assert200(response)

        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(crypto_currencies, response_json)

    def test_get_all_prices_returns_404_on_get_request_when_response_is_not_ok(self):
        self.mock_get.return_value.ok = False
        response = self.client.get("/crypto/all", follow_redirects=True)

        self.assert404(response)
        self.assertIn(b"Could not find Crypto currency prices", response.data)
        self.assertIn(b"false", response.data)

    def test_get_all_prices_returns_405_on_post_request(self):
        self.mock_get.return_value.ok = False
        response = self.client.post("/crypto/all", follow_redirects=True)
        self.assert405(response)


if __name__ == "__main__":
    unittest.main()
