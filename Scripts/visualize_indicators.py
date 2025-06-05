

"""
This script loads historical stock data, calculates technical indicators,
and visualizes them using matplotlib.
"""

import os
import sys 
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importing modules
from src.data_loader import load_stock_data
from src.indicators import compute_indicators

# Optional: Make plots look nicer
plt.style.use('seaborn-v0_8-darkgrid')

def main():
    # Set ticker and data path
    ticker = "AAPL"
    base_dir = "C:\\Users\\Shib\\Documents\\Financial-News-Sentiment-Project\\data\\yfinance_data\\yfinance_data\\AAPL_historical_data.csv"
    file_path = os.path.join(base_dir, f"{ticker}_historical_data.csv")

    # Load the data
    df = load_stock_data(ticker, data_dir=file_path)

    # Compute technical indicators
    df_indicators = compute_indicators(df)

    # Drop NA values (first few rows will be NaN due to rolling indicators)
    df_indicators.dropna(inplace=True)

    # ----- Plot Moving Averages -----
    plt.figure(figsize=(14, 6))
    plt.plot(df_indicators['Date'], df_indicators['Close'], label='Close Price')
    plt.plot(df_indicators['Date'], df_indicators['MA_10'], label='10-Day MA')
    plt.plot(df_indicators['Date'], df_indicators['MA_50'], label='50-Day MA')
    plt.title(f"{ticker} - Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # ----- Plot RSI -----
    plt.figure(figsize=(14, 4))
    plt.plot(df_indicators['Date'], df_indicators['RSI_14'], color='purple', label='RSI 14')
    plt.axhline(70, color='red', linestyle='--', label='Overbought')
    plt.axhline(30, color='green', linestyle='--', label='Oversold')
    plt.title(f"{ticker} - Relative Strength Index (RSI)")
    plt.xlabel("Date")
    plt.ylabel("RSI Value")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # ----- Plot MACD -----
    plt.figure(figsize=(14, 6))
    plt.plot(df_indicators['Date'], df_indicators['MACD'], label='MACD', color='blue')
    plt.plot(df_indicators['Date'], df_indicators['MACD_signal'], label='Signal Line', color='orange')
    plt.bar(df_indicators['Date'], df_indicators['MACD_hist'], label='Histogram', color='gray')
    plt.title(f"{ticker} - MACD")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()