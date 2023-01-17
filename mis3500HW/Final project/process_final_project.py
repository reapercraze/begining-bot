import requests
import json
import time


key1 = "Time Series (Daily)"
key2 = "4. close"


def create_file(x):
    url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + x + "&outputsize=full&apikey=NG9C9EPVYBMQT0C8"
    ticker_req = requests.get(url)
    time.sleep(12)
    ticker_dict = json.loads(ticker_req.text)
    csv_file = open("/home/ubuntu/environment/Final project/Tickers/" + x + ".csv", "w") 
    csv_file.writelines("Date, " + x + " price\n")
    write_lines = []
    for date in ticker_dict[key1]:
        write_lines.append(date + ", " + ticker_dict[key1][date][key2] + "\n")
    write_lines = write_lines[::-1]
    csv_file.writelines(write_lines)
    csv_file.close()
    

tickers = ["AAPL", "AMD", "BA", "BRK-A", "GM", "GOOG", "MSFT", "NIO", "TSLA", "WFC"]

for ticker in tickers:
    create_file(ticker)