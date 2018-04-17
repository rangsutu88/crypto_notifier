import unittest
from unittest.mock import Mock, patch
from app.mod_crypto.services import get_latest_crypto_price, get_all_crypto_currency_prices
from tests import BaseTestCase

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


class CryptoServicesTestCase(BaseTestCase):

    @patch("app.mod_crypto.services.requests.get")
    def test_get_all_crypto_prices_returns_when_response_is_ok(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = crypto_currencies

        response = get_all_crypto_currency_prices()

        self.assertEqual(crypto_currencies, response)

    @patch("app.mod_crypto.services.requests.get")
    def test_get_all_crypto_currency_prices_returns_none_when_response_is_not_ok(self, mock_get):
        mock_get.return_value = Mock(ok=False)

        response = get_all_crypto_currency_prices()

        self.assertIsNone(response)

    @patch("app.mod_crypto.services.requests.get")
    def test_get_latest_crypto_currency_returns_currency_price_for_crypto(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = crypto_currencies

        response = get_latest_crypto_price("bitcoin")

        self.assertEqual(crypto_currencies[0], response)

    @patch("app.mod_crypto.services.requests.get")
    def test_get_latest_crypto_currency_returns_none_when_response_is_not_ok_for_crypto(self, mock_get):
        mock_get.return_value = Mock(ok=False)

        response = get_latest_crypto_price("bitcoin")

        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
