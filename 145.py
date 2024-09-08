import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors

# Convert RGB to hex color
background_color = mcolors.to_hex((0/255, 0/255, 0/255))
grid_color = mcolors.to_hex((102/255, 136/255, 204/255))  # Grid, tick labels, and axis color

# Download QQQ data for the past 5 years
qqq = yf.download('QQQ', period='5y')

# Calculate the 145-day Simple Moving Average (SMA)
qqq['145_SMA'] = qqq['Close'].rolling(window=145).mean()

# Get the most recent closing price and 145-day SMA
most_recent_close = qqq['Close'].iloc[-1]
most_recent_sma = qqq['145_SMA'].iloc[-1]

# Determine the action and action color
action = 'BUY' if most_recent_close > most_recent_sma else 'SELL'
action_color = 'green' if action == 'BUY' else 'red'

# Create the plot
plt.figure(figsize=(12,6))

# Set the background color
plt.gca().set_facecolor(background_color)
plt.gcf().patch.set_facecolor(background_color)

# Plot the QQQ closing price with inverted color
plt.plot(qqq.index, qqq['Close'], label='QQQ Close Price', color='orange')

# Plot the 145-day SMA with inverted color
plt.plot(qqq.index, qqq['145_SMA'], label='145-Day SMA', color='blue')

# Customize axis and grid colors
plt.xlabel('Date', color=grid_color)
plt.ylabel('Price (USD)', color=grid_color)

# Place the legend in the bottom right corner with dark gray box
plt.legend(
    loc='lower right', 
    bbox_to_anchor=(1, 0),
    facecolor='dimgray',  # Dark gray background for the legend box
    edgecolor='black'
)

# Customize grid color
plt.grid(True, color=grid_color, linestyle='--', linewidth=0.5)

# Set color for tick labels
plt.gca().tick_params(axis='both', colors=grid_color)

# Add separate boxes for QQQ Close and 145-SMA in the bottom left
plt.gca().text(
    x=0.01, y=0.99,
    s=f'QQQ Close: ${most_recent_close:.2f}',
    fontsize=8,
    color='orange',  # Color for QQQ Close
    ha='left',
    va='top',
    bbox=dict(
        facecolor='dimgray',  # Darker gray box
        edgecolor='black',
        boxstyle='round,pad=0.5'
    ),
    transform=plt.gca().transAxes  # Use axes coordinates for positioning
)

plt.gca().text(
    x=0.01, y=0.92,
    s=f'145-SMA: ${most_recent_sma:.2f}',
    fontsize=8,
    color='blue',  # Color for 145-SMA
    ha='left',
    va='top',
    bbox=dict(
        facecolor='dimgray',  # Darker gray box
        edgecolor='black',
        boxstyle='round,pad=0.5'
    ),
    transform=plt.gca().transAxes  # Use axes coordinates for positioning
)

# Add action label in the top right corner
plt.gca().text(
    x=0.99, y=0.99,
    s=action,
    fontsize=12,
    color=action_color,  # Conditional coloring
    ha='center',
    va='top',
    bbox=dict(
        facecolor='dimgray',  # Darker gray box
        edgecolor='black',
        boxstyle='round,pad=0.5'
    ),
    transform=plt.gca().transAxes  # Use axes coordinates for positioning
)

# Display the plot
plt.show()
