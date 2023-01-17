import json
import append_data_final_project

#Simple Moving Average Strategy Function
def simple_moving_average_strategy(prices):
    i = 0
    buy = 0
    sell = 0 
    first_buy = 0
    tot_profit = 0
    for price in prices:
        if i >= 5: #5 day moving average
            avg = ((prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5)
            #buy
            if price > (avg)  and buy == 0:
                # print("buying at: ", price)
                buy = price
                #first buy
                if first_buy == 0:
                    first_buy = price
                if i == len(prices) - 1:
                    print("buy " + ticker + " today for simple moving average")
            #sell
            elif price < (avg) and buy != 0:
                # print("selling at: ", price)
                sell = price
                tot_profit = sell - buy
                if i == len(prices) - 1:
                    print("sell " + ticker + "today for simple moving average")
                # print("trade profit: ", sell - buy)
                buy = 0
            #do nothing
            else:
                pass
        i += 1
    try:
        returns = tot_profit / first_buy
    except:
        returns = 0
    # print("total profit: ", tot_profit)
    # print("returns: ", returns)
    return tot_profit, returns


#Save Results Function
def save_results(x):
    json.dump(x, open("/home/ubuntu/environment/Final project/final_project_results.json", "w"))

profit_dictionary = {}
high_returns = 0
high_returns_ticker = ""
high_returns_strategy = ""
tickers = ["AAPL", "AMD", "BA", "BRK-A", "GM", "GOOG", "MSFT", "NIO", "TSLA", "WFC"]
for ticker in tickers:
    # append_data_final_project.append_data(ticker)
    file = open("/home/ubuntu/environment/Final project/Tickers/" + ticker + ".csv")
    lines = file.readlines()[1:]
    prices = [float(line.split(",")[1]) for line in lines]
    
    #check if sma stategy is the highest for the ticker and add data to dictionary
    sma_profit, sma_returns = simple_moving_average_strategy(prices)
    profit_dictionary[ticker + "_sma_profit"] = sma_profit
    profit_dictionary[ticker + "_sma_returns"] = sma_returns
    
    if sma_returns > high_returns:
        high_returns = sma_returns
        high_returns_ticker = ticker
        high_returns_strategy = "simple moving average"
    
    #check if mr stategy is the highest for the ticker and add data to dictionary
    mr_profit, mr_returns = mean_reversion_strategy(prices)
    profit_dictionary[ticker + "_mr_profit"] = mr_profit 
    profit_dictionary[ticker + "_mr_returns"] = mr_returns
    
    if mr_returns > high_returns:
        high_returns = mr_returns
        high_returns_ticker = ticker
        high_returns_strategy = "mean reversion"
        
    #check if bb is the highest for the ticker and add data to dictionary
    bb_profit, bb_returns = bollinger_bands(prices)
    profit_dictionary[ticker + "_bb_profit"] = bb_profit
    profit_dictionary[ticker + "_bb_returns"] = bb_returns
    
    if bb_returns > high_returns:
        high_returns = bb_returns
        high_returns_ticker = ticker
        high_returns_strategy = "bollinger_bands"

#add best results to dictionary
print("Highest ticker return is: " + high_returns_ticker)
print("With the strategy: " + high_returns_strategy)
profit_dictionary["highest ticker return"] = high_returns_ticker
profit_dictionary["highest ticker return strategy"] = high_returns_strategy

#save it to a json
save_results(profit_dictionary)