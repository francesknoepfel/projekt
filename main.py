from flask import Flask, render_template, request
from json import loads, dumps


app = Flask(__name__)

# list of tasks
tasks = [{'name': 'Task 1', 'deadline': '2023-05-01', 'priority': 'High', 'list_name': 'List 1'},
         {'name': 'Task 2', 'deadline': '2023-05-05', 'priority': 'Medium', 'list_name': 'List 2'},
         {'name': 'Task 3', 'deadline': '2023-05-10', 'priority': 'Low', 'list_name': 'List 3'}]

# list of lists
lists = [{'name': 'List 1', 'description': 'List 1 description'},
         {'name': 'List 2', 'description': 'List 2 description'},
         {'name': 'List 3', 'description': 'List 3 description'}]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks, lists=lists)

# add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    task = {'name': request.form['task_name'], 'deadline': request.form['deadline'],
            'priority': request.form['priority'], 'list_name': request.form['list_name']}
    tasks.append(task)
    return render_template('index.html', tasks=tasks, lists=lists)

# add a new list
@app.route('/add_list', methods=['POST'])
def add_list():
    list = {'name': request.form['list_name'], 'description': request.form['list_description']}
    lists.append(list)
    return render_template('index.html', tasks=tasks, lists=lists)

# sort by priority
@app.route('/sort_priority', methods=['POST'])
def sort_priority():
    tasks_sorted = sorted(tasks, key=lambda k: k['priority'])
    return render_template('index.html', tasks=tasks_sorted, lists=lists)

print(tasks)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
