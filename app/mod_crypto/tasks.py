from app import celery
from .services import post_iftt_webhook_event, get_latest_crypto_price
from .constants import BITCOIN_PRICE_THRESHOLD
from .utils import format_crypto_history
from datetime import datetime


@celery.task()
def post_crypto_emergency():
    """
    Posts a crypto emergency. In this case only the bitcoin price is tracked
    """
    bitcoin = get_latest_crypto_price("bitcoin")

    if bitcoin:
        price = bitcoin["price_usd"]
        if price < BITCOIN_PRICE_THRESHOLD:
            post_iftt_webhook_event("bitcoin_price_emergency", price)


@celery.task()
def post_telegram_notification():
    """
    Posts a telegram notification
    """
    crypto_history = []
    bitcoin = get_latest_crypto_price("bitcoin")
    price = bitcoin["price_usd"]

    date = datetime.now()
    crypto_history.append({'date': date, 'price': price})

    post_iftt_webhook_event("bitcoin_price_update", format_crypto_history(crypto_history))
