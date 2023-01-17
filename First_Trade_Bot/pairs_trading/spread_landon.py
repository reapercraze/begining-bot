import pandas_datareader as web
import pandas as pd
import numpy as np
from datetime import datetime

# Pull data from the web
ticker = 'GOOG'
data = web.DataReader(ticker, 'yahoo', start=datetime(2021,3,2))
print(f"{ticker} simulation")
# print(data.head())

prices = data['Adj Close'].to_numpy()
# Initiliaze variables

best_percent = 0.0
best_return = 0.0
# percent = 0.10

# Simulate moving through time
for percent in np.arange(-1.0, 1.0, 0.01):
    # Reinitialize these for every parameter value
    buy = 0
    tot_profit = 0
    first_buy = None
    
    for i in range(9, prices.shape[0]):
        # Calculate the average
        avg = prices[i-9:i].mean()
        # get current price
        price = prices[i]
        
        # Now comes the trading logic
        if price < avg * (1.0 + percent) and buy == 0: # Do we buy?
            # print(f"buy at {price}")
            buy = price
            if first_buy is None:
                first_buy = buy
        elif price > avg * (1.0 - percent) and buy != 0:    # Do we sell?
            # print(f"sell at {price}")
            # We get money equal to current price for selling
            # and then we subtract what we bought it for
            tot_profit += price - buy
            buy = 0
    
    
    if first_buy is not None:
        if tot_profit/first_buy > best_return:
            best_percent = percent
            best_return = tot_profit/first_buy
# print(f"total profit: {tot_profit}")
# print(f"total return: {tot_profit/first_buy}")
print("best percent:", best_percent)
print("best return:", best_return)