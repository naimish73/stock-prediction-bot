from __future__ import print_function
import os
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Stock
from .utils import get_data,get_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
import pandas as pd

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
authorization_code='IQ_wGH'
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
    

    response = requests.post(url, headers=headers, data=pyload)

    return response.json().get('access_token')

    

access_token="eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiIzR0FVNjMiLCJqdGkiOiI2NjE2MjYyZGJjNzYxMzMxNDk3ODJiZWIiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNBY3RpdmUiOnRydWUsInNjb3BlIjpbImludGVyYWN0aXZlIiwiaGlzdG9yaWNhbCJdLCJpYXQiOjE3MTI3Mjc1OTcsImlzcyI6InVkYXBpLWdhdGV3YXktc2VydmljZSIsImV4cCI6MTcxMjc4NjQwMH0.ov8V1p6GgKc9fSRXTNK1j8gCTKgTDXDMxp0509Wr92E"#token()
# print("Access Token :")
print(access_token)


import requests

url = 'https://api.upstox.com/v2/market-quote/quotes?instrument_key=NSE_EQ%7CINE848E01016,NSE_EQ|INE669E01016'

market_feed_url  = "https://api.upstox.com/v2/feed/market-data-feed"

headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

pyload={
  "guid": "someguid",
  "method": "sub",
  "data": {
    "mode": "full",
    "instrumentKeys": ["NSE_INDEX|Nifty Bank"]
  }
}

# response = requests.get(url, headers=headers)
response = requests.request("GET", market_feed_url, headers=headers, data=data)


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

stocks = Stock.objects.all() # Get all stocks from the database


def signup(request):
    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ username)
            return redirect('login')
    else:
        form= CreateUserForm()
    return render(request, 'registration/signup.html', {'form':form})

def Login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.info(request,'Username or Password is incorrect')
    return render(request, 'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    
    # Home Page hero section starting
    Nifty_chart_div = get_data.create_graph('^NSEI',timeframe='1m')
    Nifty_chart = Nifty_chart_div.to_html(full_html=True, default_height=700, default_width=1800)

    BankNifty_chart = get_data.create_graph('^NSEBANK',timeframe='1m')
    BankNifty_chart = BankNifty_chart.to_html(full_html=True, default_height=700, default_width=1800)

    Sensex_chart = get_data.create_graph('^BSESN',timeframe='1m')
    Sensex_chart = Sensex_chart.to_html(full_html=True, default_height=700, default_width=1800)



    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)


    data = {
        'stocks': stocks,
        'Nifty_chart':Nifty_chart, 
        'BankNifty_chart':BankNifty_chart, 
        'Sensex_chart':Sensex_chart, 
    }

    return render(request, 'stb/index.html', data)

    
@login_required(login_url='login')
def chart(request):
    chart_div = None
    info = None

    if 'q' in request.GET:
        searched_stock = request.GET['q']
        stock_symbol = Stock.objects.filter(full_name__icontains=searched_stock).values_list('symbol', flat=True)[0]

        #Searched stocks graph
        fig = get_data.create_graph(stock_symbol,timeframe='5m') 
        chart_div = fig.to_html(full_html=True, default_height=700, default_width=1800)

        #Searched stocks info
        info = get_data.get_info(stock_symbol)

    data={
        'stocks': stocks,
        'searched_stock': stock_symbol,
        'chart_div': chart_div,
        'info': info
    }

    return render(request, 'stb/charts.html', data)

@login_required(login_url='login')
def ta(request):
    decision1_tree_chart = None
    randomeforest_tree_chart = None
    xgboost_tree_chart = None



    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)

    try:
        xgboost_tree_chart= get_model.XgBoost_predict('^NSEI')

    except:
        pass


    try:
        randomeforest_tree_chart= get_model.RandomForest_predict('^NSEI')

    except:
        pass


    try:

        decision1_tree_chart= get_model.DecisionTree_predict('^NSEI')
    except:
        pass


    decision1_tree_chart = decision1_tree_chart.to_html(full_html=True, default_height=700, default_width=1800)
    randomeforest_tree_chart = randomeforest_tree_chart.to_html(full_html=True, default_height=700, default_width=1800)
    xgboost_tree_chart = xgboost_tree_chart.to_html(full_html=True, default_height=700, default_width=1800)
    
    data={
        'stocks':stocks,
        'decision1_tree_chart':decision1_tree_chart,
        'randomeforest_tree_chart':randomeforest_tree_chart,
        'xgboost_tree_chart':xgboost_tree_chart
    }
    return render(request, 'stb/technical.html',data)

@login_required(login_url='login')
def fundamental(request):

    Qdata= get_data.quarterly_balance_sheet('INFY.NS')
    Qdata.columns = [col.strftime("%b. %d, %Y") if isinstance(col, pd.Timestamp) else col for col in Qdata.columns]




    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)

    data={
        'stocks':stocks,
        'Qdata':Qdata
    }
    return render(request, 'stb/fundamental.html',data)

@login_required(login_url='login')
def about(request):

    if 'q' in request.GET:
        search = request.GET['q']

        # searched_stock_sym = Stock.objects.filter(full_name__icontains=search).values_list('symbol', flat=True)[0]
        search = Stock.objects.filter(full_name__icontains=search).values_list('full_name', flat=True)[0]
        # print(searched_stock_sym)
        charts='/chart/?q='+search
        return HttpResponseRedirect(charts)


    data={
        'stocks':stocks
    }
    return render(request, 'stb/about.html',data)