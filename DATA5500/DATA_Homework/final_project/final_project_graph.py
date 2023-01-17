import requests
import json
import time
from datetime import datetime, timedelta
from itertools import permutations
from itertools import combinations
import networkx as nx
from networkx.classes.function import path_weight
import matplotlib.pyplot as plt

#coins that the graph is made out of
coins = {"ripple":"xrp", "bitcoin-cash":"bch", "eos":"eos", "litecoin":"ltc", "ethereum":"eth", "bitcoin":"btc", "binancecoin":"bnb", "stellar":"xlm", "chainlink":"link",  "algorand":"algo"}

g = nx.DiGraph()
edges = []

#making and calling the API
url1 = "https://api.coingecko.com/api/v3/simple/price?ids="
url2 = "&vs_currencies="

names = ",".join(str(name) for name in coins)
tickers = ",".join(str(coins[name]) for name in coins)


url = url1 + names + url2 + tickers
print(url)
dct1 = json.loads(requests.get(url).text)
for c1, c2 in permutations(coins, 2):
    
    try:
        edges.append((c1, c2, dct1[c1][coins[c2]]))
        
    except:
        continue

g.add_weighted_edges_from(edges) 


greatest_weight = -99999999
great_path = []
lowest_weight = 99999999
lowest_path = []
for n1, n2 in combinations(g.nodes,2):
    #print("paths from ", n1, "to", n2)
    for path in nx.all_simple_paths(g, source = n1, target = n2):
        
        #path to node 2
        path_weight_to = 1
        for i in range(len(path)-1):
            #print("edge from", path[i], "to", path[i+1], ": ", g[path[i]][path[i+1]]["weight"])
            path_weight_to *= g[path[i]][path[i+1]]["weight"]
        
        #making a path back
        back_path = path[::-1]
        
        #path from node 2 to node 1
        try:
            path_weight_from = 1
            for i in range(len(path)-1):
                #print("edge from", path[i], "to", path[i+1], ":", g[path[i]][path[i+1]]["weight"])
                path_weight_from *= g[back_path[i]][back_path[i+1]]["weight"]
        
        except:
            continue
        
        path_weight_factor = path_weight_to * path_weight_from
        #print("path weight factor for path", path, back_path, ":", path_weight_factor)
        
        if path_weight_factor > greatest_weight:
            greatest_weight = path_weight_factor
            greatest_path_to = path
            greatest_path_back = back_path
            greatest_path = path + back_path
        
        if path_weight_factor < lowest_weight:
            lowest_weight = path_weight_factor
            lowest_path_to = path
            lowest_path_back = back_path
            lowest_path = path + back_path

#making a list of the path i am taking
x = 0
for i in greatest_path:
    x += 1
    try:
        if greatest_path[x-1] == greatest_path[x]:
            continue
    except:
        True
    great_path.append(i)

    
#calculating the greatest percent either greater than 1 or not
if greatest_weight > 1:
    greatest_percent = (greatest_weight - 1)
    greatest_decimal = (greatest_weight - 1)
else:
    greatest_percent = (1 - greatest_weight)
    greatest_decimal = (1 - greatest_weight)
greatest_percent = "{:.2%}".format(greatest_percent)

#calculating the lowest percent for path
lowest_percent = (lowest_weight - 1)
lowest_percent = "{:.2%}".format(lowest_percent)

#making a visualization of the graph
pos=nx.circular_layout(g) 
nx.draw_networkx(g,pos)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)

plt.savefig("/home/ubuntu/environment/final_project/crypto.png")


#output
print("\n\n\n\n\n\n\n")
print("Maximum disequilibrium:", greatest_weight, "Percentage:", greatest_percent)
print("Path:\t", greatest_path_to)
print("\t", greatest_path_back)
print()
print("Minimum disequilibrium:", lowest_weight, "Percentage:", lowest_percent)
print("Path:\t", lowest_path_to)
print("\t", lowest_path_back)
print("\n")

