import pandas as pd
import pandas_ta as ta
import yfinance as yf
import datetime as dt
import pandas_ta as ta
import streamlit as st
import plotly.graph_objects as go
from db import fetch_stocks_dec



start = dt.datetime.now().strftime('%Y-%m-%d')
end = (dt.datetime.now() + dt.timedelta(days=1)).strftime('%Y-%m-%d')




def Fetch_data(symbol,timeframe):
    ticker = yf.Ticker(symbol)
    df = ticker.history(start=start, end=end, interval=timeframe)

    supertrend = df.ta.supertrend()
    df.reset_index(inplace=True)
    supertrend.reset_index(inplace=True)
    # supertrend = supertrend.drop(columns=["Datetime"])

    # Merge df and supertrend
    merged_df = pd.merge(df, supertrend, on="Datetime")


    return merged_df


def plot_graph(df):
    fig = go.Figure()

    # Plot close line
    fig.add_trace(go.Scatter(x=df['Datetime'], y=df['Close'], name='Close', line=dict(color='blue')))
    # Plot supertrend lines
    fig.add_trace(go.Scatter(x=df['Datetime'], y=df['SUPERTl_7_3.0'], name='Supertrend Long', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=df['Datetime'], y=df['SUPERTs_7_3.0'], name='Supertrend Short', line=dict(color='red')))
    # Configure layout
    fig.update_layout(title='Stock Price with Supertrend', xaxis_title='Datetime', yaxis_title='Price')

    # Show the plot
    st.plotly_chart(fig)

def main_app():
    st.session_state['s']= 0
    if st.session_state.s==0:
        st.session_state.s+=1
        try:
            stocks= fetch_stocks_dec()
            symbols = stocks.keys()
            companies = stocks.values()
        except:
            st.write("Error in fetching data from database")
            st.stop()

    company=st.selectbox("Select Company",companies)
    symbol = list(stocks.keys())[list(stocks.values()).index(company)]

    with st.empty():
        st.header(company)
        df = Fetch_data(symbol, "1m")
        st.write(df)
        plot_graph(df)


main_app()