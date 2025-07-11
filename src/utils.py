import logging
import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def setup_logger():
    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()

logger = setup_logger()

def get_client(mock=False):
    if mock:
        return None 

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")
    client = Client(api_key, api_secret)
    client.API_URL = "https://testnet.binancefuture.com/fapi"
    return client
