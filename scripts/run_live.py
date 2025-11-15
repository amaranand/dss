# Contents of /oversold-value-zone-strategy/oversold-value-zone-strategy/scripts/run_live.py

import sys
import logging
from src.main import run_strategy

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the live trading strategy...")

    try:
        run_strategy()
    except Exception as e:
        logging.error("An error occurred while running the strategy: %s", e)
        sys.exit(1)

if __name__ == "__main__":
    main()