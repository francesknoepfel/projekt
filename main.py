import random
from flask import Flask, render_template, request
from datenbank import write_json, read

import datenbank

app = Flask(__name__)

# list of tasks
tasks = []

# list of lists
lists = read('lists.json')

def get_list_names():
    lists = read('lists.json')
    return [lst['name'] for lst in lists]

@app.route('/')
def index():
    list_names = get_list_names()  # Retrieve list names
    return render_template('index.html', tasks=tasks, lists=lists, list_names=list_names)

# add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    list_names = get_list_names()  # Retrieve list names
    task = {
        'name': request.form['task_name'],
        'deadline': request.form['deadline'],
        'priority': request.form['priority'],
        'list_name': request.form['list_name']
    }
    tasks.append(task)
    return render_template('index.html', tasks=tasks, lists=lists, list_names=list_names)

# add a new list
@app.route('/add_list', methods=['POST'])
def add_list():
    list_name = request.form['list_name']
    list_description = request.form['list_description']
    new_list = {'name': list_name, 'description': list_description}
    lists.append(new_list)
    write_json('lists.json', lists)
    list_names = get_list_names()  # Retrieve list names
    return render_template('index.html', tasks=tasks, lists=lists, list_names=list_names)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
