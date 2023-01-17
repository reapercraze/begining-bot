import json

#Bollinger bands strategy
def bollinger_bands(prices):
    i = 0
    buy = 0
    sell = 0 
    first_buy = 0
    tot_profit = 0
    for price in prices:
        if i >= 5: #5 day moving average
            avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            #buy
            if price > (avg * .95)  and buy == 0:
                # print("buying at: ", price)
                buy = price
                #First Buy
                if first_buy == 0:
                    first_buy = price
                if i == len(prices) - 1:
                    print("buy " + ticker + " today for bollinger bands")
            #sell
            elif price < (avg * 1.05) and buy != 0:
                # print("selling at: ", price)
                sell = price
                tot_profit = sell - buy
                if i == len(prices) - 1:
                    print("sell " + ticker + " today for bollinger bands")
                # print("trade profit: ", sell - buy)
                buy = 0
            #do nothing
            else:
                pass
        i += 1
    # print("total profit: ", tot_profit)
    try:
        returns = tot_profit / first_buy
    except:
        returns = 0
    # print("returns: ", returns)
    
    return tot_profit, returns
