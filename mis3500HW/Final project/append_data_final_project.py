import requests
import json
import time




#appending data
def append_data(x):
        url = "http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + x + "&outputsize=full&apikey=NG9C9EPVYBMQT0C8"
        ticker_req = requests.get(url)
        time.sleep(12)
        ticker_dict = json.loads(ticker_req.text)
        
        #open in read to get last date
        csv_file = open("/home/ubuntu/environment/Final project/Tickers/" + x + ".csv", "r")
        lines = csv_file.readlines()
        last_date = lines[-1].split(", ")[0]
        
        #get new lines up until the last date
        key1 = "Time Series (Daily)"
        key2 = "4. close"
        new_lines = []
        for date in ticker_dict[key1]:
            if date == last_date:
                break
            new_lines.append(date + ", " + ticker_dict[key1][date][key2] + "\n")
            
        #write new lines into csv file
        new_lines = new_lines[::-1]
        csv_file = open("/home/ubuntu/environment/Final project/Tickers/" + x + ".csv", "a")
        csv_file.writelines(new_lines)
        csv_file.close()
    
   