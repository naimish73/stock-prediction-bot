import pandas as pd
import yfinance as yf

def fetch_stock_livetime_data(symbol, period, interval):
    stock_data = yf.download(symbol, period=period, interval=interval)
    stock_data['timeframe'] = interval
    return stock_data

def main():
    symbol = 'TCS.NS'
    timeframes = {
        "1m": "1d",
        "2m": "1d",
        "5m": "1d",
        "10m": "1d",
        "15m": "1d",
        "30m": "60d",
        "60m": "60d",
        "90m": "60d",
        "1d": "max",
        "5d": "max",
        "1wk": "max",
        "1mo": "max",
        "3mo": "max",
        "6mo": "max",
        "1y": "max",
        "2y": "max",
        "5y": "max",
        "10y": "max",
        "ytd": "max",
    }

    try:
        combined_data = pd.DataFrame()  # Initialize an empty DataFrame
        for timeframe, period in timeframes.items():
            data = fetch_stock_livetime_data(symbol, period, timeframe)
            combined_data = combined_data.append(data)  # Append data to the DataFrame

        combined_data.to_csv('dataset/TCS.NS.csv')
        print('All data downloaded and saved to CSV successfully...')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
