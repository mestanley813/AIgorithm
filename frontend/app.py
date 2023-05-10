from flask import Flask, render_template
from backend import database, purchase


def getBalance():
    acc = purchase.Account().api.get_account()
    return round(float (acc.equity) - float(acc.last_equity), 2)
def getBought():
    return database.database().collection.find({}).sort("date_of_purchase", -1).limit(1)[0]["symbol"]

def getSold():
    return database.database().collection.find({}).sort("date_of_purchase", -1).limit(2)[1]["symbol"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", balance_change=getBalance(), buy=getBought(), sell=getSold())