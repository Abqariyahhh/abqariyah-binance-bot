import sys
from utils import get_client, logger
from validate import validate_symbol, validate_quantity

# Enable mock mode: Set to True if no API access
client = get_client(mock=True)

def place_limit_order(symbol, side, quantity, price):
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
            logger.info(f"[MOCK] Limit Order: {side.upper()} {quantity} {symbol} @ {price}")
            print(f"✅ [SIMULATED] Limit order: {side.upper()} {quantity} {symbol} @ {price}")
        else:
            client.futures_change_leverage(symbol=symbol, leverage=1)
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="LIMIT",
                timeInForce="GTC", 
                quantity=quantity,
                price=price,
                positionSide="BOTH"
            )
            logger.info(f"Limit Order Placed: {order}")
            print("✅ Limit order placed successfully.")
    except Exception as e:
        logger.error(f"Error placing limit order: {str(e)}")
        print("❌ Failed to place limit order.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py SYMBOL SIDE QUANTITY PRICE")
        print("Example: python limit_orders.py BTCUSDT SELL 0.01 60000")
    else:
        _, symbol, side, quantity, price = sys.argv
        place_limit_order(symbol, side, float(quantity), float(price))
