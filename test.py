import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
company='^NSEI'
ticker = yf.Ticker(company)
data = yf.download(company,start='2024-01-21',end='2024-01-31',interval='1d')


data = pd.read_csv('nse.csv')

data['Percentage Change'] = ((data['Close'] - data['Open']) / data['Open']) * 100
data.to_csv('Final_NSE.csv')

