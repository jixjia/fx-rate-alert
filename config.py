# Currency FX rate settings
BASE_URL = 'https://www.x-rates.com/calculator/?from={}&to={}&amount=1'
BASE_CURRENCY = 'JPY'
TO_CURRENCY_LIST = ['AUD', 'CNY', 'USD', 'GBP']

# Alert threshold for sending push notification
ALERT_THRESHOLD = [
    {'fx_pair': 'JPY/AUD', 'buy-threshold': 0.0134, 'sell-threshold': 0.0137},
    {'fx_pair': 'JPY/USD', 'buy-threshold': 0.009, 'sell-threshold': 0.01},
    {'fx_pair': 'JPY/CNY', 'buy-threshold': 0.06, 'sell-threshold': 0.07}
]

# Twillio Auth & Token
TO = '{YOUR_MOBILE_NUMBER}'
FROM_ = '{YOUR_TWILIO_NUMBER}'
ACCOUNT_SID = '{YOUR_SID}'
AUTH_TOKEN = '{YOUR_TOKEN}'
