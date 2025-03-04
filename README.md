# Apple Stock Market Analysis

This project analyzes Apple (AAPL) stock market data using Python. It fetches historical data from Yahoo Finance, performs basic analysis, and generates visualizations.

## Features

- Fetches real-time Apple stock data from Yahoo Finance
- Calculates daily returns and moving averages
- Generates visualizations:
  - Stock price chart with 20-day and 50-day moving averages
  - Distribution of daily returns

## Directory Structure

```
.
├── data/                   # Contains stock market data
├── figures/                # Contains generated plots
├── src/                    # Source code
│   └── apple_stock_analysis.py
└── requirements.txt        # Python dependencies
```

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the analysis script:
```bash
python src/apple_stock_analysis.py
```

The script will:
1. Fetch the last 2 years of Apple stock data
2. Perform basic analysis
3. Generate visualizations in the `figures` directory
4. Save the data in the `data` directory

## Generated Files

- `data/apple_stock_data.csv`: Historical stock data with calculated metrics
- `figures/apple_stock_price.png`: Stock price chart with moving averages
- `figures/returns_distribution.png`: Distribution of daily returns
