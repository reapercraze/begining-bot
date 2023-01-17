import json
import time
import requests

ticker = 'AAPL'
url = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&outputsize=full&apikey=NG9C9EPVYBMQT0C8'
req = requests.get(url)
time.sleep(12)

req_dict = json.loads(req.text)


key1 = "Time Series (Daily)" # dictionary with all prices by date
key2 = '4. close'

#get last date
csv_file = open(ticker + ".csv", "r")
lines = csv_file.readlines()
last_date = lines[-1].split(",")[0]

new_lines = []
for date in req_dict[key1]:
    if date == last_date:
        break
    new_lines.append(date + "," + req_dict[key1][date][key2]+"\n")

new_lines = new_lines[::-1]
csv_file = open(ticker + ".csv", "a")
csv_file.writelines(new_lines)
csv_file.close()