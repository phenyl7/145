import yfinance as yf

# Define the stock ticker and the time period
ticker = 'QQQ'
period = '1y'  # You can adjust this to get more data (e.g., '5y', '10y', etc.)

# Download historical data for QQQ
data = yf.download(ticker, period=period)

# Calculate the 145-day Simple Moving Average (SMA)
data['145_SMA'] = data['Close'].rolling(window=145).mean()

# Print the most recent SMA value
print("Most recent 145-day SMA:", data['145_SMA'].iloc[-1])

# Optionally, print the full data with the SMA values
# print(data.tail())
