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


listen = read_json('listen.json')
print(listen)
kategorie = read_json('kategorie.json')
print(kategorie)
neue_kategorie = {
    "name": "Haushalt",
    "tasks": "Putzen"
}

kategorie[neue_kategorie['name']] = neue_kategorie



