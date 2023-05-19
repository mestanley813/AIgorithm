# AIgorithm

## Live:
[ec2-3-144-88-5.us-east-2.compute.amazonaws.com](http://ec2-3-144-88-5.us-east-2.compute.amazonaws.com)

## Video Demo:
[https://www.youtube.com/watch?v=TBC4lEiHmMk](https://www.youtube.com/watch?v=TBC4lEiHmMk)

## Description:
An AI-powered flask web application that utilizes the OpenAI Davinci 3 model to recommmend stocks and the Alpaca Python API to execute buy orders based on the AI recommendations.

This information is input into a MongoDB database, and updated whenever the stock is sold.

## Features

* Real-time market data updates
* Automated stock tranding via the Alpaca Trading API
* Detailed transaction history and portfolio tracking

## Prerequisites
Before running AIgorithm, please ensure that you have the following installed on your machine:
* Python 3.7 or higher
* Flask
* OpenAI Python SDK
* Alpaca Trading API credentials
* MongoDB

## Installation
1. Clone the repository to your local machine:
```bash
git clone https://github.com/mestanley813/AIgorithm.git
```
2. Navigate the to project's directory and install the required dependancies:
```bash
pip install -r requirements.txt
```

3. Create a .env file and store your Alpaca, MongoDB, and OpenAI API keys saved as the following:

```
ALPACA_KEY
ALPACA_SECRET

OPENAI_ORGANIZATION
OPENAI_KEY

MONGO_HOST
MONGO_PASSWORD
MONGO_API 
```
4. Navigate into the backend folder and run main.py
```bash
python3 main.py
```

5. Navigate into the frontend folder and start flask
```bash
flask run
```

## Inspirations
Inspired by Michael Reeves's [I Gave My Goldfish $50,000 to Trade Stocks](https://www.youtube.com/watch?v=USKD3vPD6ZA)

and Fireship's [How to buy Stocks with JavaScript // Algo Trading Tutorial for Dummies](https://youtu.be/BrcugNqRwUs)