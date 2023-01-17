#9.5
import json

personal_info = {}
personal_info["name"] = "Tyler Gale"
personal_info["age"] = 19
personal_info["major"] = "accounting"

json.dump(personal_info, open("personal_info.json", "w"))

new = json.load(open("personal_info.json", "r"))
print(new)