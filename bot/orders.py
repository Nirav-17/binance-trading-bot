import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        
        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        # Add price only for LIMIT orders
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        # Log request
        logging.info(f"Order Request: {params}")

        # Place order
        response = client.place_order(**params)

        # Log response
        logging.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise