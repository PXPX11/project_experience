
import requests
import json
import base64
import hmac
import hashlib
import datetime
import time

base_url = "https://api.sandbox.gemini.com"
endpoint = "/v1/order/new"
url = base_url + endpoint

gemini_api_key = "account-zmidXEwP72yLSSybXVvn"
gemini_api_secret = "375b97HfE7E4tL8YaP3SJ239Pky9".encode()

t = datetime.datetime.now()
payload_nonce = str(int(time.mktime(t.timetuple())*1000))

payload = {
   "request": "/v1/order/new",
   "nonce": payload_nonce,
   "symbol": "btcusd",
   "amount": "5",
   "price": "3633.00",
   "side": "buy",
   "type": "exchange limit",
   "options": ["maker-or-cancel"]
}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

request_headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
}

response = requests.post(url,
                         data=None,
                         headers=request_headers)

new_order = response.json()
print(new_order)


########## 输出 ##########

{'order_id': '239088767', 'id': '239088767', 'symbol': 'btcusd', 'exchange': 'gemini', 'avg_execution_price': '0.00', 'side': 'buy', 'type': 'exchange limit', 'timestamp': '1561956976', 'timestampms': 1561956976535, 'is_live': True, 'is_cancelled': False, 'is_hidden': False, 'was_forced': False, 'executed_amount': '0', 'remaining_amount': '5', 'options': ['maker-or-cancel'], 'price': '3633.00', 'original_amount': '5'}