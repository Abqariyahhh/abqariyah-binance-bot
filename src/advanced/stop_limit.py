import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  

from utils import get_client, logger
from validate import validate_symbol, validate_quantity

client = get_client(mock=True)

def place_stop_limit_order(symbol, side, quantity, stop_price, limit_price):
    try:
        if not validate_symbol(symbol):
            logger.error("Invalid symbol.")
            print("❌ Invalid symbol.")
            return

        if not validate_quantity(quantity):
            logger.error("Invalid quantity.")
            print("❌ Invalid quantity.")
            return

        if client is None:
            logger.info(f"[MOCK] Stop-Limit Order: {side.upper()} {quantity} {symbol} | Stop: {stop_price}, Limit: {limit_price}")
            print(f"✅ [SIMULATED] Stop-Limit order: {side.upper()} {quantity} {symbol} | Stop: {stop_price}, Limit: {limit_price}")
        else:
            client.futures_change_leverage(symbol=symbol, leverage=1)
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="STOP_MARKET",
                stopPrice=stop_price,
                closePosition=False,
                quantity=quantity,
                price=limit_price,
                timeInForce="GTC",
                positionSide="BOTH",
                reduceOnly=False
            )
            logger.info(f"Stop-Limit Order Placed: {order}")
            print("✅ Stop-Limit order placed successfully.")
    except Exception as e:
        logger.error(f"Error placing stop-limit order: {str(e)}")
        print("❌ Failed to place stop-limit order.")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python stop_limit.py SYMBOL SIDE QUANTITY STOP_PRICE LIMIT_PRICE")
        print("Example: python stop_limit.py BTCUSDT SELL 0.01 58000 57900")
    else:
        _, symbol, side, quantity, stop_price, limit_price = sys.argv
        place_stop_limit_order(symbol, side, float(quantity), float(stop_price), float(limit_price))
