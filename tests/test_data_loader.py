import unittest
from src.data.loader import DataLoader

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.loader = DataLoader()

    def test_load_raw_data(self):
        data = self.loader.load_raw_data('path/to/raw/data')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_load_processed_data(self):
        data = self.loader.load_processed_data('path/to/processed/data')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_invalid_data_path(self):
        with self.assertRaises(FileNotFoundError):
            self.loader.load_raw_data('invalid/path')

if __name__ == '__main__':
    unittest.main()