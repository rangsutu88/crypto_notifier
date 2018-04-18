from . import crypto
from flask import jsonify
from .services import get_all_crypto_currency_prices, get_latest_crypto_price


@crypto.route("/all", methods=["GET"])
def get_all_prices():
    """
    Gets all prices for crypto currencies
    :return: JSONIFY response
    """
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
    """
    Gets the price for a single crypto currency
    :param crypto_currency: Crypto currency to get information for
    :return:
    """
    response = get_latest_crypto_price(crypto_currency)
    if response:
        return jsonify(response)
    else:
        return jsonify({
            "message": f"Could not find price for {crypto_currency}",
            "success": False
        }), 404
