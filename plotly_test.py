import plotly.express as px
import pandas as pd
from app import category_data

print(category_data)  # Add this line to inspect the category_data dictionary

# Assuming you have a dictionary called category_data where each key is a category and the value is a list of tasks
# Example category_data: {'Category 1': [{'name': 'Task 1'}, {'name': 'Task 2'}], 'Category 2': [{'name': 'Task 3'}]}

# Prepare the data for the pie chart
category_names = list(category_data.keys())
task_counts = [len(category_data[category]) for category in category_names]

# Create a dataframe with the data
df = pd.DataFrame({'Category': category_names, 'Task Count': task_counts})

# Create the pie chart
fig = px.pie(df, values='Task Count', names='Category', title='Task Distribution by Category')

# Display the chart
fig.show()
