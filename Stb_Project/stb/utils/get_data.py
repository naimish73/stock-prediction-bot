
#yfinance data
import yfinance as yf
import pandas as pd
import pandas_ta as ta
from plotly import graph_objs as go
from plotly.subplots import make_subplots
import mplfinance as mpf
import datetime as dt
# import mpld3
# import matplotlib as matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

today = dt.date.today().strftime('%Y-%m-%d 09:15:00+05:30')
# today='2024-04-19 09:15:00+05:30'


def yf_data(symbol,timeframe='1m'):
    try:
        ticker = yf.Ticker(symbol)
        """
        Here we will fetch 1 extra day data so tha we can calculate the indicators values because will calculating it wastw the row as its lenght like sma 200 will pust first 200 rows values nan in its column so to avoid that we will get extra data to work on it and then showing only todays data. 
        """
        data = ticker.history(period='2d', interval=timeframe) 
        data.reset_index(inplace=True)
    
        data.drop(columns=['Volume', 'Dividends', 'Stock Splits'],axis=1, inplace=True)
    except Exception as e:
        return f"Please Check Your Internet!!! \n\n Exception is {e}"

    return data

def get_info(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.info
    l=['longName',
        'industry' 
       ,'website'
      ,'sector' 
      ,'longBusinessSummary' 
      ,'previousClose' 
      ,'open' 
      ,'dayLow' 
      ,'dayHigh' 
      ,'regularMarketPreviousClose' 
      ,'regularMarketOpen' 
      ,'regularMarketDayLow' 
      ,'regularMarketDayHigh' 
      ,'forwardPE' 
      ,'regularMarketVolume' 
      ,'marketCap' 
      ,'fiftyTwoWeekLow' 
      ,'fiftyTwoWeekHigh' 
      ,'fiftyDayAverage' 
      ,'twoHundredDayAverage' 
      ,'twoHundredDayAverage' 
      ,'profitMargins' 
      ,'52WeekChange' 
      ,'exchange' 
      ,'quoteType' 
      ,'symbol' 
      ,'currentPrice' 
      ,'revenuePerShare' 
      ,'revenueGrowth' 
      ,'earningsGrowth' 
      ,'debtToEquity' 
      ,'grossMargins' 
      ,'operatingMargins' 
      ,'revenueGrowth' 
      ,'recommendationKey' 
      ,'recommendationMean' ]
    data = {key: data[key] for key in l if key in data}
    
    
    
    return data

# print(get_info('INFY.NS'))
CustomStrategy_list=[
        {"kind": "sma", "length": 20},              #  |================= COMPLETE PLOTTING ==================|
        {"kind": "sma", "length": 50},              #  |================= COMPLETE PLOTTING ==================|
        # {"kind": "sma", "length": 200},               #  |================= COMPLETE PLOTTING ==================|
        # {"kind": "bbands", "length": 20},
        {"kind": "rsi","length": 14},               #  |================= COMPLETE PLOTTING ==================|
        # {"kind": "macd", "fast": 8, "slow": 21},
        # {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"},
    ]
    


def create_graph(symbol,CustomStrategy_list=CustomStrategy_list,timeframe='5m'):

    data = yf_data(symbol,timeframe)

    """
    This is for the CustomStrategy_list which contains different indicators and they have diffrent length so we are checking if the length is greater then length of data or greater than 200 then we will raise an error.
    """
    for candles in CustomStrategy_list:
        try:
            if candles['kind'] in ['sma','rsi','bbands']:
                l=candles['length']
                if len(data) <l or l>200:
                    print( f"{candles['kind']}_{candles['length']} is not valid !!!!!")
                    raise KeyError 
            elif candles['kind'] in ['macd']:
                pass
        except:
            pass
        

    CustomStrategy = ta.Strategy(
        name="Momo and Volatility",
        description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20",
        ta=CustomStrategy_list
    )
    try:
        data.ta.strategy(CustomStrategy)
    except Exception as e:
        return f"Please Check Your Internet \n\n Exception is {e}"
    s = data[data['Datetime'] == today]
    if not s.empty:
        date_index = s.index[0]
        data = data.iloc[date_index:]
        
    else:
        print("No data available for today's date.")

    candlestick = go.Candlestick(x=data.Datetime,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'],
                                 name='Candlestick')
    
    rsi = go.Scatter(x=data['Datetime'], y=data['RSI_14'], mode='lines', name='RSI 14',yaxis='y3')
    # macd1 = go.Scatter(x=data.Datetime, y=data['MACD_8_21_9'], mode='lines', name='MACD_8_21_9',yaxis='y2')
    # macd2 = go.Scatter(x=data.Datetime, y=data['MACDh_8_21_9'], mode='lines', name='MACDh_8_21_9',yaxis='y2')
    # macd3 = go.Scatter(x=data.Datetime, y=data['MACDs_8_21_9'], mode='lines', name='MACDs_8_21_9',yaxis='y2')

    sma_20 = go.Scatter(x=data['Datetime'], y=data['SMA_20'], mode='lines', name='SMA 20')
    sma_50 = go.Scatter(x=data['Datetime'], y=data['SMA_50'], mode='lines', name='SMA 50')
    # sma_200 = go.Scatter(x=data.Datetime, y=data['SMA_200'], mode='lines', name='SMA 200')


    stuff = [candlestick,rsi ,sma_20,sma_50]
    layout = go.Layout(
        yaxis3=dict(
            domain=[0, 0.2]
        ),
        yaxis2=dict(
            domain=[0.2, 0.4]
        ),
        yaxis=dict(
            domain=[0.4, 1]
        ),)

    # layout = go.Layout(xaxis=dict(title='Date'), yaxis=dict(title='Price', side='right'))
    fig = go.Figure(data=stuff, layout=layout)
    # fig.show()
    return fig

def quarterly_balance_sheet(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.quarterly_balance_sheet
        data.fillna(0, inplace=True)
    except Exception as e:
        print(f"Please check Your Internet Connection \n\n Exception : {e}")
        return f"Please check Your Internet Connection \n\n Exception : {e}"

    return data

print(quarterly_balance_sheet('ABCOTS.NS'))