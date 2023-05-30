import plotly.express as px
import pandas as pd
from flask import Flask, render_template, request
from datenbank import write_json, read

app = Flask(__name__)

# Assuming the user's chosen category is stored in a variable called "chosen_category"
chosen_category = "xy"  # Replace "xy" with the user's chosen category

# Filter the category_data dictionary based on the chosen category
filtered_data = category_data.get(chosen_category, {})

# Convert the filtered data into a DataFrame
df = pd.DataFrame({'Category': list(filtered_data.keys()), 'Task Count': [len(tasks) for tasks in filtered_data.values()]})

# Create the pie chart using Plotly
fig = px.pie(df, values='Task Count', names='Category', title='Tasks nach Kategorie')

# Display the chart
fig.show()

