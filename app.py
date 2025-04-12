from flask import Flask, render_template, request, jsonify
import time
import hmac
import hashlib
import json
import requests

app = Flask(__name__)

COINDCX_API_URL = "https://api.coindcx.com/exchange/v1/orders/create"

def generate_signature(payload: dict, secret: str) -> str:
    """
    Generate HMAC SHA256 signature using API secret
    """
    serialized_payload = json.dumps(payload, separators=(',', ':'))
    return hmac.new(
        key=secret.encode('utf-8'),
        msg=serialized_payload.encode('utf-8'),
        digestmod=hashlib.sha256
    ).hexdigest()


def place_order(api_key: str, api_secret: str, side: str, quantity: float, price: float, market: str, demo: bool = False) -> dict:
    """
    Place a limit order on CoinDCX or simulate a demo order
    """
    if demo:
        return {
            "status": "demo",
            "message": "Simulated order placed.",
            "details": {
                "side": side,
                "quantity": quantity,
                "price": price,
                "market": market
            }
        }

    # Prepare payload
    timestamp = int(round(time.time() * 1000))
    payload = {
        "market": market.upper(),
        "side": side.lower(),  # must be "buy" or "sell"
        "order_type": "limit_order",
        "price_per_unit": price,
        "total_quantity": quantity,
        "timestamp": timestamp
    }

    # Generate signature
    try:
        signature = generate_signature(payload, api_secret)
    except Exception as e:
        return {"error": "Failed to generate signature", "details": str(e)}

    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "X-AUTH-APIKEY": api_key,
        "X-AUTH-SIGNATURE": signature
    }
    print("===================>>")
    print("Payload:", payload)
    print("Signature:", signature)
    print("Headers:", headers)


    # Make POST request
    try:
        response = requests.post(COINDCX_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": "HTTP error occurred", "details": str(http_err), "status_code": response.status_code, "response": response.text}
    except Exception as err:
        return {"error": "Unexpected error occurred", "details": str(err)}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/place_order', methods=['POST'])
def order_endpoint():
    try:
        data = request.get_json()
        api_key = data.get('api_key')
        api_secret = data.get('api_secret')
        side = data.get('side')
        quantity = float(data.get('quantity'))
        price = float(data.get('price'))
        market = data.get('market')
        demo = data.get('demo', False)

        # Input validation
        if not all([api_key, api_secret, side, quantity, price, market]):
            return jsonify({"error": "Missing required fields"}), 400

        result = place_order(api_key, api_secret, side, quantity, price, market, demo)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": "Failed to process request", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
