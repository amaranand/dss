# backtest.py

import pandas as pd
from src.strategy.oversold_value_zone import OversoldValueZone
from src.data.loader import DataLoader

def run_backtest(start_date, end_date, symbol):
    # Load historical data
    data_loader = DataLoader()
    historical_data = data_loader.load_data(symbol, start_date, end_date)

    # Initialize the strategy
    strategy = OversoldValueZone()

    # Run the backtest
    results = strategy.backtest(historical_data)

    # Output results
    print("Backtest Results:")
    print(results)

if __name__ == "__main__":
    # Example parameters for the backtest
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    symbol = "AAPL"

    run_backtest(start_date, end_date, symbol)