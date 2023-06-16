import json


def read(file_name):
    """
    sLiest den Inhalt einer JSON-Datei und gibt ihn als Liste zurück oder eine leere Liste, wenn die Datei nicht existiert
    oder leer ist.
    """
    try:
        with open(file_name, 'r') as f:
            json_content = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        json_content = []
    return json_content


def write_json(file_name, inhalt):
    """
    Schreibt den übergebenen Inhalt in eine JSON-Datei. Wenn die Datei bereits existiert, wird der Inhalt als Listenelement
    angehängt. Wenn die Datei nicht existiert, wird eine neue Datei mit dem Inhalt als Listenelement erstellt.
    """
    json_inhalt = read(file_name)
    json_inhalt.append(inhalt)
    with open(file_name, "w", encoding="utf8") as open_file:
        json_str = json.dumps(json_inhalt, indent=4)
        open_file.write(json_str)
