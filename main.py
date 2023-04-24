from flask import Flask
from flask import render_template

app = Flask(__name__)

from flask import Flask, render_template

app = Flask(__name__)

#Noch Tasks richtig definieren mit Kategorie etc.)
tasks = [    {'name': 'Task 1', 'deadline': '2023-05-01', 'priority': 'High'},    {'name': 'Task 2', 'deadline': '2023-05-05', 'priority': 'Medium'},    {'name': 'Task 3', 'deadline': '2023-05-10', 'priority': 'Low'}]
tasks.append({'name': 'Task 4', 'deadline': '2023-05-15', 'priority': 'High'})

# The to-do list page route
@app.route('/')
def todo_list():
    tasks = [] # Empty list of tasks for now
    return render_template('todo.html', tasks=tasks)

# The route for adding a new task
@app.route('/', methods=['POST'])
def add_task():
    task = {'name': request.form['task'], 'deadline': request.form['deadline'], 'priority': request.form['priority']}
    tasks.append(task)
    return render_template('todo.html', tasks=tasks)


@app.route("/")
def start():
    ueberschrifts_text = 'Willkommen zu deiner To Do Listen Übersicht'
    einleitungs_text = "Hier kannst du deine persönlichen Tasks sowie Listen erfassen, um einen Überblick zu behalten. " \
                       "Du kannst deine Tasks auch priorisieren und mit Datum und Zeit aufnehmen, damit du genau siehst, " \
                       "was als Nächstes ansteht. Zudem kannst du aus eigenen oder schon bestehenden Kategorien aussuchen, " \
                       "um deine Tasks zu ordnen. Viel Erfolg!"
    taskerstellen_text = "Möchtest du einen neuen Task erstellen?"
    return render_template('index.html', app_name="To Do List", tasks=tasks,
                           ueberschrift=ueberschrifts_text, einleitung=einleitungs_text,
                           taskerstellen=taskerstellen_text)

# Neue Liste
@app.route('/eingabe', methods=["POST", "GET"])  #
def eingabe_formular():  #
    if request.method == "POST":  #
        kategorie = request.form["kategorie"]  # Kategorie ist der key
        prioritaet = request.form["prioritaet"]   # Priorität ist der key
        deadline = request.form ['deadline']  # request.from bedeutet woher wir was anfragen
        speichern(aktivitaet, dauer, kategorie)  # Wurde so in Daten als def speichern def definiert

    # Eingabe Listenname
    @app.route('/form')
    def form():
        return render_template('form.html')

    # Task hinzufügen --> Ja oder Skip (bei Ja zu "Neuer Task")
# Neuer Task
    # Eingabe Taskname
    # Enddatum / Zeit festlegen
    # Prioriät festlegen
    # Kategorie definieren
    # Neue Kategorie erstellen? --> Skip oder Ja Neue Kategorie erstellen
    # Zu bestehender Liste hinzufügen? --> Skip oder Ja
# Zeige Prioritäten
    # Sortieren nach ... --> Ja oder Skip
    # Eingabe Kategoire/DatumZeit
    # Task hinzufügen --> Ja oder Skip (bei Ja zu "Neuer Task")



if __name__ == "__main__":
        app.run(debug=True, port=5001)



