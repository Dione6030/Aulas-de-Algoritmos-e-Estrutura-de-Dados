import plotly.express as px

generos = {
    "Drama": 15,
    "Suspense": 6,
    "Comédia": 20,
    "Aventura": 12
}

fig = px.pie(
    names=generos.keys(),
    values=generos.values(),
    title="Distribuição de Filmes por Gênero"
)

fig.show()