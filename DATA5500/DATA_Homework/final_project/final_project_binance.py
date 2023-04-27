from final_project_graph import *

from binance.enums import *
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

#contecting to server
client = Client(api_key, api_secret)
client.API_URL = "https://testnet.binance.vision/api"

#running analysis if disequilibrium is profitable
trans_fee = .001
num_transactions = len(great_path)
cost = trans_fee * num_transactions

print("\nMy paper trading account info----------")
print(client.get_account())
print("\nThe tickers that the paper account can trade-----------")
print(client.get_all_tickers())
print("\n\nMy asset balance of BNB before order-------")
print(client.get_asset_balance(asset="BNB"))

#making an order to binance exchange
try:
    order = client.create_order(
    symbol =  "BNBBTC",
    side = Client.SIDE_BUY,
    type = Client.ORDER_TYPE_MARKET,
    quantity = 5)
        
#outputs what the error is 
except BinanceAPIException as e:
    print(e.message)

print("\nMy asset balance pf BNB after the order-------")
print(client.get_asset_balance(asset="BNB"))
