import os
from deta import Deta
from dotenv.main import load_dotenv
import pandas as pd

load_dotenv(".env")
DETA_KEY = os.environ.get("deta_key")
deta= Deta(DETA_KEY)

stock_dec=deta.Base("StockDec")


def insert_user(symbol,Company):
    stock_dec.put({"key":symbol,"Company":Company})

# data = pd.read_excel("AllCompanies.xlsx")
# data['Symbol'] = data['Symbol'] + ".NS"

# for i in range(len(data)):
#     print(i)
#     print("\n\n")
#     print(data['Symbol'][i],data['Company Name'][i])
#     insert_user(data['Symbol'][i],data['Company Name'][i])


def fetch_stocks_dec():
    stocks_data=stock_dec._fetch()
    
    dl=stocks_data[1]['items']

    dd={}

    for dt in dl:
        dd[dt["key"]]=dt["Company"]
    return dd
