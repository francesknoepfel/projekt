# Importieren notwendiger Module
from flask import Flask, render_template, request, redirect
from categories import categories
import plotly.express as pxs
import plotly.graph_objects as go


# flask klasse wird initialisiert
app = Flask(__name__)

# Laden der Kategorien aus categories,txt und gibt eine liste zurück
def load_categories():
    with open('categories.txt', 'r') as file:
        categories = [line.strip() for line in file]
    return categories

# Initialisierung der Kategorien
categories = load_categories()

# dictionary zur Speicherung von Aufgaben- und Kategoriedaten
category_data = {}

# Die index-Route rendert die Startseite der Anwendung
# zeigt eine Liste der Aufgaben an, sortiert nach den gewählten Optionen (Priorität, Fälligkeitsdatum oder Kategorie)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mein_projekt')
def mein_projekt():
    return render_template('mein_projekt.html')

# zu den generierten graphen
@app.route('/graph')
def graph():
    # enthält eine Liste der Kategorienamen
    # Kategorienamen werden aus dem category_data-Dictionary genommen
    category_names = list(category_data.keys())
    #  enthält eine Liste der Aufgabenzahlen pro Kategorie, für jede Kategorie wird  Anz. der Tasks abgerufen
    category_counts = [len(category_data.get(category, {}).get('tasks', [])) for category in category_names]

    # enthält eine Instanz von Plotly, die ein Kreisdiagramm darstellt
    # Daten für das Kreisdiagramm werden mit category_names als labels erstellt
    fig = go.Figure(data=[go.Pie(labels=category_names, values=category_counts)])
    # enthätl den den HTML code für das Kriesdiagramm
    graph_html = fig.to_html(full_html=False)

    return render_template('graph.html', plot_html=graph_html)

# gibt eine liste der namen der kategorien
def get_list_names():
    return [category.get('category_name', 'Unknown') for category in category_data.values()]

# Anzeige einer Taskübersicht
@app.route('/task_overview')
def task_overview():
    # sortier option für user
    sort_option = request.args.get('sort_option')

    # wird als leere liste initilaisiert, dient dazu alle Aufgaben aus allen Kategorien zu sammeln
    tasks_list = []
    # Schleife die alle werte im category_data dictionary durchläuft
    for category in category_data.values():
        tasks_list.extend(category['tasks'])

    # tasks werden sortiert
    if sort_option == 'priority':
        tasks_list.sort(key=lambda x: x['priority'])
    elif sort_option == 'deadline':
        tasks_list.sort(key=lambda x: x['deadline'])
    elif sort_option == 'category':
        tasks_list.sort(key=lambda x: x['category'])
    else:
        # Standardsortieroption, wenn sort_option nicht bereitgestellt oder ungültig ist
        tasks_list.sort(key=lambda x: x['priority'])

    return render_template('task_overview.html', tasks=tasks_list, category_data=category_data, sort_option=sort_option)

# route um neuen task zu erstellen
@app.route('/neuer_task', methods=['GET', 'POST'])
def neuer_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = 'Hoch'
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
        return redirect("/task_saved")

    list_names = get_list_names()
    return render_template('neuer_task.html', list_names=list_names, categories=load_categories())

# behandelt das Speichern einer Aufgabe
# verarbeitet die eingegebenen Daten und fügt die Aufgabe der entsprechenden Kategorie hinzu
@app.route('/save_task', methods=['POST'])
def save_task():
    # in neuer_task POST anfrage, weshalb formulardaten aus der Anfrage abgerufen werden
    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = request.form['priority']
        category = request.form['category']
        task_duration = request.form['task_duration']
        notes = request.form['notes']

        # wenn user neue kategorie hinzfügen will
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

        # erstellte Task wird zur category_data hinzugefügt.
        if category in category_data:
            category_data[category]['tasks'].append(task)
        else:
            category_data[category] = {'tasks': [task], 'lists': []}

        # Leitet den Benutzer zu task_saved.html weiter
        return redirect("/task_saved")

# zeigt eine Bestätigungsseite an, dass die Aufgabe erfolgreich gespeichert wurde.
@app.route('/task_saved')
def task_saved():
    # zuletzt gespeicherte Aufgabe aus der "category_data"-Sammlung oder der Datenbank wird weitergegeben
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

    return redirect("/task_overview")

if __name__ == '__main__':
    app.run(debug=True, port=5003)