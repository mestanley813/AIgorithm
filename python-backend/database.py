import os
import datetime

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
cluster = MongoClient(f"mongodb+srv://mestanley813:{MONGO_PASSWORD}@aigorithmcluster.hsloxug.mongodb.net/?retryWrites=true&w=majority")
db = cluster["AIgorithmCluster"]
collection = db["alpaca"]

def insertDB(ticker, buy_price):
    post = {
        "symbol": ticker, 
        "date_of_purchase": datetime.datetime.now(),
        "buy_price": float(buy_price),
        }
    collection.insert_one(post)

def updateDB(sell_price):
    # Find most recent document
    query = collection.find({}).sort("date_of_purchase", -1).limit(1)[0]
    net = float(sell_price) - float (query["buy_price"])

    collection.update_one(query, {
        "$set":{
            "sell_price": float(sell_price), 
            "net": float(net)
            }
    })