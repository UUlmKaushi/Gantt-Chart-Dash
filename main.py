
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
 
# ---------------------------------------------------------------------------
# Beispieldaten (später durch Eingabe / Datenbank ersetzen)
# ---------------------------------------------------------------------------
df = pd.DataFrame(
    [
        dict(Task="Planung", Start="2026-01-05", Finish="2026-01-20", Status="Fertig"),
        dict(Task="Design", Start="2026-01-15", Finish="2026-02-05", Status="In Arbeit"),
        dict(Task="Entwicklung", Start="2026-02-01", Finish="2026-03-15", Status="In Arbeit"),
        dict(Task="Test", Start="2026-03-10", Finish="2026-03-31", Status="Geplant"),
        dict(Task="Release", Start="2026-04-01", Finish="2026-04-10", Status="Geplant"),
    ]
)
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])
 
COLORS = {
    "Fertig": "#2ca02c",
    "In Arbeit": "#1f77b4",
    "Geplant": "#999999",
}
 
 
def build_figure(data: pd.DataFrame):
    fig = px.timeline(
        data,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="Status",
        color_discrete_map=COLORS,
    )
    # Erste Aufgabe oben (sonst steht sie unten)
    fig.update_yaxes(autorange="reversed", title=None)
    fig.update_xaxes(title=None)
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        legend_title_text="Status",
        height=400,
    )
    return fig
 
 
# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------
app = Dash(__name__)
app.title = "Gantt Chart"
 
app.layout = html.Div(
    style={"maxWidth": "1100px", "margin": "0 auto", "padding": "20px"},
    children=[
        html.H2("Projektplan"),
        dcc.Graph(id="gantt", figure=build_figure(df)),
    ],
)
 
if __name__ == "__main__":
    app.run(debug=True)
 