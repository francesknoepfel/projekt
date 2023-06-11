import json


def read(file_name):
    """
    Reads the contents of a JSON file and returns it as a list or an empty list if the file doesn't exist or is empty.
    """
    try:
        with open(file_name, 'r') as f:
            json_content = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        json_content = []
    return json_content


def write_json(file_name, inhalt):
    """
    Writes the given content to a JSON file. If the file already exists, the content is appended to it as a list item.
    If the file doesn't exist, a new file is created with the content as a list item.
    """
    json_inhalt = read(file_name)
    json_inhalt.append(inhalt)
    with open(file_name, "w", encoding="utf8") as open_file:
        json_str = json.dumps(json_inhalt, indent=4)
        open_file.write(json_str)
