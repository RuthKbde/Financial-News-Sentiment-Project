

import os
import sys
import pandas as pd

# 🔧 Add src/ to system path for importing custom modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from data_loader import load_stock_data
from indicators import compute_indicators

# ✅ List of tickers to process
TICKERS = ["AAPL", "AMZN", "GOOGL", "META", "MSFT", "NVDA", "TSLA"]

def main():
    input_dir = "data/yfinance_data/yfinance_data"
    output_dir = "data/processed"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for ticker in TICKERS:
        print(f"\n📈 Processing {ticker}...")

        df = load_stock_data(ticker, input_dir)
        if df is None:
            print(f"❌ Skipping {ticker} (file not found)")
            continue

        df_indicators = compute_indicators(df)

        output_path = os.path.join(output_dir, f"{ticker}_indicators.csv")
        df_indicators.to_csv(output_path, index=False)
        print(f"✅ Saved indicators to {output_path}")

if __name__ == "__main__":
    main()