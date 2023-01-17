import numpy as np

file = open("week7/AAPL.txt", "r")
prices = []
line = file.readline()
print(line)

days = 5
buy = 0
profit = 0.0
first_buy = 0 
while line:
    prices.append(float(line))
    line = file.readline()
    print(line)
    
    if len(prices) == 6:
        avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5
        if prices[5] < avg * .95 and buy == 0: #buy
            buy = prices[5]
            if first_buy == 0:
                first_buy = buy
        elif prices[5] > avg * 1.05 and buy != 0: #sell
            profit += (prices[5] - buy)
            buy = 0
        else:
            pass
        
        prices.pop(0) #removing the oldest day

print("profit:", profit)
print("returns:", (profit/first_buy))