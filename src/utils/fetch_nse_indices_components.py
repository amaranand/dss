import io
import yaml
import requests
import pandas as pd
from pathlib import Path

# Folder to store output CSV files
OUTPUT_DIR = Path("data/raw/nse_indices_components")
OUTPUT_DIR.mkdir(exist_ok=True)

CONFIG_FILE = "config/indices/nse_broader_indices.yaml"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def download_csv(url):
    """Download CSV from NSE and return as pandas DataFrame."""
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text))

def main():
    # Read YAML config
    with open(CONFIG_FILE, "r") as f:
        config = yaml.safe_load(f)

    # Loop over NSE indices
    for item in config["indices"]:
        name = item["name"]
        symbol = item["symbol"]
        url = item["csv_url"]

        print(f"Fetching: {name} ...")

        df = download_csv(url)

        output_path = OUTPUT_DIR / f"{symbol}.csv"
        df.to_csv(output_path, index=False)

        print(f"Saved → {output_path}")


if __name__ == "__main__":
    main()
