# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Grid(Component):
    """A Grid component.
Grid is a dashboarding component that allows us to make resizable, draggable layouts

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): children or something
- id (string; optional): The ID used to identify this component in Dash callbacks
- label (string; optional): A label that will be printed when this component is rendered.
- value (string; optional): The value displayed in the input
- cols (number; optional): The number of columns in the grid
- rows (number; optional): The number of rows in the grid
- width (number; optional): Width of each column
- height (number; optional): Height of each row
- colWidth (number; optional): Column width
TODO Not sure if this one is declared properly
- rowHeight (number; optional): Row height
- layout (list; optional): The layout of components in the grid
- next_layout (list; optional): Not to be passed through - holds
- autoSize (boolean; optional): Whether to resize the grid to fit the current layout
- draggableHandle (string; optional): class name for the draggable handle component"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, label=Component.UNDEFINED, value=Component.UNDEFINED, cols=Component.UNDEFINED, rows=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, colWidth=Component.UNDEFINED, rowHeight=Component.UNDEFINED, layout=Component.UNDEFINED, next_layout=Component.UNDEFINED, autoSize=Component.UNDEFINED, draggableHandle=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'label', 'value', 'cols', 'rows', 'width', 'height', 'colWidth', 'rowHeight', 'layout', 'next_layout', 'autoSize', 'draggableHandle']
        self._type = 'Grid'
        self._namespace = 'dash_grid_layout'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'label', 'value', 'cols', 'rows', 'width', 'height', 'colWidth', 'rowHeight', 'layout', 'next_layout', 'autoSize', 'draggableHandle']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Grid, self).__init__(children=children, **args)
