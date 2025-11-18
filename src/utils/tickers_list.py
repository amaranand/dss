import yaml

path = "config/tickers/stocks_large.yaml"

with open(path, "r") as f:
    data = yaml.safe_load(f)

for s in data.get("symbols", []):
    ticker = s["ticker"].replace(".NS", "")
    print(ticker)
