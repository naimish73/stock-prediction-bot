
#yfinance data
import yfinance as yf
import pandas as pd
import pandas_ta as ta
from plotly import graph_objs as go
import mplfinance as mpf
import mpld3
import matplotlib as matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



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
    # List of indicator categories
    print(data.ta.indicators())

    # # Running a Categorical Strategy only requires the Category name
    # df.ta.strategy("Momentum") # Default values for all Momentum indicators
    # df.ta.strategy("overlap", length=42) # Override all Overlap 'length' attributes
    candlestick = go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'])
    layout = go.Layout(xaxis=dict(title='Date'), yaxis=dict(title='Price', side='right'))
    fig = go.Figure(data=[candlestick], layout=layout)
    return fig

create_graph('ITC.NS')

# NOT COMPLETE ( =========================== IN TESTING MODE ==================== )
def mpl_graph(symbol,timeframe='1m'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d', interval=timeframe)
    fig,ax=mpf.plot(data,type='candle',mav=(5,10,20),volume=True,style='yahoo',returnfig=True)
    html_str = mpld3.fig_to_html(fig)


    return html_str



