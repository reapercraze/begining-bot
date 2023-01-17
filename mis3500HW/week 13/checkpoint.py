#json APIs
import requests
import json 

url = "https://api.datamuse.com/words?ml=duck&sp=b*&max=3"
req= requests.get(url)

req_dict = json.loads(req.text)

# json.dump(req_dict, open("words.csv", "w"))

scores = []
for d in req_dict:
    scores.append(d['score'])

print("scores:", scores)