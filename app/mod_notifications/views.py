from . import notifications
from flask import current_app, jsonify
import requests

COINMARKET_CAP_API_URL = "https://api.coinmarketcap.com/v1/ticker/"
IFTT_BASE_URL = "https://maker.ifttt.com/trigger/{}/with/key/"

@notifications.route("/all", methods=["GET"])
def get_all_prices():
    response = requests.get(COINMARKET_CAP_API_URL)
    response_json = response.json()    
    return jsonify(response_json)


@notifications.route("/<str: cryptocurrency", methods=["GET"])
def get_latest_price(cryptocurrency):
    response = requests.get(COINMARKET_CAP_API_URL + f"/{cryptocurrency}")
    response_json = response.json()
    return jsonify(response_json[0])