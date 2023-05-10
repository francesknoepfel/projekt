from flask import Flask, render_template, request
from datenbank import write_json, read_json

app = Flask(__name__)

# list of tasks
tasks = []

# list of lists
lists = read_json('lists.json')

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
    write_json('lists.json', lists)
    return render_template('index.html', tasks=tasks, lists=lists)

# sort by priority
@app.route('/sort_priority', methods=['POST'])
def sort_priority():
    tasks_sorted = sorted(tasks)
    return render_template('index.html', tasks=tasks_sorted, lists=lists)

@app.route("/neue_kategorie", methods=["GET", "POST"])
def neue_kategorie():
    if request.method == "GET":
        return render_template("neue_kategorie.html")

    if request.method == "POST":
        kategorie_name = request.form['kategorie_name']
        priority = request.form['priority']
        neue_kategorie = {
            "name": kategorie_name,
            "priority": priority
        }
        write_json('kategorie.json', neue_kategorie)
        return "Kategorie wurde gespeichert"


@app.route("/lists")
def get_lists():
    return render_template('task_liste.html', lists=lists)

@app.route("/neuer_task", methods=["GET", "POST"])
def neuer_task():
    if request.method == "GET":
        return render_template("neuer_task.html")

    if request.method == "POST":
        task_name = request.form['task_name']
        priorität = request.form['priorität']
        neuer_task = {
            "name": task_name,
            "priorität": priorität
        }
        write_json('tasks.json', neuer_task)
        return "Task wurde gespeichert"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
