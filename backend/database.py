import os
import datetime

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class DB(object):
    def __init__(self):
        MONGO_HOST = os.getenv("MONGO_HOST")
        MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
        MONGO_API = os.getenv("MONGO_API")
        self.cluster = MongoClient(f"mongodb+srv://{MONGO_HOST}:{MONGO_PASSWORD}@{MONGO_API}")
        self.db = self.cluster["AIgorithmCluster"]
        self.collection = self.db["alpaca"]

    def insertDB(self, ticker, buy_price):
        post = {
            "symbol": ticker, 
            "date_of_purchase": datetime.datetime.now(),
            "buy_price": float(buy_price),
            }
        self.collection.insert_one(post)

    def updateDB(self, sell_price):
        # Find most recent document
        query = self.collection.find({}).sort("date_of_purchase", -1).limit(1)[0]
        net = float(sell_price) - float (query["buy_price"])

        self.collection.update_one(query, {
            "$set":{
                "sell_price": float(sell_price), 
                "net": float(net)
                }
        })