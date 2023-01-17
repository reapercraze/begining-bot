#programming activity 1
import json

person = {}
person["name"] = "Tyler Gale"
person["fav_color"] = ["yellow", "purple", "red"]
person["hieght"] = [48, 50, 52, 54, 56, 60, 66, 69, 71, 72, 73]

json.dump(person, open("person.json", "w"))
