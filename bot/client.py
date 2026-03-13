from binance.client import Client

API_KEY = "tUG8tdF3ay4DILj9Kpmll2nizDM4Qf5mL0Kalwd4oJQ7vJlJT4IiYALN6HuF5wic"
API_SECRET = "gDT6LKbBTc0ShquTWHvuTHWAZD2zD5ONn029BwNF06gk5Pj3sCqad41sndUUc69A"

BASE_URL = "https://testnet.binancefuture.com"

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = BASE_URL
    return client