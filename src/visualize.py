import os
from src.data_loader import load_stock_data
from src.indicators import compute_indicators
import matplotlib.pyplot as plt

def visualize_indicators(stock, file_path):
    df = load_stock_data(file_path)
    if df is None:
        print(f"❌ No data loaded for {stock}")
        return
    df = compute_indicators(df)
    df.plot(y=["Close", "MA_10", "MA_50"])
    plt.title(f"{stock} Technical Indicators")
    plt.savefig(f"outputs/{stock}_indicators.png")
    plt.close()

def main():
    tickers = ["AAPL", "META", "NVDA","GOOGL", "AMZN", "MSFT", "TSLA"]
    data_dir = r"data/processed"  # ✅ This is correct relative to your project folder

    for stock in tickers:
        file_path = os.path.join(data_dir, f"{stock}.csv")
        if not os.path.exists(file_path):
            print(f"❌ File not found for {stock}: {file_path}")
            continue
        try:
            visualize_indicators(stock, file_path)
            print(f"✅ Plotted for {stock}")
        except Exception as e:
            print(f"❌ Error processing {stock}: {e}")

if __name__ == "__main__":
    main()
