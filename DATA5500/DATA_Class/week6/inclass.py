import json
import requests

key1 = "Time Series (Daily)"
key3 = "4. close"

url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=NG9C9EPVYBMQT0C8"
request = requests.get(url)
dct = json.loads(request.text)

price = []

for date in dct[key1]:
    price.append(float(dct[key1][date][key3]))


print(price[0])