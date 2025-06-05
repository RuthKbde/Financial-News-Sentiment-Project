import os
import pandas as pd

# Define tickers and file paths
tickers = ["AAPL", "META", "NVDA", "GOOGL", "AMZN", "MSFT", "TSLA"]
data_dir = "data/processed"
sentiment_path = os.path.join(data_dir, "sentiment_scores.csv")
output_path = "outputs/correlation_results.csv"

# Load sentiment data
sentiment_df = pd.read_csv(sentiment_path, parse_dates=["date"])
sentiment_df["ticker"] = sentiment_df["ticker"].str.upper()

# Container for correlation results
correlation_results = []

# Loop through each ticker
for ticker in tickers:
    stock_file = os.path.join(data_dir, f"{ticker}.csv")
    if not os.path.exists(stock_file):
        print(f"❌ Missing stock file: {stock_file}")
        continue

    try:
        # Load stock data and compute daily return
        stock_df = pd.read_csv(stock_file, parse_dates=["Date"])
        stock_df.sort_values("Date", inplace=True)
        stock_df["daily_return"] = stock_df["Close"].pct_change()

        # Prepare for merge
        stock_df["ticker"] = ticker
        stock_df.rename(columns={"Date": "date"}, inplace=True)

        # Merge with sentiment
        merged_df = pd.merge(sentiment_df, stock_df, on=["date", "ticker"])

        # Drop missing values
        merged_df.dropna(subset=["sentiment_score", "daily_return"], inplace=True)

        # Compute correlation
        corr = merged_df["sentiment_score"].corr(merged_df["daily_return"])
        correlation_results.append({"ticker": ticker, "correlation": corr})
        print(f"✅ Correlation for {ticker}: {corr:.4f}")

    except Exception as e:
        print(f"❌ Error processing {ticker}: {e}")

# Save correlation results
correlation_df = pd.DataFrame(correlation_results)
correlation_df.to_csv(output_path, index=False)
print(f"\n📁 Correlation results saved to {output_path}")
