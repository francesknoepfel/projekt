import json

#read_json--> read (mit refacotirng)
def read(file_name):
    try:
        with open(file_name, 'r') as f:
            json_content = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        json_content = []
    return json_content

def write_json(file_name, inhalt):
    json_inhalt = read(file_name)
    json_inhalt.append(inhalt)
    with open(file_name, "w", encoding="utf8") as open_file:
        json_str = json.dumps(json_inhalt, indent=4)
        open_file.write(json_str)
