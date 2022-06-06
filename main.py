# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

import sqlite3

con = sqlite3.connect('sample.sqlite')

df = pd.read_sql("Select * from temperatures;", con)
df['dt'] = pd.to_datetime(df['dt'], unit="s", origin='unix')

balances_df = pd.read_sql("Select * from balances;", con)
balances_df['dt'] = pd.to_datetime(balances_df['dt'], unit="s", origin='unix')

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.DataFrame({
#    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#    "Amount": [4, 1, 2, 2, 4, 5],
#    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
#})

fig = px.line(df, x="dt", y="temp")
balances = px.line(balances_df, x="dt", y="balance", color='account_id', symbol="account_id", markers=True)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
html.Div(children='''
        Display account balances
    '''),

    dcc.Graph(
        id='balances',
        figure=balances
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)