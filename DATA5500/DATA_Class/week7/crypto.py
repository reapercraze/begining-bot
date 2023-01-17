import requests
import json
import time
from datetime import datetime, timedelta

#url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=02-01-2020&localization=false" 

url1 = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date="
url2 = "&localization=false"

key1 = "market_data"
key2 = "current_price"
key3 = "usd"

dt = datetime(2019, 12, 31)
for i in range(100):
    dt += timedelta(days = 1)
    dts = dt.strftime("%d-%m-%Y")

    url = url1 + dts + url2
    print(url)

    req = requests.get(url)
    #print(req.text)
    dct1 = json.loads(req.text)
    print(dct1[key1][key2][key3])
    time.sleep(10)

