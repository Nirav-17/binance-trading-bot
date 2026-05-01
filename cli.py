import click
from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logging

# Initialize logging
setup_logging()

@click.command()
@click.option('--symbol', required=True, help="Trading pair (e.g., BTCUSDT)")
@click.option('--side', required=True, help="BUY or SELL")
@click.option('--order_type', required=True, help="MARKET or LIMIT")
@click.option('--quantity', type=float, required=True, help="Order quantity")
@click.option('--price', type=float, default=None, help="Required for LIMIT orders")
def main(symbol, side, order_type, quantity, price):
    try:
        # Validate input
        validate_order(symbol, side, order_type, quantity, price)

        # Create client
        client = BinanceFuturesClient()

        # Print order summary
        print("\nPlacing Order...")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if order_type == "LIMIT":
            print(f"Price: {price}")

        # Place order
        response = place_order(
            client=client,
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        
        # Print response
        print("\n✅ Order Successful!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        #print(f"Executed Qty: {response.get('executedQty')}")
        #print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()