from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    tasks = ['task 1', 'task 2', 'task 3']
    return render_template('index.html', tasks=tasks)

# Neue Liste
    # Eingabe Listenname
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


