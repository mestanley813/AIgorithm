import os
import logging
import time

from dotenv import load_dotenv
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

load_dotenv()
logging.basicConfig(filename="output.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='w')
logging.root.setLevel(logging.NOTSET)

class Account(object):
    def __init__(self):
        # API authentication and initialization
        self.key = os.getenv("ALPACA_KEY")
        self.secret = os.getenv("ALPACA_SECRET")
        self.api = TradingClient(self.key, self.secret, paper=True)
        self.logger = logging.getLogger()

    
    def placeBuyOrder(self, ticker):
        import database
        db = database.DB()
        # Cancels current order if there is one open
        closedPosition = self.api.close_all_positions(cancel_orders=True)

        # Update database if there is an existing closed position
        try:
            closedPosition = closedPosition[0].body.client_order_id
        except:
            pass
        else:
            time.sleep(15)
            sellPrice = self.api.get_order_by_client_id(closedPosition).filled_avg_price
            db.updateDB(sellPrice)

        # Creates an order to buy an asset
        self.logger.info(f'Attempting to buy {ticker}')
        try:
            self.api.get_asset(ticker)
        except:
            self.logger.error(f'Could not buy {ticker}')
        else:
            market_order_data = MarketOrderRequest(
                    symbol=ticker,
                    qty=1,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.GTC
                    )
            self.api.submit_order(order_data=market_order_data)
            self.logger.info(f'Bought {ticker}!')
            time.sleep(15)
            buyPrice = self.api.get_open_position(ticker).avg_entry_price
            db.insertDB(ticker, buyPrice)
            self.api.get_order_by_id