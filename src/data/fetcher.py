import os
import yaml
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

CONFIG_DIR = "config/tickers"
DATA_DIR   = "data/raw"

DOWNLOAD_YEARS = 2     # for POC fetch full history
MIN_ROWS = 50          # sanity check


# ----------------------------------------------------------
# 1. Load ALL yaml files under config/tickers/
# ----------------------------------------------------------
def load_all_tickers():
    tickers = []

    for file in os.listdir(CONFIG_DIR):
        if file.endswith(".yaml"):
            path = os.path.join(CONFIG_DIR, file)

            with open(path, "r") as f:
                data = yaml.safe_load(f)

            if data and "symbols" in data:
                for s in data["symbols"]:
                    tickers.append({
                        "name":   s["name"],
                        "ticker": s["ticker"],
                        "type":   s.get("type", "unknown"),
                        "source_file": file
                    })

    return tickers


# ----------------------------------------------------------
# 2. Fetch data for a SINGLE ticker
# ----------------------------------------------------------
def fetch_ticker_data(ticker, years=DOWNLOAD_YEARS):
    safe_name = ticker.replace("^", "").replace("=", "")
    file_path = os.path.join(DATA_DIR, f"{safe_name}.csv")

    # ---- always download full data in POC ----
    end = datetime.today()
    start = end - timedelta(days=365 * years)

    print(f"\n⏳ Downloading {ticker} (last {years} years)...")

    df = yf.download(ticker, start=start, end=end, 
                      auto_adjust=True,   # explicitly choose adjusted prices
                      progress=False)

    if df.empty:
        print(f"❌ No data fetched for {ticker}. Possibly holiday or source issue.")
        return None

    df.reset_index(inplace=True)
    df.to_csv(file_path, index=False)

    print(f"✔ Saved: {file_path} ({len(df)} rows)")
    return df


# ----------------------------------------------------------
# 3. Fetch data for ALL tickers listed in YAML config
# ----------------------------------------------------------
def fetch_all_configured():
    tickers = load_all_tickers()

    if not tickers:
        print("❌ No tickers loaded from config folder.")
        return

    print(f"\n=== TOTAL SYMBOLS FOUND: {len(tickers)} ===")

    os.makedirs(DATA_DIR, exist_ok=True)

    success = []
    failed = []

    for item in tickers:
        if not item["ticker"]:     # skips None, "", null, missing
            continue

        df = fetch_ticker_data(item["ticker"])

        if df is None or len(df) < MIN_ROWS:
            failed.append(item)
        else:
            success.append(item)

    # Summary
    print("\n==================== SUMMARY ====================")
    print(f"✔ Successful downloads : {len(success)}")
    print(f"❌ Failed downloads     : {len(failed)}")

    if failed:
        print("\nFailed tickers:")
        for x in failed:
            print(f"- {x['name']} ({x['ticker']}) from {x['source_file']}")

    print("=================================================\n")

    return success, failed


# ----------------------------------------------------------
# Execute as script
# ----------------------------------------------------------
if __name__ == "__main__":
    fetch_all_configured()
