# Contents of /oversold-value-zone-strategy/oversold-value-zone-strategy/src/data/loader.py

import pandas as pd
import os

class DataLoader:
    def __init__(self, raw_data_path, processed_data_path):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path

    def load_raw_data(self, filename):
        file_path = os.path.join(self.raw_data_path, filename)
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"Raw data file {filename} not found in {self.raw_data_path}")

    def load_processed_data(self, filename):
        file_path = os.path.join(self.processed_data_path, filename)
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        else:
            raise FileNotFoundError(f"Processed data file {filename} not found in {self.processed_data_path}")

    def save_processed_data(self, df, filename):
        file_path = os.path.join(self.processed_data_path, filename)
        df.to_csv(file_path, index=False)