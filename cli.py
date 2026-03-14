import argparse
from bot.orders import place_order
from bot.validators import validate_side, validate_type
from bot.logging_config import setup_logging

setup_logging()

parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--qty", type=float, required=True)
parser.add_argument("--price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_type(args.type)

    print("\nOrder Request Summary")
    print("Symbol:", args.symbol)
    print("Side:", args.side)
    print("Type:", args.type)
    print("Quantity:", args.qty)

    if args.type == "LIMIT":
        print("Price:", args.price)

    order = place_order(
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

    print("\nOrder Response")
    print("Order ID:", order["orderId"])
    print("Status:", order["status"])
    print("Executed Qty:", order["executedQty"])

except Exception as e:
    print("Error:", e)
