from flask import Flask, render_template, request
from datenbank import write_json, read

app = Flask(__name__)

# dictionary zum Speichern von Aufgaben für jede Liste und Kategorien
tasks = {}
list_tasks = {}
category_data = {}

# list of lists
#lists = [
 #   {'name': 'Category 1'},
 #   {'name': 'Category 2'},
  #  {'name': 'Category 3'},
#]

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

    return render_template('index.html', list_names=list_names, tasks=tasks, lists=lists)



@app.route('/neuer_task')  # route um Tasks zu erstellen
def neuer_task():
    list_names = get_list_names()  # list names holen
    tasks = []  # Liste der Tasks aus Datenquelle holen

    task = request.args.get('task')  # Get the saved task from the query parameters

    return render_template('neuer_task.html', list_names=list_names, tasks=tasks, categories=category_data.keys(), task=task)

@app.route('/save_task', methods=['POST'])  # neuer task kreieren
def save_task():
    list_names = get_list_names()  # list names holen


    task = {
        'name': request.form['task_name'],
        'deadline': request.form['deadline'],
        'priority': request.form['priority'],
        'list_name': request.form['list_name'],
        'category': request.form['list_name']  # Use the selected category as the value
    }
    return render_template('neuer_task.html', list_names=list_names, tasks=[], categories=category_data.keys(), show_task_saved=True, task=task)

@app.route('/neue_liste')  # route um neue Liste zu erstellen
def neue_liste():
    return render_template('neue_liste.html')

# get_all_tasks() funktion definieren
def get_all_tasks():
    # Alle Tasks holen
    tasks = [
        {'name': 'Task 1', 'deadline': '2023-06-01', 'priority': 'High', 'category': 'Work'},
        {'name': 'Task 2', 'deadline': '2023-06-03', 'priority': 'Medium', 'category': 'Personal'},
        {'name': 'Task 3', 'deadline': '2023-06-05', 'priority': 'Low', 'category': 'Work'},
    ]

    return tasks

# Definittion task_overview route
@app.route('/task_overview')
def task_overview():
    tasks = get_all_tasks()  # get_all_tasks() funktion um Tasks zu holen

    return render_template('task_overview.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])  # neuer Task erstellen
def add_task():
    list_names = get_list_names()  # Namen der Listen holen
    task = {
        'name': request.form['task_name'],
        'deadline': request.form['deadline'],
        'priority': request.form['priority'],
        'list_name': request.form['list_name'],
        'category': request.form['list_name']  # Die ausgewählte Kategorie als Wert verwenden
    }
    list_name = task['list_name']
    category = task['category']
    if list_name in list_tasks:
        list_tasks[list_name].append(task)
    else:
        list_tasks[list_name] = [task]

    if category == "new_category":
        new_category = request.form['new_category_name']
        if new_category in category_data:
            category_data[new_category]['tasks'].append(task)
        else:
            category_data[new_category] = {'tasks': [task], 'lists': []}
    elif category in category_data:
        category_data[category]['tasks'].append(task)
    else:
        category_data[category] = {'tasks': [task], 'lists': []}

    # Überprüfen, ob eine neue Kategorie angegeben wurde
    new_category_input = request.form.get('new_category_input')
    if new_category_input:
        if new_category_input in category_data:
            category_data[new_category_input]['tasks'].append(task)
        else:
            category_data[new_category_input] = {'tasks': [task], 'lists': []}

    # Task in der JSON-Datei speichern
    write_json('daten/tasks.json', list_tasks)

    return render_template('task_overview.html', list_tasks=list_tasks, task=task, list_names=list_names, category_data=category_data)


@app.route('/add_list', methods=['POST'])  # neue Liste erstellen
def add_list():
    list_name = request.form['lst_name']
    list_description = request.form['list_description']
    category = request.form['category']

    new_list = {'name': list_name, 'description': list_description}

    lists.append(new_list)
    write_json('daten/lists.json', lists)

    if category == "new_category":
        new_category = request.form['new_category_name']
        if new_category in category_data:
            category_data[new_category]['lists'].append(new_list)
        else:
            category_data[new_category] = {'tasks': [], 'lists': [new_list]}
    elif category in category_data:
        category_data[category]['lists'].append(new_list)
    else:
        category_data[category] = {'tasks': [], 'lists': [new_list]}

    list_names = get_list_names()  # Listen namen holen

    return render_template('index.html', lists=lists, list_names=list_names, list_tasks=list_tasks, category_data=category_data)

if __name__ == '__main__':
    app.run(debug=True, port=5003)
