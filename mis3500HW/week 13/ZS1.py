#programming activity 1 
import json
import requests
import numpy

url = "https://api.datamuse.com/words?ml=duck&sp=b*&max=5"
req = requests.get(url)

req_dict = json.loads(req.text)

# json.dump(req_dict, open("data.json", "w"))

#programming activity 2
scores = []
for d in req_dict:
    scores.append(d["score"])
    
print(scores)
print("average: ", numpy.mean(scores))