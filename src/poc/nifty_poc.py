import os
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta


DATA_PATH = "data/raw/nifty_50_eod.csv"
SYMBOL = "^NSEI"    # yfinance symbol for Nifty 50 index
LOOKBACK_DAYS = 200
DOWNLOAD_YEARS = 2


def ensure_data():
    """
    If data file does NOT exist:
        → Download last 2 years and save.
    If exists:
        → Load and use it.
    """

    if os.path.exists(DATA_PATH):
        print("✔ Local data found. Using existing file.")

    else:
        print("⏳ No local file found — downloading 2 years of data...")

        end = datetime.today()
        start = end - timedelta(days=365 * DOWNLOAD_YEARS)

        df = yf.download(SYMBOL, start=start, end=end)

        if df.empty:
            raise Exception("❌ Failed to download data — possibly market holiday or data not ready.")

        df.reset_index(inplace=True)
        df.to_csv(DATA_PATH, index=False)

        print(f"✔ Download complete. Saved to {DATA_PATH}")

    df = pd.read_csv(DATA_PATH, parse_dates=['Date'],skiprows=[1])
    df = df.sort_values("Date")
    return df

def compute_rsi(series, period=14):
    """Standard RSI"""
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi


def compute_weekly_rsi(df):
    """Weekly RSI using weekly candles."""
    weekly = df.resample('W-MON', on='Date').agg({'Close': 'last'})
    weekly['RSI_W'] = compute_rsi(weekly['Close'])
    return weekly['RSI_W']


def compute_monthly_rsi(df):
    """Monthly RSI using monthly candles."""
    monthly = df.resample('M', on='Date').agg({'Close': 'last'})
    monthly['RSI_M'] = compute_rsi(monthly['Close'])
    return monthly['RSI_M']


def run_poc():
    df = ensure_data()

    # Daily indicators
    df['RSI'] = compute_rsi(df['Close'])
    df['SMA_200'] = df['Close'].rolling(200).mean()

    # Higher timeframe indicators
    weekly_rsi = compute_weekly_rsi(df)
    print(weekly_rsi)
    monthly_rsi = compute_monthly_rsi(df)
    print(monthly_rsi)
    
    # Merge Weekly & Monthly RSI back into daily df
    df = df.merge(weekly_rsi, left_on='Date', right_index=True, how='left')
    df = df.merge(monthly_rsi, left_on='Date', right_index=True, how='left')

    print("\n✔ Indicators computed successfully.\n")
    print(df)
    print(df.tail(10))
    return df


if __name__ == "__main__":
    run_poc()
