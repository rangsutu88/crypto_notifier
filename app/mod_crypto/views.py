from . import crypto
from flask import current_app, jsonify
from .services import get_all_crypto_currency_prices, get_latest_crypto_price, post_iftt_webhook_event


@crypto.route("/all", methods=["GET"])
def get_all_prices():
    response = get_all_crypto_currency_prices()
    if response:
        return jsonify(response)
    else:
        return jsonify({
            "message": "Could not find Crypto currency prices",
            "success": False
        }), 404


@crypto.route("/<string:crypto_currency>", methods=["GET"])
def get_latest_price(crypto_currency):
    response = get_latest_crypto_price(crypto_currency)
    if response:
        return jsonify(response)
    else:
        return jsonify({
            "message": f"Could not find price for {crypto_currency}",
            "success": False
        }), 404


def post_iftt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'value1': value}
    post_iftt_webhook_event(event, data)