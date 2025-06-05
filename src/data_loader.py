# src/data_loader.py

import os
import pandas as pd

def load_stock_data(ticker=None, filepath=None):
    """
    Loads stock data from a specific CSV file.

    Parameters:
        ticker (str): Optional stock ticker for logging.
        filepath (str): Full path to the CSV file.

    Returns:
        pd.DataFrame or None: Loaded DataFrame or None if file doesn't exist.
    """
    if filepath is None:
        print("❌ No file path provided.")
        return None

    if not os.path.exists(filepath):
        print(f"⚠️ File not found for {ticker or 'unknown'}: {filepath}")
        return None

    try:
        df = pd.read_csv(filepath)
        print(f"✅ Loaded data for {ticker or 'unknown'} with columns: {df.columns.tolist()}")
        return df
    except Exception as e:
        print(f"❌ Failed to load file: {filepath}\nError: {e}")
        return None
