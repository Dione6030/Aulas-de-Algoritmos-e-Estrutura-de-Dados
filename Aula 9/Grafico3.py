import plotly.express as px

inscritos = {
    "Semana1": 10,
    "Semana2": 16,
    "Semana3": 20,
    "Semana4": 29
}

fig = px.line(
    x=inscritos.keys(),
    y=inscritos.values(),
    title="Distribuição de Filmes por Gênero"
)

fig.show()