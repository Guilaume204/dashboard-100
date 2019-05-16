import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        multi=True,
        value="MTL"
    ),
    html.H1(children='Hello Dash'),
    html.Div(children='Dash: A web application framework for Python.'),
    dcc.Graph(id='Graph1',
              figure={
                  'data': [
                      {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                       'y': [4, 1, 2] * 5,
                       'type': 'scatter',
                       'name': 'Temperature'},

                      {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                       'y': [2, 4, 5] * 5,
                          'type': 'bar',
                          'name': 'Humidity'}
                  ]
              }
              )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=9997)
