import pandas_datareader as web
import pandas as pd 
from datetime import datetime

#pull data
data = web.DataReader("TSLA", "yahoo", start=datetime(2021,3,2))
print(data.head())

prices = data["Adj Close"].to_numpy()

#initillaze variables
buy = 0
tot_profit = 0
first_buy = 0
best_return = 0.0
best_percent = 0.0


#sim moving through time
for i in range(9, prices.shape[0]):
    #calculate the average
    avg = prices[i-9:i].mean()
    #get current price
    price = prices[i]
    
    #trade logic
    if price < avg and buy == 0:
        buy = price
        print(f"buy at {price}")
        if first_buy == 0:
            first_buy = price
    
    elif price > avg and buy != 0:
        print(f"sell at {price}")
        tot_profit += price - buy
        buy = 0 

print(f"total profit: {tot_profit}")