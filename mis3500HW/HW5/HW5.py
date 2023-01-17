import json

#Simple Moving Average Strategy Function
def SimpleMovingAverageStrategy(prices):
    i = 0
    buy = 0
    sell = 0 
    first_buy = 0
    tot_profit = 0
    for price in prices:
        if i >= 5: #5 day moving average
            avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            #buy
            if price > (avg)  and buy == 0:
                print("buying at: ", price)
                buy = price
                #first buy
                if first_buy == 0:
                    first_buy = price
            #sell
            elif price < (avg) and buy != 0:
                print("selling at: ", price)
                sell = price
                tot_profit = sell - buy
                print("trade profit: ", sell - buy)
                buy = 0
            #do nothing
            else:
                pass
        i += 1
    returns = tot_profit / first_buy
    print("total profit: ", tot_profit)
    print("returns: ", returns)
    return tot_profit, returns

#Mean Reversion Strategy
def MeanReversionStrategy(prices):
    i = 0
    buy = 0
    sell = 0 
    first_buy = 0
    tot_profit = 0
    for price in prices:
        if i >= 5: #5 day moving average
            avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            #buy
            if price <= (avg * .95)  and buy == 0:
                print("buying at: ", price)
                buy = price
                #First Buy
                if first_buy == 0:
                    first_buy = price
            #sell
            elif price >= (avg * 1.05) and buy != 0:
                print("selling at: ", price)
                sell = price
                tot_profit = sell - buy
                print("trade profit: ", sell - buy)
                buy = 0
            #do nothing
            else:
                pass
        i += 1
    print("total profit: ", tot_profit)
    returns = tot_profit / first_buy
    print("returns: ", returns)
    
    return tot_profit, returns

#Save Results Function
def SaveResults(x):
    json.dump(x, open("results.json", "w"))
    
# loop of all the tickers 
profit_dictionary = {}
prices_dictionary = {}
tickers = ["AAPL", "AMD", "BA", "BRK-A", "GM", "GOOG", "MSTF", "NIO", "TSLA", "WFC"]
for ticker in tickers:
    file = open("/home/ubuntu/environment/HW5/" + ticker + ".txt", "r")
    lines = file.readlines()
    ticker_prices = [float(line) for line in lines]
    profit_dictionary[ticker + "_prices"] = ticker_prices
    #running the strategies
    mr_prof, mr_returns = MeanReversionStrategy(ticker_prices)
    profit_dictionary[ticker + "_mr_profit"] = mr_prof 
    profit_dictionary[ticker + "_mr_returns"] = mr_returns
    sma_prof, sma_returns = SimpleMovingAverageStrategy(ticker_prices)
    profit_dictionary[ticker + "_sma_profit"] = sma_prof 
    profit_dictionary[ticker + "_sma_returns"] = sma_returns
    
SaveResults(profit_dictionary)