import yfinance as yf
import pandas_ta as ta
from plotly import graph_objs as go
import mplfinance as mpf

def create_graph(symbol,timeframe='1m'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d', interval=timeframe)
    # List of indicator categories
    
    CustomStrategy = ta.Strategy(
    name="Momo and Volatility",
    description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20",
    ta=[
        {"kind": "sma", "length": 50},
        {"kind": "sma", "length": 200},
        # {"kind": "bbands", "length": 20},
        # {"kind": "rsi"},
        # {"kind": "macd", "fast": 8, "slow": 21},
        # {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"},
    ]
    )
    # To run your "Custom Strategy"
    data.ta.strategy(CustomStrategy)
    print(data.columns)

    # # Running a Categorical Strategy only requires the Category name
    # df.ta.strategy("Momentum") # Default values for all Momentum indicators
    # df.ta.strategy("overlap", length=42) # Override all Overlap 'length' attributes
    candlestick = go.Candlestick(x=data.index,
                                 open=data['Open'],
                                 high=data['High'],
                                 low=data['Low'],
                                 close=data['Close'])
    

    # Creating traces for each indicator
    sma_50_trace = go.Scatter(x=data.index, y=data['SMA_50'], mode='lines', name='SMA 50')
    sma_200_trace = go.Scatter(x=data.index, y=data['SMA_200'], mode='lines', name='SMA 200')
    # rsi_trace = go.Scatter(x=data.index, y=data['RSI_14'], mode='lines', name='RSI')
    # macd_trace = go.Scatter(x=data.index, y=data['MACDh_8_21_9'], mode='lines', name='MACD Histogram')
    # volume_sma_trace = go.Scatter(x=data.index, y=data['VOLUME_SMA_20'], mode='lines', name='Volume SMA 20')
    
    # Combining all traces into a single figure
    layout = go.Layout(title=f"{symbol} Stock Analysis",
                       xaxis=dict(title='Date'),
                       yaxis=dict(title='Price', side='right'))
    fig = go.Figure(data=[candlestick, sma_50_trace, sma_200_trace], layout=layout)
    
    # Show the figure
    fig.show()

def mpl_graph(symbol,timeframe='5m'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d', interval=timeframe)
    mpf.plot(data,type='candle',mav=(5,10,20),volume=True,style='yahoo',returnfig=False)
    mpf.show()

