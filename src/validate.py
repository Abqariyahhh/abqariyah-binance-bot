def validate_symbol(symbol: str) -> bool:
    return symbol.upper().endswith("USDT")

def validate_quantity(qty) -> bool:
    try:
        return float(qty) > 0
    except:
        return False