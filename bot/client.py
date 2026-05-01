import os
from binance.client import Client
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API keys not found. Check your .env file.")

        
        self.client = Client(api_key, api_secret)

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **kwargs):
        """
        Wrapper function to place futures orders
        """
        return self.client.futures_create_order(**kwargs)

    def get_balance(self):
        """
        Fetch futures account balance
        """
        return self.client.futures_account_balance()