import requests
from .constants import COINMARKET_CAP_API_URL, IFTTT_BASE_URL


def get_all_crypto_currency_prices():
    """
    Gets all crypto currency prices
    :return: Response in json format
    """
    response = requests.get(COINMARKET_CAP_API_URL)
    if response.ok:
        return response.json()
    else:
        return None


def get_latest_crypto_price(crypto_currency):
    """
    Gets the latest crypto currency price
    :param crypto_currency: Crypto currency
    :return: Response for the latest crypto currency
    """
    response = requests.get(COINMARKET_CAP_API_URL + f"/{crypto_currency}")
    if response.ok:
        response_json = response.json()
        return response_json[0]
    else:
        return None


def post_iftt_webhook_event(event, data):
    """
    Posts IFTTT webhook event
    :param event: event to post
    :param data: data to send
    :return:
    """
    ifttt_event_url = IFTTT_BASE_URL.format(event)
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=data)
