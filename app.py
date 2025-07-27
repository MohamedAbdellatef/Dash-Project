from dash import html, dcc, Dash
import plotly.express as px
from dash.dependencies import Output, Input
import pandas as pd

# Load data
df = px.data.gapminder()
print(df.columns)
fig = px.scatter(df, x='gdpPercap', y='lifeExp',size='pop',color="continent", title='Life Expectancy vs GDP per Capita')



# Dash app
app = Dash(assets_folder='assete')  # Use your custom assets folder

app.layout = html.Div([
    html.H1('My First Dash App'),
    html.Div([
        dcc.Graph(figure=fig,id='my-graph'),
        dcc.Slider(min=df['year'].min(),step=None, max=df['year'].max(),
                   value=2007, marks={str(year): str(year) for year in df['year'].unique()}, id='my-slider'),
    ], className='section'),
    html.Hr()
])

@app.callback(
    Output('my-graph', 'figure'),
    Input('my-slider', 'value')
)

def update_graph(selected_year):
    mygraph = px.scatter(df[df['year']==selected_year], x='gdpPercap', y='lifeExp',size='pop',color="continent", title='Life Expectancy vs GDP per Capita')
    return mygraph
if __name__ == '__main__':
    app.run(port=8052, debug=True)