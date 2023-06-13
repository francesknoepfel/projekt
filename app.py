from flask import Flask, render_template, request, redirect, url_for
from datenbank import write_json, read
from categories import categories
import plotly.express as px
import re
import os

app = Flask(__name__)

# Declare and initialize category_data globally
category_data = {}

# Load categories at the beginning
def load_categories():
    with open('categories.txt', 'r') as file:
        categories = [line.strip() for line in file]
    return categories

# Load categories into category_data
category_data['categories'] = load_categories()

@app.route('/mein_projekt')
def mein_projekt():
    return render_template('mein_projekt.html')

@app.route('/task_overview')
def task_overview():
    list_names = get_list_names()
    print(category_data)  # Add this line to check the contents of category_data
    return render_template('task_overview.html', tasks=category_data, category_data=category_data, list_names=list_names)

@app.route('/graph')
def graph():
    # Define and populate the chart data
    chart_data = {
        'categories': ['Category 1', 'Category 2', 'Category 3'],
        'values': [10, 20, 30]
    }

    # Create a pie chart using Plotly Express
    fig = px.pie(chart_data, values='values', names='categories', labels={'categories': 'Category Names'})

    # Convert the graph to HTML
    graph_html = fig.to_html(full_html=False)

    return render_template('graph.html', graph_html=graph_html)

def get_list_names():
    lists = read('daten/lists.json')
    return [lst['name'] for lst in lists]

@app.route('/')
def index():
    sort_option = request.args.get('sort')  # Get the selected sort option from the URL parameter

    list_names = get_list_names()  # Get list names

    # Merge tasks from all categories into a single list
    tasks_list = []
    for category in category_data.values():
        if isinstance(category, dict) and 'tasks' in category:
            tasks_list.extend(category['tasks'])

    # Sort the tasks based on the selected option
    if sort_option == 'priority':
        tasks_list.sort(key=lambda x: x['priority'])
    elif sort_option == 'deadline':
        tasks_list.sort(key=lambda x: x['deadline'])
    elif sort_option == 'category':
        tasks_list.sort(key=lambda x: x['category'])

    # Filter tasks for highest priority
    highest_priority_tasks = [task for task in tasks_list if task['priority'] == 'High']
    # Filter remaining tasks for other categories
    other_tasks = [task for task in tasks_list if task['priority'] != 'High']

    return render_template('index.html', list_names=list_names, highest_priority_tasks=highest_priority_tasks, other_tasks=other_tasks, category_data=category_data, sort_option=sort_option)

# return render_template('neuer_task.html', list_names=list_names, categories=category_data['categories'], category_data=category_data)

tasks = []
category_data = {}

@app.route('/neuer_task', methods=['GET', 'POST'])
def neuer_task():
    if 'categories' not in category_data:
        category_data['categories'] = []

    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = request.form['priority']
        category = request.form['category']
        task_duration = request.form['task_duration']

        if category == 'new_category':
            new_category = request.form.get('new_category', '').strip()
            if new_category and new_category not in category_data['categories']:
                category_data['categories'].append(new_category)
                category = new_category

        task = {
            'name': task_name,
            'deadline': deadline,
            'priority': priority,
            'category': category,
            'duration': task_duration,
            'finished': False
        }

        if category in category_data:
            category_data[category]['tasks'].append(task)
        else:
            category_data[category] = {'tasks': [task], 'lists': []}

        list_names = get_list_names()
        return redirect(url_for('task_overview'))

    list_names = get_list_names()

    return render_template('neuer_task.html', list_names=list_names, categories=category_data['categories'], category_data=category_data, category=None)



@app.route('/save_task', methods=['POST'])
def save_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        deadline = request.form['deadline']
        priority = request.form['priority']
        category = request.form['category']
        task_duration = request.form['task_duration']

        # Check if a new category was selected or entered
        if category == 'new_category':
            new_category = request.form['new_category']
            category = new_category.strip()  # Remove leading/trailing spaces

            # Add the new category to the category list if it doesn't already exist
            if category not in categories:
                categories.append(category)

        task = {
            'name': task_name,
            'deadline': deadline,
            'priority': priority,
            'category': category,
            'duration': task_duration,
            'finished': False
        }

        if category in category_data:
            category_data[category]['tasks'].append(task)
            print(category_data)  # Debug statement
        else:
            category_data[category] = {'tasks': [task], 'lists': []}
            print(category_data)  # Debug statement

        return redirect(url_for('task_saved', task_name=task_name, task=task))  # Pass 'task' to the 'task_saved' template

    list_names = get_list_names()
    return render_template('neuer_task.html', list_names=list_names, categories=category_data['categories'], category_data=category_data)

@app.route('/task_saved', methods=['POST'])
def task_saved():
    task_name = request.form['task_name']
    deadline = request.form['deadline']
    priority = request.form['priority']
    category = request.form['category']
    task_duration = request.form['task_duration']
    notes = request.form['notes']

    task = {
        'name': task_name,
        'deadline': deadline,
        'priority': priority,
        'category': category,
        'duration': task_duration,
        'notes': notes
    }

    return render_template('task_saved.html', task=task)

@app.route('/mark_task_finished', methods=['POST'])
def mark_task_finished():
    task_id = int(request.form['task_id'])
    tasks_list = []
    for category in category_data.values():
        if isinstance(category, dict) and 'tasks' in category:
            tasks_list.extend(category['tasks'])

    if task_id < len(tasks_list):
        tasks_list[task_id]['finished'] = True

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5004)
