from flask import Flask, render_template, request
from datenbank import write_json, read

app = Flask(__name__)

# dictionary to store tasks for each list
list_tasks = {}

# list of lists
lists = read('daten/lists.json')


def get_list_names():
    lists = read('daten/lists.json')
    print(type(lists))
    print(lists)
    return [lst['name'] for lst in lists]


@app.route('/')
def index():
    list_names = get_list_names()  # Retrieve list names
    print(list_names)  # Print list names
    return render_template('index.html', lists=lists, list_names=list_names)


# add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    list_names = get_list_names()  # Retrieve list names
    task = {
        'name': request.form['task_name'],
        'deadline': request.form['deadline'],
        'priority': request.form['priority'],
        'list_name': request.form['lst_name']
    }
    list_name = task['list_name']
    if list_name in list_tasks:
        list_tasks[list_name].append(task)
    else:
        list_tasks[list_name] = [task]
    return render_template('index.html', lists=lists, list_names=list_names, list_tasks=list_tasks)


# add a new list
@app.route('/add_list', methods=['POST'])
def add_list():
    list_name = request.form['lst_name']
    list_description = request.form['list_description']
    new_list = {'name': list_name, 'description': list_description}
    lists.append(new_list)
    write_json('daten/lists.json', lists)
    list_names = get_list_names()  # Retrieve list names
    print(list_names)  # Print list names
    return render_template('index.html', lists=lists, list_names=list_names, list_tasks=list_tasks)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
