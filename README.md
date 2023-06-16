
# Ausgangslage
Seit ich in meiner Schulkarriere auf mich alleine gestellt bin und selber meine Aufgaben und Deadlines im Griff haben muss, benutze ich To-Do Listen. Mithilfe von Listen kann man strukturiert und organisiert arbeiten, egal ob im Rahmen des Studiums, Haushalts oder sonstigen Verpflichtungen. Zudem bestätigt das Abhaken der Aufgabe bei Vollenden ein Gefühl von Leistungserbringung. Wichtige Funktionsmöglichkeiten für mich sind die Kategorisierung von Aufgaben, sowie Deadline-Setzung und Erinnerungen jener Tasks. 

Als Projekt im Programmieren 2 programmiere ich eine To-Do Liste Webapplikation mit dem Ziel alle möglichen Tasks unter einen Hut zu bringen. Die App sollte es ermöglichen aus vorgegebenen, sowie selber erstellten Kategorien auszusuchen, um eine neue To-Do Liste zu erstellen. Die Tasks sollten schnell erstellt werden können und der entsprechenden Liste zugeordnet werden, sowie schnell und einfach eine Zeit und/oder Datum eingestellt werden. Nutzende der App sollten beim Öffnen eine einfache Übersicht der bevorstehenden Tasks sehen, sowie die dringlichsten Aufgaben hervorgehoben bekommen. 

# Eingebaute Funktionen:
-	Erstellen und Speichern von Aufgaben: Benutzer können neue Aufgaben erstellen und die Details wie Aufgabenname, Deadline, Priorität, Kategorie und Notizen angeben. Diese Aufgaben werden dann in einer Datenbank gespeichert.
-	Aufgabenübersicht: Eine Funktion, um eine Liste aller gespeicherten Aufgaben anzuzeigen. Die Aufgaben können nach verschiedenen Kriterien wie Priorität, Fälligkeitsdatum oder Kategorie sortiert werden.
-	Kategorienverwaltung: Eine Funktion, um Kategorien für Aufgaben zu erstellen, zu bearbeiten und zu löschen. Benutzer können Aufgaben verschiedenen Kategorien zuordnen, um sie besser zu organisieren.
-	Filterung und Sortierung von Aufgaben: Benutzer können die Aufgabenliste nach verschiedenen Kriterien filtern, z. B. nach Priorität, Fälligkeitsdatum oder Kategorie. Sie können auch die Sortierreihenfolge festlegen, um die Aufgaben in aufsteigender oder absteigender Reihenfolge anzuzeigen.

#Ablaufdiagramm
Erster Entwurf:
Siehe Upload im Projektordner
 
Endgültiges Ablaufdiagramm:
Siehe Upload im Projektordner
 
# Anleitung
Diese folgenden Pakete sind erforderlich und müssen zu Beginn installiert werden:
-	Flask: Flask ist ein Web-Framework für Python.
-	render_template: Eine Funktion von Flask, mit der HTML-Templates gerendert werden können
-	request:  Ein Objekt von Flask, das Informationen über die eingehende Anfrage enthält.
-	redirect: Eine Funktion von Flask, um den Benutzer auf eine andere Seite umzuleiten.
-	categories: Eine Modul- oder Dateiabhängigkeit, die die Kategorien für die Anwendung bereitstellt.
-	plotly.express und plotly.graph_objects: Pakete zum Erstellen von interaktiven Diagrammen und Visualisierungen.

Initialisierung der Flask Anwendung
-	Die Flask-Klasse wird initialisiert, indem der Name des Moduls __name__ als Argument übergeben wird.
Laden der Kategorien:
-	Die Funktion load_categories() lädt die Kategorien aus einer Datei (z.B. categories.txt) und speichert sie in einer Variablen (categories).
Definition der Routen und Funktionen:
-	Die Funktionen werden mit der @app.route als Routen definiert.
-	Jede Route wird durch eine Funktion repräsentiert, die eine HTML-Seite (Template) rendert oder eine bestimmte Aktion durchführt, z.B. das Hinzufügen einer Aufgabe oder das Markieren einer Aufgabe als erledigt.
Startseite (index-Route):
-	Die index-Route rendert die Startseite der Anwendung.
-	Abhängig vom sort-Parameter werden die Aufgaben sortiert und in den entsprechenden Jinja2-Templates angezeigt.
Andere Routen und Funktionen:
-	Es gibt weitere Routen und Funktionen für spezifische Seiten und Aktionen wie die Anzeige eines Graphen (graph-Route), die Anzeige einer Aufgabenübersicht (task_overview-Route), das Hinzufügen einer neuen Aufgabe (neuer_task-Route), das Speichern einer Aufgabe (save_task-Route), die Anzeige einer Bestätigungsseite für gespeicherte Aufgaben (task_saved-Route) und das Markieren einer Aufgabe als erledigt (mark_task_finished-Route).
Start App
-	if __name__ == '__main__':: Eine Bedingung, die sicherstellt, dass die App nur gestartet wird, wenn sie direkt ausgeführt wird (nicht, wenn sie importiert wird).
-	app.run(debug=True, port=5003): Startet die Flask-App auf dem angegebenen Port mit Debugging aktiviert..

# Vorhandene Funktionen
In app.py:
-	`load_categories()`: Diese Funktion liest die Kategorien aus der Datei 'categories.txt' und gibt eine Liste der Kategorien zurück.
-	`mein_projekt()`: Diese Funktion ist für die Route '/mein_projekt' zuständig und rendert das Template 'mein_projekt.html'.
-	`graph()`: Diese Funktion ist für die Route '/graph' zuständig und rendert das Template 'graph.html'. Sie erstellt ein Diagramm, das die Anzahl der Aufgaben pro Kategorie anzeigt.
-	`get_list_names()`: Diese Funktion gibt eine Liste der Namen der Kategorien zurück.
-	`index()`: Diese Funktion ist für die Route '/' (Startseite) zuständig und rendert das Template 'index.html'. Sie zeigt eine Liste der Aufgaben an, sortiert nach den gewählten Optionen (Priorität, Fälligkeitsdatum oder Kategorie).
-	`task_overview()`: Diese Funktion ist für die Route '/task_overview' zuständig und rendert das Template 'task_overview.html'. Sie zeigt eine Übersicht aller Aufgaben an.
-	`neuer_task()`: Diese Funktion ist für die Route '/neuer_task' zuständig und behandelt das Hinzufügen einer neuen Aufgabe. Wenn die Methode der Anfrage 'POST' ist, werden die eingegebenen Daten verarbeitet und die Aufgabe wird der entsprechenden Kategorie hinzugefügt. Andernfalls wird das Template 'neuer_task.html' gerendert und die verfügbaren Kategorien werden geladen.
-	`save_task()`: Diese Funktion ist für die Route '/save_task' zuständig und behandelt das Speichern einer Aufgabe. Sie verarbeitet die eingegebenen Daten und fügt die Aufgabe der entsprechenden Kategorie hinzu.
-	`task_saved()`: Diese Funktion ist für die Route '/task_saved' zuständig und rendert das Template 'task_saved.html'. Sie zeigt eine Bestätigungsseite an, dass die Aufgabe erfolgreich gespeichert wurde.
-	`mark_task_finished()`: Diese Funktion ist für die Route '/mark_task_finished' zuständig und behandelt das Markieren einer Aufgabe als erledigt. Sie aktualisiert den Status der Aufgabe und leitet den Benutzer zur Aufgabenübersicht weiter.

In neuer_task.html:
-	handleCategoryChange(selectElement): Diese JavaScript-Funktion wird aufgerufen, wenn sich die Auswahl der Kategorie ändert. Sie überprüft, ob die ausgewählte Kategorie "new_category" ist, und zeigt das Eingabefeld für eine neue Kategorie an, wenn dies der Fall ist.
-	 Ich versuchte eigentlich, JavaScript nicht einzubauen,, da es nicht zum Modul gehörte. Jedoch sah ich schlussendlich keine andere Lösung und durch Recherchieren und Herumprobieren stellte ich fest, dass es letztendlich mit JS machbar war. Da ich das Modul Webprogrammieren bereits absolviert hatte, verfügte ich über ausreichende Grundkenntnisse, und mit dem Lesen der Unterrichtsmaterialien war es letztendlich ein Erfolg.
-	
In datenbank.py:
-	`read(file_name)`: Diese Funktion liest den Inhalt einer JSON-Datei und gibt ihn als Liste zurück. Wenn die Datei nicht existiert oder leer ist, wird eine leere Liste zurückgegeben. Die Funktion nimmt den Parameter `file_name` entgegen, der den Pfad zur JSON-Datei angibt. Sie verwendet die Funktion `json.load()`, um den JSON-Inhalt aus der Datei zu laden.

-	`write_json(file_name, inhalt)`: Diese Funktion schreibt den angegebenen Inhalt in eine JSON-Datei. Wenn die Datei bereits existiert, wird der Inhalt als neues Listenelement hinzugefügt. Wenn die Datei nicht existiert, wird eine neue Datei erstellt und der Inhalt als erstes Listenelement gespeichert. Die Funktion hat zwei Parameter: `file_name`, der den Pfad zur JSON-Datei angibt, und `inhalt`, der der zu schreibende Inhalt ist. Zunächst wird der bestehende JSON-Inhalt aus der Datei mit der Funktion `read()` gelesen, der neue Inhalt wird angehängt und dann wird der aktualisierte Inhalt mit `json.dumps()` in eine JSON-Zeichenkette umgewandelt und in die Datei geschrieben.

Diese Funktionen dienen zum Lesen und Schreiben von JSON-Daten in eine Datei. Die Funktion `read()` ermöglicht es, bestehende Daten aus einer JSON-Datei abzurufen, und die Funktion `write_json()` ermöglicht es, neue Daten zur JSON-Datei hinzuzufügen oder eine neue Datei zu erstellen, falls sie nicht existiert.
Vorhandene Files & Ordnerstruktur
Die Ordnerstruktur mit allen verwendeten Files sieht wie folgt aus:
-	Projekt (Hauptordner für Projekt)
-	Venv (entählt das virtuelle Python Umfeld / Virtual Environment)
-	Daten (Json-dateien zu Datenspeicherung)
o	Datensatz.json
o	Kategorie.json
o	Lists.json
o	Tasks.json
-	Func
o	__init__.py
-	Static
o	Bootstap
o	Css
-	Templates
o	Footer.jinja2
o	Graph.html
o	Header.jinja2
o	Index.html
o	Mein_projekt.html
o	Navbar.jinja2
o	Neue_kategorie.html
o	Neuer_task.html
o	Task_overview.html
o	Task_Saved.html
-	App.py (Hauptdatei die den flask-webserver und die routen für das Projekt enthält)
-	Categories.py (enthält funktionen und definitionen füf kategorien
-	Categories.txt (enthält liste von kategorien)
-	Datenbank.py (funktion unbekannt, und wird vielleicht gar nicht verwendet)

# Reflexion
Als Einstiegsprogrammiererin, die ausserhalb meines Studiums nur wenig Interesse an der Programmierwelt hatte, fiel es mir anfangs schwer, mich in das Projekt zu stürzen. Allerdings musste ich mich zusammenreissen, da mir nun eine zweite Chance gegeben wurde, mich in diesem Kurs zu verbessern und eine ausreichende Note zu erzielen. Anstatt mich auf Desinteresse am Modul einzustellen, versuchte ich meine Perspektive zu ändern, um tatsächlich Fortschritte zu machen. Also begann ich damit. Schnell wurde mir klar, dass mir viele grundlegende Elemente des Programmierens fehlen, wodurch mein Fortschritt äusserst langsam war. Daraufhin entschied ich, dass es am sinnvollsten wäre, den Unterricht als Aufzeichnung anzusehen, damit ich jederzeit pausieren und besser folgen konnte.
Anfangs war mein Fortschritt schleichend und relativ mühsam, um viel verpassten Unterrichtsstoff nachzuholen. Jedoch als ich mit dem Fortschritt der Klasse und den Vorlesungen aufholen konnte, schöpfte ich neue Hoffnung für mein Projekt und begann fleissig daran zu arbeiten, so regelmässig wie ich konnte. Trotz vielen frustrierenden Fehlermeldungen und langsame Fortschritte, bekam ich Freude daran, wenn sich ein mühseliges Problem endlich löste. Dank ChatGPT konnte ich sehr viel Zeit sparen in der Error Meldung Behebung, was ich am Anfang des Projekts nicht gemacht habe. Es war sein sehr hilfreiches Tool und rettete meine Nerven. 
Ich entschied mich für meine Projektidee aus zwei Gründen: Zum einen, weil ich persönlich davon profitieren würde, und zum anderen, weil ich bei meinem ersten Durchgang im Modul Pro2 eine eher komplizierte Projektidee gewählt hatte. Dieses Mal wollte ich mit einer einfachen, aber gut umgesetzten Idee zufrieden sein.
Schlussendlich bin ich sehr zufrieden mit dem Fortschritt den ich im Pro2 Kurs machen konnte, da ich den Vergleich zu vor zwei Jahre mahcen konnte, wo meine Skills ganz klar ungenügend waren. Abgesehen von meinem Projekt, bin ich auch stolz dass ich mit viele Selbst-Disziplin und viele Fleiss meine Wissenslücken schliessen konnte und auch teilweise, sogar (ein wenig) Spass daran hatte.






