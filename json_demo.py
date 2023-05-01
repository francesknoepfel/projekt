import json

with open('datensatz.json') as open_file:
    datensatz = json.load(open_file)

print(datensatz)

datensatz["priority"] = "High"

with open("datensatz.json", n)
