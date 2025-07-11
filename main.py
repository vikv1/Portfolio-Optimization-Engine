import yfinance as yf

# Download historical data for Apple (AAPL)
ticker = yf.Ticker("AAPL")
hist_data = ticker.history(period="5y")
print(hist_data.head())