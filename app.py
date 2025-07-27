from dash import html, dcc, Dash
import plotly.express as px
import pandas as pd

# Load data
df = px.data.stocks()
fig = px.line(df, x='date', y='GOOG', title='Google Stock Price Over Time')

# Dash app
app = Dash()

app.layout = html.Div([
    html.H1('My First Dash App'),
    html.Hr()
])

# Updated method to run the server
app.run(debug=True, use_reloader=False)