import dash_grid_layout as dgl
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate

app = dash.Dash('')

app.scripts.config.serve_locally = True

def generate_new_dash_item(idx, x=0, y=0, w=4, h=4, grid_width=150, grid_height=150):
    return html.Div(key=idx,
                    children=[html.Div(className="widget-drag-handle", children="{} another draggable bit".format(idx)),
                                dcc.Graph(
                                        id='{}-example-graph'.format(idx),
                                        style={'height': '{}px'.format(h * grid_height), 'width': '{}px'.format(w * grid_width)},
                                        figure={
                                            'data': [
                                                {'x': [1, 2, 3], 'y': [4, 4, 4], 'type': 'bar', 'name': idx},
                                                {'x': [1, 2, 3], 'y': [1, 1, 1], 'type': 'bar', 'name': u'Montr?al'},
                                            ],
                                            'layout': {
                                                'title': 'Added Data Visualization'
                                            }
                                        }
                                    )
                                ]

                    )

grid_layout = [
                  {"i": 'b', "x": 1, "y": 0, "w": 4, "h": 4, "minW": 2, "maxW": 6},
                  {"i": 'c', "x": 4, "y": 4, "w": 4, "h": 4},
                ]

app.layout = html.Div(children=[html.Div(id='dash-grid-container',
children=[
    dgl.Grid(
        id='dash-grid',
        layout=grid_layout,
        autoSize=True,
        cols=8,
        rows=8,
        rowHeight=155,
        width=1280,
        draggableHandle=".widget-drag-handle",
        children=[
            generate_new_dash_item('b'),
            generate_new_dash_item('c')

        ]
    ),
    html.Div(id='output'),

] ), html.Button('add another graph', id='button')
])


# Callback for adding new elements to the grid
# Because the layout is fundamental to the grid, we can't just render the children of the grid,
# we have to render the entire grid
@app.callback(
	dash.dependencies.Output('dash-grid-container', 'children'),
	[dash.dependencies.Input('button', 'n_clicks')],
	[dash.dependencies.State('dash-grid', 'layout'),
	dash.dependencies.State('dash-grid', 'children')
	])
def display_output(value, layout, children):
    if value is None:
        raise PreventUpdate()
    idx = 'e{}'.format(value)
    e_is_in_layout = bool([lyt for lyt in layout if lyt['i'] == idx])
    if not e_is_in_layout:
        layout.append({"i": idx, "x": 4, "y": 4, "w": 4, "h": 4})
        children.append(generate_new_dash_item(idx))
    resp = [dgl.Grid(
                   id='dash-grid',
                   layout=layout,
                   autoSize=True,
                   cols=8,
                   rows=8,
                   rowHeight=155,
                   width=1280,
                   draggableHandle=".widget-drag-handle",
                   children=children
               )]
    return resp

if __name__ == '__main__':
    app.run_server(debug=True)
