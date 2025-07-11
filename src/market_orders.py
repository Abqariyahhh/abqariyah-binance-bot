import sys
from utils import get_client, logger
from validate import validate_symbol, validate_quantity

client = get_client(mock=True) 

def place_market_order(symbol, side, quantity):
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
            logger.info(f"[MOCK] Market Order: {side.upper()} {quantity} {symbol}")
            print(f"✅ [SIMULATED] Market order: {side.upper()} {quantity} {symbol}")
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type="MARKET",
                quantity=quantity,
                positionSide="BOTH"
            )
            logger.info(f"Market Order Placed: {order}")
            print("✅ Market order placed successfully.")
    except Exception as e:
        logger.error(f"Error placing market order: {str(e)}")
        print("❌ Failed to place market order.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py SYMBOL SIDE QUANTITY")
        print("Example: python market_orders.py BTCUSDT BUY 0.01")
    else:
        _, symbol, side, quantity = sys.argv
        place_market_order(symbol, side, float(quantity))
