import logging
from bot.client import get_client

client = get_client()

def place_order(symbol, side, order_type, quantity, price=None):

    try:

        if order_type == "MARKET":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        logging.info(f"Order Response: {order}")

        return order

    except Exception as e:
        logging.error(f"Order Failed: {str(e)}")
        print("Order Failed:", e)