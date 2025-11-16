import yfinance as yf
import pandas as pd
import os

# Choose your save directory
SAVE_DIR = "data/raw/indices_sectorial_eod"

# Create directory if it doesn't exist
os.makedirs(SAVE_DIR, exist_ok=True)

# Yahoo Finance tickers you confirmed earlier
tickers = [
    '^CNXAUTO', '^NSEBANK', '^CEX', 'NIFTY_FIN_SERVICE.NS', '^CNXFIN',
    'FINIETF.NS', '^CNXFMCG', 'NIFTY_HEALTHCARE.NS', '^CNXIT', '^CNXMEDIA',
    '^CNXMETAL', '^CNXPHARMA', 'NIFTYPVTBANK.NS', '^CNXPSUBANK', '^CNXREALTY',
    'NIFTY_CONSR_DURBL.NS', 'NIFTY_OIL_AND_GAS.NS'
]

# Download 1 year of daily EOD data
df = yf.download(
    tickers,
    period='1y',
    interval='1d',
    group_by='ticker',
    threads=True
)

# Save each ticker as its own CSV inside SAVE_DIR
for t in tickers:
    try:
        sub = df[t].dropna()
        if not sub.empty:
            filename = t.replace("^", "").replace(".", "_") + "_eod.csv"
            filepath = os.path.join(SAVE_DIR, filename)
            sub.to_csv(filepath)
            print(f"Saved: {filepath}")
    except Exception as e:
        print(f"Could not save {t}: {e}")

print("All available tickers processed.")
