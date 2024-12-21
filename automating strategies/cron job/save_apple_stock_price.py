import yfinance as yf
import pandas as pd
import os
from datetime import datetime

def fetch_data(ticker, file_path):
    # Fetch new data
    data = yf.Ticker(ticker).history(period="1d", interval="1m")
    data.reset_index(inplace=True)  # Reset index to prepare for appending
    data["Ticker"] = ticker  # Add a column for the ticker symbol

    # Check if the file exists
    if os.path.exists(file_path):
        # Load existing data
        existing_data = pd.read_csv(file_path)

        # Combine and remove duplicates
        combined_data = pd.concat([existing_data, data], ignore_index=True)
        combined_data.drop_duplicates(subset=["Datetime", "Ticker"], inplace=True)

        # Save updated data
        combined_data.to_csv(file_path, index=False)
        print(f"Updated data for {ticker} saved to {file_path}")
    else:
        # Save new data
        data.to_csv(file_path, index=False)
        print(f"Data for {ticker} saved to {file_path}")

# Example usage
fetch_data("AAPL", "/path/to/stock_data.csv")
