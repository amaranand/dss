#!/bin/bash

# This script is used to run backtests on the oversold value zone strategy.

# Activate the virtual environment if needed
# source /path/to/your/venv/bin/activate

# Set the path to the Python executable
PYTHON_EXEC="python"

# Set the path to the backtest script
BACKTEST_SCRIPT="../scripts/backtest.py"

# Run the backtest
$PYTHON_EXEC $BACKTEST_SCRIPT

# Optionally, you can add logging or output redirection here
# For example:
# $PYTHON_EXEC $BACKTEST_SCRIPT >> backtest_output.log 2>&1