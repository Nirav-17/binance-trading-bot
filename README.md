# Binance Futures Trading Bot (Testnet)

##  Overview

Python CLI bot to place Market and Limit orders on Binance Futures Testnet with validation and logging.

---

##  Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

---

##  Run

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.01
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.01 --price 70000
```

---

##  Notes

* Uses Binance Futures Testnet (no real funds)
* Logs stored in `trading_bot.log`

---

##  Structure

```
bot/
  client.py
  orders.py
  validators.py
  logging_config.py

cli.py
requirements.txt
```
