import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations
from itertools import combinations
import networkx as nx
from networkx.classes.function import path_weight
import matplotlib.pyplot as plt


coin_names = ["ripple", "cardano", "bitcoin-cash", "eos", "litecoin", "ethereum", "bitcoin"]
tickers = ["xrp", "ada", "bch", "eos", "ltc", "eth", "btc"]
coins = {"ripple":"xrp", "bitcoin-cash":"bch", "eos":"eos", "litecoin":"ltc", "ethereum":"eth", "bitcoin":"btc"}

g = nx.DiGraph()
edges = []


url1 = "https://api.coingecko.com/api/v3/simple/price?ids="
url2 = "&vs_currencies="
for c1, c2 in permutations(coin_names, 2):
    for coin in coins
    url = url1 + c1 + "," + c2 + url2 + coins[c1] + "," + coins[c2]
    print(url)
    dct1 = json.loads(requests.get(url).text)
    #time.sleep(1)
    
    try:
        edges.append((c1, c2, dct1[c1][coins[c2]]))
        
    except:
        continue

g.add_weighted_edges_from(edges) 


greatest_weight = -99999999
greatest_path = []
lowest_weight = 99999999
lowest_path = []
for n1, n2 in combinations(g.nodes,2):
    print("paths from ", n1, "to", n2)
    for path in nx.all_simple_paths(g, source = n1, target = n2):
        print(path)
        
        #path to node 2
        path_weight_to = 1
        for i in range(len(path)-1):
            print("edge from", path[i], "to", path[i+1], ": ", g[path[i]][path[i+1]]["weight"])
            path_weight_to *= g[path[i]][path[i+1]]["weight"]
        
        back_path = path[::-1]
        print(back_path)
        
        path
        print(path)
        #path from node 2 to node 1
        try:
            path_weight_from = 1
            for i in range(len(path)-1):
                print("edge from", path[i], "to", path[i+1], ":", g[path[i]][path[i+1]]["weight"])
                path_weight_from *= g[back_path[i]][back_path[i+1]]["weight"]
        
        except:
            continue
        
        path_weight_factor = path_weight_to * path_weight_from
        print("path weight factor for path", path, back_path, ":", path_weight_factor)
        
        if path_weight_factor > greatest_weight:
            greatest_weight = path_weight_factor
            greatest_path_to = path
            greatest_path_back = back_path
        
        if path_weight_factor < lowest_weight:
            lowest_weight = path_weight_factor
            lowest_path_to = path
            lowest_path_back = back_path
            
if greatest_weight > 1:
    greatest_percent = (greatest_weight - 1) 
else:
    greatest_percent = (1 - greatest_weight) 
greatest_percent = "{:.2%}".format(greatest_percent)

if lowest_weight < 1:
    lowest_percent = (1 - lowest_weight)
else:
    lowest_percent = (lowest_weight - 1)
lowest_percent = "{:.2%}".format(lowest_percent)


print("\n\n\n\n\n\n\n")
print("Maximum disequilibrium:", greatest_weight, "percentage:", greatest_percent)
print("Path:\t", greatest_path_to)
print("\t", greatest_path_back)
print()
print("Minimum disequilibrium:", lowest_weight, "percentage:", lowest_percent)
print("Path:\t", lowest_path_to)
print("\t", lowest_path_back)
input("enter a key to quit")
