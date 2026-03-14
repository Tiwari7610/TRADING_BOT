from binance.client import Client

API_KEY = "LsnmsVqxvjSVoOAYeoHsRhnGzBrdkCPlSQhbDhutmPqKxt4UcuLwtYnSQcLmdC6U"
API_SECRET = "JIvMORkHMIpZi4oVFhdxtpe5QNYgqG6kPNc0qThzabpkHe94QkKIIUVL5knThdYk"

def get_client():

    client = Client(API_KEY, API_SECRET)

    # Correct Binance Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client