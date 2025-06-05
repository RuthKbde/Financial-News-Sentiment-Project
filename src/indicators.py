

"""
This module computes common technical indicators using TA-Lib.
"""

import talib
import pandas as pd

def compute_indicators(df):
    """
    Takes a DataFrame with OHLCV data and adds technical indicators.

    Parameters:
        df (pd.DataFrame): Stock data with 'Open', 'High', 'Low', 'Close', 'Volume'

    Returns:
        pd.DataFrame: DataFrame with new columns for technical indicators
    """
    df = df.copy()

    # Moving Averages
    df['MA_10'] = talib.SMA(df['Close'], timeperiod=10)
    df['MA_50'] = talib.SMA(df['Close'], timeperiod=50)

    # Relative Strength Index (RSI)
    df['RSI_14'] = talib.RSI(df['Close'], timeperiod=14)

    # Moving Average Convergence Divergence (MACD)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

    return df
def plot_indicators(df, ticker):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.plot(df['Date'], df['MA_10'], label='10-Day MA')
    plt.plot(df['Date'], df['MA_50'], label='50-Day MA')
    plt.title(f"{ticker} - Price and Moving Averages")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
