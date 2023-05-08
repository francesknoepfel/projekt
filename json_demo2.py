from json import dumps, loads


def read_json(file_name):
    with open(file_name, encoding="utf8") as open_file:
        content = open_file.read()
        json_content = loads(content)
    return json_content

def write_json(file_name, inhalt):
    with open(file_name, "w", encoding="utf8") as open_file:
        json_str = dumps(inhalt, indent=4)
        open_file.write(json_str)


lists = read_json('lists.json')
print(lists)
kategorie = read_json('kategorie.json')
print(kategorie)
neue_kategorie = {
    "name": "Haushalt",
    "tasks": "Ofen putzen, Wohnzimmer staubsaugen",
}
kategorie[neue_kategorie['name']] = neue_kategorie
write_json('kategorie.json', kategorie)
    json_inhalt = read_json(file_name)
    
    with open(file_name, "w", encoding="utf8") as open_file:
        json_str = dumps(inhalt, indent=4)
        open_file.write(json_str)
