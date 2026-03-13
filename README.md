# Binance Futures Trading Bot

A simple Python CLI bot that places orders on Binance Futures Testnet.

## Setup

1 Install Python
2 Install dependencies

pip install -r requirements.txt

3 Add API keys in client.py

4 Run bot

Example:

Market order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

Limit order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 65000

## Logs

Logs saved in:

trading_bot.log