from flask import Flask, render_template, request
# wieso ist write_json nicht aktiv?
from datenbank import write_json, read
from categories import categories
import plotly.express as px
import re
import os

app = Flask(__name__)

# Dictionary zum Speichern von Aufgaben und Kategoriedaten
category_data = {}

@app.route('/mein_projekt')
def mein_projekt():
    return render_template('mein_projekt.html')


@app.route('/graph')
def graph():
    #
    chart_data = {
        'categories': ['Category 1', 'Category 2', 'Category 3'],
        'values': [10, 20, 30]
    }

    #
    fig = px.pie(chart_data, values='values', names='categories', labels={'categories':'Category Names'})

    # Diagrammw wird in HTML konvertiert
    graph_html = fig.to_html(full_html=False)

    return render_template('graph.html', graph_html=graph_html)
def get_list_names():
    lists = read('daten/lists.json')
    return [lst['name'] for lst in lists]

@app.route('/')
def index():
    sort_option = request.args.get('sort')  # Ausgewählte sortieroptiuon aus dem URL-Parameter wird abgerufen

    list_names = get_list_names()  # list namen werden geholt

    # Tasks aus allen Kategorien werden in eine einzige Liste zusammengeführt
    tasks_list = []
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    # Tasks werden basierend auf der ausgewählten Option sortiert
    # Sort the tasks based on the selected option
    if sort_option == 'priority':
        tasks_list.sort(key=lambda x: x['priority'])
    elif sort_option == 'deadline':
        tasks_list.sort(key=lambda x: x['deadline'])
    elif sort_option == 'category':
        tasks_list.sort(key=lambda x: x['category'])

    # Tasks werden nach höchster Priorität filtriert
    highest_priority_tasks = [task for task in tasks_list if task['priority'] == 'High']
    # Verbleibende Aufgaben nach anderen Kategorien filtern
    other_tasks = [task for task in tasks_list if task['priority'] != 'High']

    return render_template('index.html', list_names=list_names, highest_priority_tasks=highest_priority_tasks, other_tasks=other_tasks, category_data=category_data, sort_option=sort_option)

@app.route('/task_overview')
def task_overview():
    # Tasks von allen Kategorien werden in eine einzige liste vereint
    tasks_list = []
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    return render_template('task_overview.html', tasks=tasks_list, category_data=category_data)

#
def load_categories():
    with open('categories.txt', 'r') as file:
        categories = [line.strip() for line in file]
    return categories

categories = load_categories()
@app.route('/neuer_task', methods=['GET', 'POST'])
def neuer_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = request.form['priority']
        category = request.form['category']
        task_duration = request.form['task_duration']

        if category == 'new_category':
            new_category = request.form.get('new_category', '').strip()
            if new_category and new_category not in categories:
                categories.append(new_category)
                category = new_category

        task = {
            'name': task_name,
            'deadline': deadline,
            'priority': priority,
            'category': category,
            'duration': task_duration,
            'finished': False
        }

        if category in category_data:
            category_data[category]['tasks'].append(task)
        else:
            category_data[category] = {'tasks': [task], 'lists': []}

        show_task_saved = True

        list_names = get_list_names()
        return render_template('neuer_task.html', show_task_saved=show_task_saved, task=task, list_names=list_names, categories=categories)

    list_names = get_list_names()

    return render_template('neuer_task.html', list_names=list_names, categories=categories)

@app.route('/save_task', methods=['POST'])
def save_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = request.form['priority']
        category = request.form['category']
        task_duration = request.form['task_duration']

        # Wird abgechcekt ob eine neue kategorie ausgewählt wurde
        if category == 'new_category':
            new_category = request.form['new_category']
            category = new_category.strip()  #

            # neue kategorie wird zu kategorie liste hinzugefügt wenn sie nicht shcon exisitiert
            if category not in categories:
                categories.append(category)

        task = {
            'name': task_name,
            'deadline': deadline,
            'priority': priority,
            'category': category,
            'duration': task_duration,
            'finished': False
        }

        if category in category_data:
            category_data[category]['tasks'].append(task)
        else:
            category_data[category] = {'tasks': [task], 'lists': []}

        show_task_saved = True

    return render_template('neuer_task.html', show_task_saved=show_task_saved, task=task)


@app.route('/mark_task_finished', methods=['POST'])
def mark_task_finished():
    task_id = int(request.form['task_id'])
    tasks_list = []
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    if task_id < len(tasks_list):
        tasks_list[task_id]['finished'] = True

    return index()

if __name__ == '__main__':
    app.run(debug=True, port=5003)