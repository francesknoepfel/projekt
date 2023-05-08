import json

with open('datensatz.json') as open_file:
    datensatz = json.load(open_file)

datensatz["priority"] = "High"
datensatz["deadline"] = "Juni"

with open("datensatz.json", "w", encoding="utf8") as open_file:
    json.dump(datensatz, open_file, indent=4)
