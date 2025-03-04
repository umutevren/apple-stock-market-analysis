import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def fetch_apple_stock_data(start_date, end_date):
    """Fetch Apple stock data from Yahoo Finance."""
    aapl = yf.Ticker("AAPL")
    df = aapl.history(start=start_date, end=end_date)
    return df

def analyze_stock_data(df):
    """Perform basic analysis on the stock data."""
    # Calculate daily returns
    df['Daily_Return'] = df['Close'].pct_change()
    
    # Calculate moving averages
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA50'] = df['Close'].rolling(window=50).mean()
    
    return df

def plot_stock_price(df, save_path='figures/apple_stock_price.png'):
    """Plot stock price with moving averages."""
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.plot(df.index, df['MA20'], label='20 Day MA')
    plt.plot(df.index, df['MA50'], label='50 Day MA')
    plt.title('Apple Stock Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.savefig(save_path)
    plt.close()

def plot_returns_distribution(df, save_path='figures/returns_distribution.png'):
    """Plot the distribution of daily returns."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Daily_Return'].dropna(), kde=True)
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Returns')
    plt.ylabel('Frequency')
    plt.savefig(save_path)
    plt.close()

def main():
    # Set date range for analysis (last 2 years)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=2*365)
    
    # Fetch and analyze data
    df = fetch_apple_stock_data(start_date, end_date)
    df = analyze_stock_data(df)
    
    # Save data
    df.to_csv('data/apple_stock_data.csv')
    
    # Create visualizations
    plot_stock_price(df)
    plot_returns_distribution(df)
    
    print("Analysis complete! Check the data and figures directories for results.")

if __name__ == "__main__":
    main() 