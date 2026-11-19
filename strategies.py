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

