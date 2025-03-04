# Stock Market Technical Analysis: Apple (AAPL)

This stock market analysis project dives deep into Apple (AAPL) stock, using historical data from 2020 to the present to uncover trends, patterns, and potential trading opportunities. It's a thorough breakdown that combines basic analysis with more advanced technical indicators to give a well-rounded view of the stock's performance. Here's how it all comes together:

## Inspiration and Acknowledgments

This project draws inspiration from Chapter 3 of "Time Series Forecasting in Python" by Marco Peixeiro. The book's comprehensive approach to technical analysis and its practical implementation of trading strategies has been instrumental in shaping this project. While the original concepts are from Peixeiro's work, this project extends and adapts them specifically for Apple stock analysis, incorporating additional features and visualizations.

Key concepts adapted from the book include:
- The implementation of technical indicators (Moving Averages, RSI)
- The approach to volatility analysis
- The framework for generating trading signals
- The methodology for performance evaluation

The project builds upon these foundations while adding custom visualizations and analysis specific to Apple's trading patterns.

### **1. Data Collection**
The project starts by pulling historical stock price and trading volume data for Apple using the `yfinance` library. This data is the backbone of the analysis, covering everything from daily price movements to trading activity over the years.

### **2. Basic Analysis**
From there, the analysis calculates daily returns (the percentage change in price from one day to the next) and tracks changes in trading volume. These metrics give a sense of how the stock has been performing and how much interest it's been generating among traders. To make things clearer, the project also creates visualizations of the stock price and trading volume over time. These charts help spot trends and patterns at a glance.

### **3. Technical Indicators**
The analysis then moves into more advanced territory with technical indicators:
- **Moving Averages**: The 20-day and 50-day moving averages are calculated to smooth out the noise in price data and highlight trends. These averages help identify key support and resistance levels, as well as potential shifts in momentum.
- **Volatility**: The 20-day standard deviation of returns is used to measure how much the stock's price fluctuates. High volatility can signal riskier periods, while low volatility might suggest stability.
- **Relative Strength Index (RSI)**: This momentum indicator helps identify overbought or oversold conditions. When the RSI is above 70, the stock might be overbought (and due for a pullback), and when it's below 30, it could be oversold (and potentially ready to bounce back).

### **4. Trading Signals**
The project uses these indicators to generate trading signals:
- **Moving Average Crossovers**: When the 20-day moving average crosses above the 50-day, it's considered a buy signal. Conversely, when the 20-day crosses below the 50-day, it's a sell signal. This strategy helps catch trends early.
- **RSI Signals**: The RSI is used to spot overbought and oversold conditions. If the RSI goes above 70, it might be time to sell, and if it drops below 30, it could be a good time to buy.

### **5. Performance Metrics**
Finally, the analysis evaluates the effectiveness of these trading strategies:
- **Signal Counts**: It tracks how many buy and sell signals are generated over time, giving a sense of how often these strategies might be used.
- **Sharpe Ratio**: This metric assesses the risk-adjusted return of the trading strategy. It's not just about how much money you could make, but how much risk you're taking to get there.

### **Insights and Patterns**
Looking at the charts and data, a few key patterns stand out:
- **Price Trends**: The stock price and moving averages show clear periods of upward and downward momentum. These trends can help identify potential entry and exit points.
- **Volatility**: The volatility analysis highlights periods of high and low price swings, which can be crucial for managing risk.
- **Momentum**: The RSI helps pinpoint moments when the stock might be overextended in one direction, signaling potential reversals.
- **Trading Signals**: Combining moving average crossovers with RSI signals creates a robust framework for making trading decisions. It's not just about following one indicator but using multiple tools to confirm trends.

### **The Big Picture**
At its core, this project is about using data to make smarter trading decisions. By combining basic analysis with technical indicators, it provides a comprehensive view of Apple's stock performance. The goal isn't just to predict where the stock is headed but to do so in a way that balances potential returns with risk. Whether you're a seasoned trader or just getting started, this kind of analysis can be a valuable tool for navigating the stock market.

In short, it's a practical, data-driven approach to understanding Apple's stock, with plenty of insights to help you make more informed decisions.

## Project Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/apple-stock-market-analysis.git
   cd apple-stock-market-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the analysis script:
```bash
python src/apple_stock_analysis.py
```

The script will:
1. Fetch the latest Apple stock data
2. Perform technical analysis
3. Generate visualizations
4. Calculate performance metrics

### Output Files

- `data/apple_stock_data.csv`: Historical stock data with calculated metrics
- `figures/apple_stock_analysis.png`: Comprehensive technical analysis visualization including:
  - Stock price with moving averages
  - Trading volume
  - Volatility
  - RSI indicator
