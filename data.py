import yfinance as yf
import pandas as pd
import os

def load_prices(ticker, start, end):
    path = f'data/{ticker}_{start}_{end}.csv'

    if os.path.exists(path):
        return pd.read_csv(path, parse_dates=True, index_col=0).squeeze()
    else:
        yf.download(ticker, start=start, end=end)['Close'].to_csv(path)
        return pd.read_csv(path, parse_dates=True, index_col=0).squeeze()
    
    