from dash import html, register_page

register_page(__name__, name='Page 3')

layout = html.Div([

    html.P('Content of page 3')

])