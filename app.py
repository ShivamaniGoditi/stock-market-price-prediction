from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

# Load and preprocess data
data = pd.read_csv('datasets/TATASTEEL.NS.csv')

@app.route('/')
def index():
    fig = px.line(data, x='Date', y='Stock Price', title='Tata Steel Stock Price Over Time')
    graph = pio.to_html(fig, full_html=False)
    return render_template('index.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)
