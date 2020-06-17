import json

with open("data.json",'r') as json_file:
        json_data = json.load(json_file)

items = json_data['items']
print(json_data["items"][:5])
