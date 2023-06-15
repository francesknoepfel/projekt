from flask import Flask, render_template, request, redirect
# from categories import categories
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

def load_categories():
    with open('categories.txt', 'r') as file:
        categories = [line.strip() for line in file]
    return categories

categories = load_categories()


# dictionary zur Speicherung von Aufgaben- und Kategoriedaten
category_data = {}

@app.route('/mein_projekt')
def mein_projekt():
    return render_template('mein_projekt.html')

@app.route('/graph')
def graph():
    tasks_list = []
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    completed_tasks = sum(1 for task in tasks_list if task['finished'])
    incomplete_tasks = sum(1 for task in tasks_list if not task['finished'])

    # Create a bar chart for task status
    data = [
        go.Bar(x=['Abgeschlossene Aufgaben', 'Unvollständige Aufgaben'], y=[completed_tasks, incomplete_tasks])
    ]
    layout = go.Layout(title='Aufgabenstatus', xaxis={'title': 'Aufgabenstatus'}, yaxis={'title': 'Anzahl der Aufgaben'})
    fig_status = go.Figure(data=data, layout=layout)
    status_html = fig_status.to_html(full_html=False)

    # Retrieve task durations from your data
    task_durations = [task['task_duration'] for category in category_data.values() for task in category['tasks']]

    # Create a histogram
    fig_histogram = px.histogram(task_durations, nbins=10, title='Task Duration Histogram')
    histogram_html = fig_histogram.to_html(full_html=False)

    # Combine the HTML for both graphs
    graph_html = status_html + histogram_html

    return render_template('graph.html', graph_html=graph_html)

def get_list_names():
    # Ersetze diese Funktion durch deine eigene Implementierung,
    # um die Namen der Listen aus deiner Datenquelle abzurufen
    return []

@app.route('/')
def index():
    sort_option = request.args.get('sort')

    list_names = get_list_names()

    tasks_list = []
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    if sort_option == 'priority':
        tasks_list.sort(key=lambda x: x['priority'])
    elif sort_option == 'deadline':
        tasks_list.sort(key=lambda x: x['deadline'])
    elif sort_option == 'category':
        tasks_list.sort(key=lambda x: x['category'])

    highest_priority_tasks = [task for task in tasks_list if task['priority'] == 'Hoch']
    other_tasks = [task for task in tasks_list if task['priority'] != 'Hoch']

    return render_template('index.html', list_names=list_names, highest_priority_tasks=highest_priority_tasks, other_tasks=other_tasks, category_data=category_data, sort_option=sort_option)

@app.route('/task_overview')
def task_overview():
    tasks_list = []
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    return render_template('task_overview.html', tasks=tasks_list, category_data=category_data)

@app.route('/neuer_task', methods=['GET', 'POST'])
def neuer_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = 'Hoch'  # Setze die Priorität auf 'Hoch'
        category = request.form['category']
        task_duration = request.form['task_duration']
        notes = request.form['notes']

        if category == 'new_category':
            new_category = request.form.get('new_category', '').strip()
            if new_category:
                category = new_category
                if category not in categories:
                    categories.append(category)

        task = {
            'name': task_name,
            'deadline': deadline,
            'priority': priority,
            'category': category,
            'task_duration': task_duration,
            'notes': notes,
            'finished': False
        }

        if category in category_data:
            category_data[category]['tasks'].append(task)
        else:
            category_data[category] = {'tasks': [task], 'lists': []}

        list_names = get_list_names()
        return render_template('index.html', list_names=list_names, category_data=category_data)

    list_names = get_list_names()
    return render_template('neuer_task.html', list_names=list_names, categories=load_categories())

@app.route('/save_task', methods=['POST'])
def save_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = request.form['priority']
        category = request.form['category']
        task_duration = request.form['task_duration']
        notes = request.form['notes']

        if category == 'new_category':
            new_category = request.form.get('new_category', '').strip()
            if new_category and new_category not in categories:
                categories.append(new_category)
                category = new_category

        # Konvertiert task_duration in Minuten oder Stunden
        task_duration = int(task_duration)
        duration_unit = 'Minuten'

        if task_duration >= 60:
            task_duration = task_duration // 60
            duration_unit = 'Stunden'

        task = {
            'name': task_name,
            'deadline': deadline,
            'priority': priority,
            'category': category,
            'task_duration': f'{task_duration} {duration_unit}',
            'notes': notes,
            'finished': False
        }

        if category in category_data:
            category_data[category]['tasks'].append(task)
        else:
            category_data[category] = {'tasks': [task], 'lists': []}

        # Leitet den Benutzer zu task_saved.html weiter
        return redirect("/task_saved")

@app.route('/task_saved')
def task_saved():
    # Ruft die zuletzt gespeicherte Aufgabe aus category_data
    # oder der Datenbank ab und übergibt sie an die Vorlage
    task = {
        'name': 'Aufgabenname',
        'deadline': '2023-06-15',
        'priority': 'Hoch',
        'category': 'Eine Kategorie',
        'task_duration': '2 Stunden',
        'notes': 'Einige Notizen',
    }

    return render_template('task_saved.html', task=task)

@app.route('/mark_task_finished', methods=['POST'])
def mark_task_finished():
    task_id = int(request.form['task_id'])
    tasks_list = []
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    if task_id < len(tasks_list):
        tasks_list[task_id]['finished'] = True

    return task_overview()

if __name__ == '__main__':
    app.run(debug=True, port=5003)