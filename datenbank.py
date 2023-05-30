import json
from json import dumps, loads
# read_json --> read (mit refactoring)
def read(file_name): # wird gebraucht für das Lesen von Inhalt JSON Datein
    try:
        with open(file_name, 'r') as f:
            json_content = json.load(f)
           # print("JSON content:", json_content)  # Print zum ausprobieren
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        json_content = []
    return json_content


def write_json(file_name, inhalt): # wird gebraucht für das schreiben von Inhalt von json dateien
    json_inhalt = read(file_name)
    json_inhalt.append(inhalt)
    with open(file_name, "w", encoding="utf8") as open_file:
        json_str = json.dumps(json_inhalt, indent=4)
        open_file.write(json_str)
   # print("JSON written to file:", file_name)  # Print zum ausprobieren

