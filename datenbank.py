from json import dumps, loads


def read_json(file_name):
    with open(file_name, encoding="utf8") as open_file:
        content = open_file.read()
        json_content = loads(content)
    tasks = json_content.get('tasks', [])
    return tasks



def write_json(file_name, inhalt):
    json_inhalt = read_json(file_name)
    json_inhalt.append(inhalt)
    with open(file_name, "w", encoding="utf8") as open_file:
        json_str = dumps(json_inhalt, indent=4)
        open_file.write(json_str)


tasks = read_json('tasks.json')
neuer_task = {
    "name": "Staubsaugen",
    "deadline": "01.07.2023",
    "priority": "mittel",
    "category": "Haushalt"
}
write_json('tasks.json', neuer_task)


tasks.append(neuer_task)
write_json('tasks.json', tasks)


kategorie = read_json('kategorie.json')
neue_kategorie = {
    "name": "Haushalt"
}
kategorie = {neue_kategorie['name']: neue_kategorie}
write_json('kategorie.json', kategorie)



