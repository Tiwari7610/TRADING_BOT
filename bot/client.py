from binance.client import Client

API_KEY = "IEmFEqkjCqQXtjMZt7laSsQMtKAsG2OgUK5nR8L2TEjhtb8cdiDP3nSWpr3od5QL"
API_SECRET = "gVSng6NDv0OdorPkhALfuw39KB0GSmKenAz4DwHHQF3A1U7MlVOhsm76SC3DgMzX"

BASE_URL = "https://testnet.binancefuture.com"

def get_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = BASE_URL
    return client