import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import sys
import os

def fetch_apple_stock_data():
    """Fetch Apple stock data from Yahoo Finance."""
    try:
        # Download data directly
        df = yf.download('AAPL', period='5y', interval='1d', progress=False)
        if df.empty:
            print("Error: No data found for Apple stock")
            sys.exit(1)
        return df
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        sys.exit(1)

def calculate_rsi(data, periods=14):
    """Calculate Relative Strength Index."""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_volatility(data, window=20):
    """Calculate rolling volatility."""
    return data['Daily_Return'].rolling(window=window).std() * np.sqrt(252)

def analyze_stock_data(df):
    """Perform comprehensive technical analysis."""
    try:
        # Basic metrics
        df['Daily_Return'] = df['Close'].pct_change()
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        
        # Volume analysis
        df['Volume_MA20'] = df['Volume'].rolling(window=20).mean()
        df['Volume_Change'] = df['Volume'].pct_change()
        
        # RSI
        df['RSI'] = calculate_rsi(df)
        
        # Volatility
        df['Volatility_20d'] = calculate_volatility(df)
        
        # Trading signals
        df['Signal'] = 0  # Initialize signals
        
        # Simple MA Crossover signals
        df.loc[df['MA20'] > df['MA50'], 'Signal'] = 1
        df.loc[df['MA20'] <= df['MA50'], 'Signal'] = -1
        
        return df
    except Exception as e:
        print(f"Error analyzing data: {str(e)}")
        sys.exit(1)

def plot_stock_price_with_signals(df, save_path='figures/apple_stock_analysis.png'):
    """Create a comprehensive plot with price, MAs, technical indicators, and volume."""
    try:
        # Create figure with subplots
        fig = plt.figure(figsize=(15, 16))
        gs = fig.add_gridspec(4, 1, height_ratios=[2, 1, 1, 1])
        
        # Plot 1: Price and MAs
        ax1 = fig.add_subplot(gs[0])
        ax1.plot(df.index, df['Close'], label='Close Price', alpha=0.8)
        ax1.plot(df.index, df['MA20'], label='20-day MA', alpha=0.7)
        ax1.plot(df.index, df['MA50'], label='50-day MA', alpha=0.7)
        ax1.set_title('Stock Price Over Time')
        ax1.set_ylabel('Price (USD)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Trading Volume
        ax2 = fig.add_subplot(gs[1])
        ax2.plot(df.index, df['Volume'], color='blue', alpha=0.8)
        ax2.set_title('Trading Volume Over Time')
        ax2.set_ylabel('Volume')
        ax2.grid(True, alpha=0.3)
        
        # Plot 3: 20-day Volatility
        ax3 = fig.add_subplot(gs[2])
        ax3.plot(df.index, df['Volatility_20d'], color='purple', alpha=0.8)
        ax3.set_title('20-day Volatility')
        ax3.set_ylabel('Volatility')
        ax3.grid(True, alpha=0.3)
        
        # Plot 4: RSI
        ax4 = fig.add_subplot(gs[3])
        ax4.plot(df.index, df['RSI'], color='blue', alpha=0.8)
        ax4.axhline(y=70, color='r', linestyle='--', alpha=0.5)  # Overbought line
        ax4.axhline(y=30, color='g', linestyle='--', alpha=0.5)  # Oversold line
        ax4.set_title('RSI (Relative Strength Index)')
        ax4.set_ylabel('RSI')
        ax4.set_xlabel('Date')
        ax4.grid(True, alpha=0.3)
        
        # Format and save
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        
    except Exception as e:
        print(f"Error creating analysis plot: {str(e)}")
        sys.exit(1)

def calculate_performance_metrics(df):
    """Calculate and return performance metrics."""
    try:
        total_return = ((df['Close'].iloc[-1] / df['Close'].iloc[0]) - 1) * 100
        annual_volatility = df['Daily_Return'].std() * np.sqrt(252) * 100
        avg_daily_return = df['Daily_Return'].mean()
        daily_std = df['Daily_Return'].std()
        sharpe_ratio = (avg_daily_return / daily_std) * np.sqrt(252) if daily_std != 0 else 0
        rolling_max = df['Close'].expanding(min_periods=1).max()
        daily_drawdown = df['Close'] / rolling_max - 1
        max_drawdown = daily_drawdown.min() * 100
        
        metrics = {
            'Total_Return': float(total_return),
            'Annual_Volatility': float(annual_volatility),
            'Sharpe_Ratio': float(sharpe_ratio),
            'Max_Drawdown': float(max_drawdown)
        }
        return metrics
    except Exception as e:
        print(f"Error calculating performance metrics: {str(e)}")
        sys.exit(1)

def main():
    print("Performing comprehensive technical analysis on Apple stock...")
    
    # Create directories if they don't exist
    for directory in ['data', 'figures']:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Fetch and analyze data
    df = fetch_apple_stock_data()
    df = analyze_stock_data(df)
    
    # Calculate performance metrics
    metrics = calculate_performance_metrics(df)
    
    # Save data
    df.to_csv('data/apple_stock_data.csv')
    
    # Create visualization
    plot_stock_price_with_signals(df)
    
    # Print results
    print("\nAnalysis complete! Results:")
    print(f"Total Return: {metrics['Total_Return']:.2f}%")
    print(f"Annual Volatility: {metrics['Annual_Volatility']:.2f}%")
    print(f"Sharpe Ratio: {metrics['Sharpe_Ratio']:.2f}")
    print(f"Maximum Drawdown: {metrics['Max_Drawdown']:.2f}%")
    
    print("\nFiles generated:")
    print("- data/apple_stock_data.csv")
    print("- figures/apple_stock_analysis.png")

if __name__ == "__main__":
    main() 