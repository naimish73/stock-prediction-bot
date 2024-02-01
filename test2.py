import yfinance as yf
from datetime import datetime, timedelta

def get_max_intraday_data(ticker, interval):
    # Set a very large period to attempt to fetch maximum data available
    # Note: Yahoo Finance may limit the actual data returned
    max_period = "60d"
    stock = yf.download(ticker, interval=interval, period=max_period)
    return stock

# Example usage
ticker = "INFY"  # Example ticker for Nifty 50 index
interval = "5m"   # 5-minute interval

# Calculate the end date as today's date
# end_date = datetime.now().date()

# # Calculate the start date as 60 days before today's date
# start_date = end_date - timedelta(days=60)

max_intraday_data = get_max_intraday_data(ticker, interval)
# max_intraday_data.to_csv('Nifty50_shortTerm.csv')
print(max_intraday_data)
