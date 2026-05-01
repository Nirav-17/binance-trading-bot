def validate_order(symbol, side, order_type, quantity, price):
    # Symbol check
    if not symbol:
        raise ValueError("Symbol is required (e.g., BTCUSDT)")

    # Side check
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    # Order type check
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    # Quantity check
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    # Price required for LIMIT orders
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")