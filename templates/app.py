# Maybe delete if unnötig
from flask import Flask

app = Flask(__name__)

@app.route("/todo_list")
def todo_list():
    tasks = []
    return render_template("todo.html", tasks=tasks)
