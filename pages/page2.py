from dash import html, dcc, register_page, callback, Input, Output
import pandas as pd
import plotly.express as px

# Enregistrement de la page
register_page(__name__, name='Page 2')

# Charger les données
df = pd.read_csv("Soccer_Football Clubs Ranking.csv")

# Mise en page de la page 2
layout = html.Div([
    html.H1("Page 2 - Top 10 Clubs par Pays", style={'textAlign': 'center'}),
    
    html.Label("Sélectionnez un pays :"),
    dcc.Dropdown(
        id='country-dropdown-page2',
        options=[
            {'label': country, 'value': country} for country in df['country'].unique()
        ],
        value=df['country'].unique()[0],  # Sélection du premier pays par défaut
        placeholder="Choisissez un pays"
    ),
    
    dcc.Graph(id='bar-chart-page2'),
    
    html.P("Content of page 2", style={'marginTop': '20px'}),
])

# Callback spécifique à cette page
@callback(
    Output('bar-chart-page2', 'figure'),
    Input('country-dropdown-page2', 'value')
)
def update_bar_chart(selected_country):
    # Filtrer les données par pays
    filtered_df = df[df['country'] == selected_country]
    
    # Trier et sélectionner le top 10
    df_sorted = filtered_df.sort_values(by="point score", ascending=False).head(10)
    
    # Créer la figure
    fig = px.bar(
        df_sorted,
        x="club name ",
        y="point score",
        title=f"Top 10 Clubs de {selected_country}",
        labels={"club name ": "Nom du club", "point score": "Score"}
    )
    return fig
