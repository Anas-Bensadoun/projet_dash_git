from dash import html, register_page

register_page(__name__, path='/', name='Home')

layout = html.Div([

    html.P('Home page')

])