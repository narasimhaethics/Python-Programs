from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Sample data for demonstration
sample_data = {'name': ['John', 'Alice', 'Bob'],
               'age': [25, 30, 22]}

# Convert the sample data to a Pandas DataFrame
df = pd.DataFrame(sample_data)

# Define a route to display data in tabular format
@app.route('/')
def display_data():
    # Convert the DataFrame to HTML for rendering in the template
    table_html = df.to_html(classes='table table-striped', index=False)

    return render_template('index.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
