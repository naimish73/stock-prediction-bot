from __future__ import print_function
import os
from django.shortcuts import render,redirect
from .models import Stock
from .utils import get_data
from django.db.models import Q
import json

#upstox stuff
import time
import upstox_client
from upstox_client.rest import ApiException
from pprint import pprint
from dotenv.main import load_dotenv
import requests
"""
load_dotenv()
api_key = os.getenv('upstox_api_key')
secret_key = os.getenv('upstox_secret_key')
redirect_url='http://127.0.0.1:8000/'
authorization_code='s888eL'
headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

data = {
    'code': authorization_code,
    'client_id': api_key,
    'client_secret': secret_key,
    'redirect_uri': redirect_url,
    'grant_type': 'authorization_code',
}

def token():
    

    url = 'https://api.upstox.com/v2/login/authorization/token'
    

    response = requests.post(url, headers=headers, data=data)

    return response.json().get('access_token')

    

access_token=token()
# print("Access Token :")
print(access_token)


import requests

url = 'https://api.upstox.com/v2/market-quote/quotes?instrument_key=NSE_EQ%7CINE848E01016,NSE_EQ|INE669E01016'
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(url, headers=headers)

print(response.text)
# import requests

# url = "https://api.upstox.com/v2/option/chain"

# payload={
#     'instrument_key':'',

#     "expiry_date": "2024-02-15",
    
# }
# headers = {
#   'Accept': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
"""
def base(request):
    stocks = Stock.objects.all()
    
    # if request.method == 'GET':
    #     search = request.GET['q']
    #     stocks = Stock.objects.filter(Q(symbol__icontains=search) | Q(full_name__icontains=search))
    #     return redirect(request, 'stb/index.html',{'stocks':stocks})
    return render(request, 'stb/base.html',{'stocks':stocks})


def home(request):
    stocks = Stock.objects.all()
    search = None
    searched_stock_sym = None
    chart_div = None
    info=None

    if 'q' in request.GET:
        search = request.GET['q']


        searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]

        #Searched stocks graph
        fig = get_data.create_graph(searched_stock_sym,timeframe='5m') 
        chart_div = fig.to_html(full_html=True, default_height=700, default_width=1800)

        #Searched stocks info
        info = get_data.get_info(searched_stock_sym)
        print(info)

    else:
        stocks = Stock.objects.all()


    data = {'stocks': stocks, 'searched_stock': search, 'searched_stock_sym': searched_stock_sym, 'chart_div': chart_div, 'info': info}
    return render(request, 'stb/index.html', data)


def about(request):
    return render(request, 'stb/about.html')