from flask import Flask, render_template, request
from datenbank import write_json, read

app = Flask(__name__)

# dictionary zum Speichern von Aufgaben und Kategorien
tasks = {}
category_data = {}

@app.route('/mein_projekt')
def mein_projekt():
    return render_template('mein_projekt.html')

def get_list_names():
    lists = read('daten/lists.json')
    return [lst['name'] for lst in lists]

@app.route('/')
def index():
    list_names = get_list_names()  # Get list names

    # Abrufen von Tasks und Listen auf category_data basiert
    tasks = []
    lists = []
    for category in category_data.values():
        tasks.extend(category['tasks'])
        lists.extend(category['lists'])

    return render_template('index.html', list_names=list_names, tasks=tasks, lists=lists, category_data=category_data)

@app.route('/neuer_task')
def neuer_task(category_data=None, show_task_saved=False, task=None):
    list_names = get_list_names()  # list names holen

    # Übergabe der Liste der vorhandenen Kategorien an die Vorlage.
    categories = ["Schule", "Haushalt", "Finanzen", "Familie", "Einkauf", "Sonstiges"]

    return render_template('neuer_task.html', list_names=list_names, category_data=category_data, show_task_saved=show_task_saved, task=task)

@app.route('/save_task', methods=['POST'])
def save_task():
    task_name = request.form['task_name']
    deadline = request.form['deadline']
    priority = request.form['priority']
    category = request.form['category']
    task_duration = request.form['task_duration']  # Dauer des Tasks holen

    # Create a task dictionary
    task = {
        'name': task_name,
        'deadline': deadline,
        'priority': priority,
        'category': category,
        'duration': task_duration  # Dauer des Tasks wird im dictionary included
    }

    # Task wird zum task list hinzugefügt
    tasks = []
    tasks.append(task)

    if task['category'] == "new_category":
        new_category = request.form['new_category_name']
        # Neue Kategorie zur Kategorie Auswahl hinzufügen
        categories.append(new_category)
        # Die Auswahl wird aktualisiert mit der neuen Kategorie
        category_data['categories'] = categories

        task['category'] = new_category

    category = task['category']
    if category in category_data:
        category_data[category]['tasks'].append(task)
    else:
        category_data[category] = {'tasks': [task], 'lists': []}

    return neuer_task(category_data=category_data, show_task_saved=True, task=task)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
