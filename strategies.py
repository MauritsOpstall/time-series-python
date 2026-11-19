import numpy as np
import pandas as pd

def sma_crossover(prices, short, long):
    """
    Simple Moving Average (SMA) Crossover Strategy.

    Parameters:
    - prices: A pandas Series of stock prices.
    - short: The window size for the short-term SMA.
    - long: The window size for the long-term SMA.

    Returns:
    - A pandas Series of signals where 1 indicates a long signal and 0 indicates a flat signal.
    """
    # Calculate short-term and long-term SMAs
    short_sma = prices.rolling(window=short).mean()
    long_sma = prices.rolling(window=long).mean()


    # Generate signals
    results = short_sma > long_sma
    
    
    return results.astype(int)

def momentum(prices, lookback):
    """
    Momentum Strategy.

    Parameters:
    - prices: A pandas Series of stock prices.
    - lookback: The number of periods to look back for momentum calculation.

    Returns:
    - A pandas Series of signals where 1 indicates a long signal and 0 indicates a flat signal.
    """
    # Calculate momentum
    past_returns = prices.pct_change(periods=lookback)

    # Generate signals
    results = past_returns > 0

    return results.astype(int)

def rsi(prices, n):
    """
    Relative Strength Index (RSI) Strategy.

    Parameters:
    - prices: A pandas Series of stock prices.
    - n: The number of periods to use for RSI calculation.

    Returns:
    - A pandas Series of RSI values.
    """
    delta = prices.diff()
    
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)


    avg_gain = gain.ewm(alpha=1/n, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/n, adjust=False).mean()

    rs_t = avg_gain / avg_loss
    rsi_t = 100 - (100 / (1 + rs_t))

    return rsi_t

def rsi_strategy(prices, n, lower_threshold=30, upper_threshold=70):
    """
    RSI Strategy.

    Parameters:
    - prices: A pandas Series of stock prices.
    - n: The number of periods to use for RSI calculation.
    - lower_threshold: The lower threshold for generating long signals.
    - upper_threshold: The upper threshold for generating flat signals.

    Returns:
    - A pandas Series of signals where 1 indicates a long signal, and 0 indicates a flat signal.
    """
    rsi_values = rsi(prices, n)

    rsi_values.iloc[:n] = np.nan  # Set the first n values to NaN since RSI is not defined for those periods

    # Generate signals
    
    results = pd.Series(np.nan, index=prices.index)

    results[rsi_values < lower_threshold] = 1
    results[rsi_values > upper_threshold] = 0
    
    results.ffill(inplace=True)  # Forward fill to maintain the last signal until a new one is generated
    results = results.fillna(0)  # Fill any remaining NaN values with 0 (flat signal)
    
    return results.astype(int)
