from flask import Flask, render_template

import sys 
sys.path.append("..")

from backend import database, purchase

db = database.DB()

def getBalance():
    acc = purchase.Account().api.get_account()
    balance = round(float (acc.equity) - float(acc.last_equity), 2)
    return abs(balance)

def getBought():
    return db.collection.find({}).sort("date_of_purchase", -1).limit(1)[0]["symbol"]


def getSold():
    return db.collection.find({}).sort("date_of_purchase", -1).limit(2)[1]["symbol"]

app = Flask(__name__)

@app.route("/")
def index():
    stocks = db.collection.find().sort("date_of_purchase", -1).limit(9)

    return render_template("index.html", balance_change=getBalance(), buy=getBought(), sell=getSold(), stocks = stocks)

if __name__ == "__main__":
    app.run()