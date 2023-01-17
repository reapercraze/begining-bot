#Used with BA ticker

file = open("/home/ubuntu/environment/HW4/BA.txt", "r")
lines = file.readlines()

prices = [float(line) for line in lines]

def MeanReversionStrategy(prices):
    i = 0
    buy = 0
    sell = 0 
    first_buy = 0
    tot_profit = 0
    for price in prices:
        if i >= 5: 
            avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            #buy
            if price <= (avg * .95)  and buy == 0:
                print("buying at: ", price)
                buy = price
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
    print("ROI: ", returns)
    
    return tot_profit, returns
    
prof, returns = MeanReversionStrategy(prices)

profit_dictionary = {}
profit_dictionary["profit"] = prof
profit_dictionary["returns"] = returns
print(profit_dictionary)