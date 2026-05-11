import plotly.express as px

cursos = {
    "ADS": 65,
    "Redes": 30,
    "Marketing": 40,
    "PMM": 25,
    "PG": 45
}

fig = px.bar(
    x=cursos.keys(),
    y=cursos.values(),
    title="Gráfico: Nº Alunos por Curso"
)

fig.show()