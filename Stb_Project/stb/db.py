"""

This file is just created for use case in creating sqlite database of 2266 stocks.

"""

import os
from deta import Deta
from dotenv.main import load_dotenv
from .models import Stock


load_dotenv("/home/rahul/Desktop/Rahul/DE SEM 6/stock-prediction-bot/Stb_Project/.env")


DETA_KEY = os.environ.get("DETA_KEY")



def fetch_stocks_dec():
    # Fetch stocks data from cloud
    deta = Deta(DETA_KEY)
    stock_dec = deta.Base("StockDec")
    stocks_data = stock_dec._fetch()
    
    dl=stocks_data[1]['items']

    dd={}

    for dt in dl:
        dd[dt["key"]]=dt["Company"]
    return dd



def save_stocks_to_database(stocks):
    # Create Stock objects and save them to the database
    for symbol, company_name in stocks.items():
        # Check if the stock already exists in the database
        if not Stock.objects.filter(symbol=symbol).exists():
            # Create a new Stock object if it doesn't exist
            stock = Stock(symbol=symbol, company_name=company_name)
            stock.save()


