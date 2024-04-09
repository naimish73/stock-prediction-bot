
#yfinance data
import yfinance as yf
import pandas as pd
from plotly import graph_objs as go
import mplfinance as mpf

def get_info(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.info
    l=['industry' 
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


def create_graph(symbol,timeframe='1m'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d', interval=timeframe)
    candlestick = go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'])
    layout = go.Layout(xaxis=dict(title='Date'), yaxis=dict(title='Price', side='right'))
    fig = go.Figure(data=[candlestick], layout=layout)
    return fig
        
def mpl_graph(symbol,timeframe='1m'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d', interval=timeframe)
    data['Date'] = data.index
    data['Date'] = pd.to_datetime(data['Date'])
    data['Date'] = data['Date'].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'))
    data = data[['Date','Open','High','Low','Close']]
    data = data.rename(columns={'Date':'Date','Open':'open','High':'high','Low':'low','Close':'close'})
    fig, ax = mpf.plot(data, type='candle', show_nontrading=True, returnfig=True)
    chart = mpf.make_mpf_style(base_mpf_style='yahoo', rc={'font.size': 6})
    mplfinance_html = mpf.plot_html(fig, rc=chart)

    return mplfinance_html 