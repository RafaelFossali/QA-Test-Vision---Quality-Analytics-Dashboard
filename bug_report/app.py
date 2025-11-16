import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# --- Carrega dados ---
bugs = pd.read_csv("data/bugs_sprint_15.csv")
historico = pd.read_csv("data/historico_bugs.csv")

# --- Gráfico 1: Distribuição de status ---
status_counts = bugs['status'].value_counts().reset_index()
status_fig = px.pie(status_counts, names='index', values='status',
                    title="Distribuição de Status dos Bugs",
                    color_discrete_sequence=px.colors.sequential.Blues)

# --- Gráfico 2: Tendência histórica ---
trend_fig = px.line(historico, x='sprint', y=['corrigidos', 'pendentes', 'despriorizados'],
                    title="Tendência de Bugs nas Últimas Sprints",
                    markers=True)

# --- Gráfico 3: Bugs por Time Responsável ---
team_counts = bugs['time_responsavel'].value_counts().reset_index()
team_fig = px.bar(team_counts, x='index', y='time_responsavel',
                  title="Bugs por Time Responsável", text_auto=True)

# --- Inicializa app Dash ---
app = Dash(__name__)
app.title = "QA Dashboard - Bugs por Sprint"

app.layout = html.Div([
    html.H1("📊 QA Dashboard - Análise de Bugs", style={'textAlign': 'center'}),
    html.Div([
        html.P("Este dashboard mostra métricas automáticas coletadas no final de cada sprint.")
    ], style={'textAlign': 'center'}),

    html.Hr(),

    html.Div([
        html.H3("Distribuição de Status"),
        dcc.Graph(figure=status_fig)
    ]),

    html.Div([
        html.H3("Tendência de Bugs"),
        dcc.Graph(figure=trend_fig)
    ]),

    html.Div([
        html.H3("Bugs por Time"),
        dcc.Graph(figure=team_fig)
    ]),

    html.Footer("Gerado automaticamente pelo Time QA", style={'textAlign': 'center', 'marginTop': '30px'})
])

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
