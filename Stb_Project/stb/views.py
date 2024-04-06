from __future__ import print_function
import os
from django.shortcuts import render
from .models import Stock

#upstox stuff
import time
import upstox_client
from upstox_client.rest import ApiException
from pprint import pprint
from dotenv.main import load_dotenv

load_dotenv()

api_key = os.getenv('upstox_secret_key')


# Configure OAuth2 access token for authorization: OAUTH2
configuration = upstox_client.Configuration()
configuration.access_token = api_key

# create an instance of the API class
api_instance = upstox_client.WebsocketApi(upstox_client.ApiClient(configuration))
api_version = 'v2' # str | API Version Header

try:
    # Market Data Feed
    api_instance.get_market_data_feed(api_version)
except ApiException as e:
    print("Exception when calling WebsocketApi->get_market_data_feed: %s\n" % e)
    print("Not Done")

import requests

url = "https://api.upstox.com/v2/option/chain"

payload={
    'instrument_key':'',

    "expiry_date": "2024-02-15",
    
}
headers = {
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
def home(request):
    stocks = Stock.objects.all()
    search = None
    searched_stock_sym = None

    if 'q' in request.GET:
        search = request.GET['q']
        print(search)
        searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)
        searched_stock_sym = searched_stock_sym[0]

    data = {'stocks': stocks, 'searched_stock': search, 'searched_stock_sym': searched_stock_sym}
    return render(request, 'stb/index.html', data)
