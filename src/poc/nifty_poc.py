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


# --------------------------------------------------------
# WEEKLY RSI (with partial week candle)
# --------------------------------------------------------
def compute_weekly_rsi(df):
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')

    # historical full weekly candles (Mon–Fri)
    weekly_full = df.resample('W-MON').agg({'Close': 'last'})

    # partial week candle — current week data only
    current_week_start = df.index.max() - pd.to_timedelta(df.index.max().weekday(), unit='D')
    partial_week_df = df[df.index >= current_week_start]

    partial_week_close = partial_week_df['Close'].iloc[-1]
    partial_week_date = df.index.max()

    # append partial week
    weekly_combined = weekly_full.copy()
    weekly_combined.loc[partial_week_date] = partial_week_close

    weekly_combined['RSI_W'] = compute_rsi(weekly_combined['Close'])
    return weekly_combined['RSI_W']


# --------------------------------------------------------
# MONTHLY RSI (with partial month candle)
# --------------------------------------------------------
def compute_monthly_rsi(df):
    df = df.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')

    # historical full month candles
    monthly_full = df.resample('M').agg({'Close': 'last'})

    # partial month candle — current month
    current_month_start = df.index.max().replace(day=1)
    partial_month_df = df[df.index >= current_month_start]

    partial_month_close = partial_month_df['Close'].iloc[-1]
    partial_month_date   = df.index.max()

    # append partial month
    monthly_combined = monthly_full.copy()
    monthly_combined.loc[partial_month_date] = partial_month_close

    monthly_combined['RSI_M'] = compute_rsi(monthly_combined['Close'])
    return monthly_combined['RSI_M']

def generate_signals(df):
    """
    Generate entry signals for the latest day only (POC version).
    """

    latest = df.iloc[-1]

    rsi = latest['RSI']
    price = latest['Close']
    dma200 = latest['SMA_200']
    weekly_rsi = latest['RSI_W']
    monthly_rsi = latest['RSI_M']

    # % distance from 200 DMA using absolute difference
    dma_diff_pct = abs(price - dma200) / dma200 * 100

    signal = None
    stage = None

    # --- Base Stages (1–3) ---
    if rsi <= 40 and dma_diff_pct <= 5:
        signal = "Stage 1 Trigger"
        stage = 1

    if rsi <= 35 and dma_diff_pct <= 3:
        signal = "Stage 2 Trigger"
        stage = 2

    if rsi <= 30 and dma_diff_pct <= 1:
        signal = "Stage 3 Trigger"
        stage = 3

    # --- Extended Stages (Weekly + Monthly RSI) ---
    if weekly_rsi <= 40 and monthly_rsi <= 50:
        signal = "Stage 4 Trigger (Extended Opportunity)"
        stage = 4

    if weekly_rsi <= 35 and monthly_rsi <= 45:
        signal = "Stage 5 Trigger (Super Extended)"
        stage = 5

    if signal is None:
        print("No signals today.")

    return {
        "date": str(latest['Date']),
        "close": float(price),
        "RSI": float(rsi),
        "RSI_W": float(weekly_rsi),
        "RSI_M": float(monthly_rsi),
        "DMA200": float(dma200),
        "DMA_Diff_pct": float(dma_diff_pct),
        "signal": signal,
        "stage": stage
    }



def run_poc():
    df = ensure_data()

    # Daily indicators
    df['RSI'] = compute_rsi(df['Close'])
    df['SMA_200'] = df['Close'].rolling(200).mean()

    # Higher timeframe indicators
    weekly_rsi = compute_weekly_rsi(df)
    monthly_rsi = compute_monthly_rsi(df)

    # Merge Weekly & Monthly RSI back into daily df
    df = df.merge(weekly_rsi, left_on='Date', right_index=True, how='left')
    df = df.merge(monthly_rsi, left_on='Date', right_index=True, how='left')

    print("\n✔ Indicators computed successfully.\n")
    print(df.tail(10))

    signals = generate_signals(df)

    print("\n=== SIGNALS FOR LATEST DAY ===")
    if not signals:
        print("No signals today.")
    else:
        for k, v in signals.items():
            print(f"- {k}: {v}")

    return df

if __name__ == "__main__":
    run_poc()
