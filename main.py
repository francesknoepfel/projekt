from flask import Flask
from flask import render_template
from flask import request

from func import datenbank

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if__name__=='__main__':
    app.run(debug_True)

