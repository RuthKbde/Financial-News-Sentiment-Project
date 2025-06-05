# Scripts/New_visualize_indicators.py

import os
import sys
import matplotlib.pyplot as plt

# Add project root to sys.path for local imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_loader import load_stock_data

def plot_indicators(df, stock):
    plt.figure(figsize=(14, 8))

    plt.subplot(3, 1, 1)
    plt.plot(df['Date'], df['Close'], label='Close', color='black')
    plt.plot(df['Date'], df['MA_10'], label='MA 10', linestyle='--')
    plt.plot(df['Date'], df['MA_50'], label='MA 50', linestyle='--')
    plt.title(f"{stock} Price with Moving Averages")
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(df['Date'], df['RSI_14'], label='RSI (14)', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title(f"{stock} RSI")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(df['Date'], df['MACD'], label='MACD', color='blue')
    plt.plot(df['Date'], df['MACD_signal'], label='Signal', color='orange')
    plt.title(f"{stock} MACD & Signal")
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():
    stock = "TSLA"  # Example stock, can be parameterized
    filepath = os.path.join("data", "processed", f"{stock}_indicators.csv")
    df = load_stock_data(ticker=stock, filepath=filepath)

    if df is not None and not df.empty:
        df['Date'] = pd.to_datetime(df['Date'])  # ensure date is datetime
        plot_indicators(df, stock)
    else:
        print(f"❌ No data loaded for {stock}")

if __name__ == "__main__":
    import pandas as pd
    main()
