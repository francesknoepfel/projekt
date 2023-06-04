from flask import Flask, render_template, request
from datenbank import write_json, read

app = Flask(__name__)

# dictionary zum Speichern von Aufgaben für jede Liste und Kategorien
tasks = {}
list_tasks = {}
category_data = {}

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
def neuer_task(list_tasks=None, category_data=None, show_task_saved=False, task=None):
    list_names = get_list_names()  # list names holen
    tasks = []  # Liste der Tasks aus Datenquelle holen

    # Pass the list of pre-existing categories to the template
    categories = ["Schule", "Haushalt", "Finanzen", "Familie", "Einkauf", "Sonstiges"]

    return render_template('neuer_task.html', list_names=list_names, list_tasks=list_tasks, category_data=category_data, show_task_saved=show_task_saved, task=task)

@app.route('/save_task', methods=['POST'])
def save_task():
    list_names = get_list_names()

    task = {
        'name': request.form['task_name'],
        'deadline': request.form['deadline'],
        'priority': request.form['priority'],
        'list_name': request.form['list_name'],
        'category': request.form['category']
    }

    if task['category'] == "new_category":
        new_category = request.form['new_category_name']
        # Add the new category to the category list
        categories.append(new_category)
        # Update the template with the updated category list
        category_data['categories'] = categories

        task['category'] = new_category

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

    # Task in der JSON-Datei speichern
    write_json('daten/tasks.json', list_tasks)

    return neuer_task(list_tasks=list_tasks, category_data=category_data, show_task_saved=True, task=task)

@app.route('/add_task', methods=['POST'])
def add_task():
    list_names = get_list_names()  # Namen der Listen holen
    task = {
        'name': request.form['task_name'],
        'deadline': request.form['deadline'],
        'priority': request.form['priority'],
        'list_name': request.form['list_name'],
        'category': request.form['category']
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

    # Task in der JSON-Datei speichern
    write_json('daten/tasks.json', list_tasks)

    return render_template('index.html', list_tasks=list_tasks, task=task, list_names=list_names, category_data=category_data)

@app.route('/add_list', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True, port=5003)
