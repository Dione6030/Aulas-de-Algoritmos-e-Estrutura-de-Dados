import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def gerarHTML():
    # Consulta SQL para obter os dados das músicas e cantores
    sql = """
        SELECT m.nome AS musica, c.nome AS cantor, m.visualizacoes, m.img_link
        FROM musica m
        JOIN cantor c ON m.cantor_id = c.id
    """
    cursor.execute(sql)
    resultados = cursor.fetchall()

    # Criação do conteúdo HTML
    html_content = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lista de Músicas e Cantores</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head> 
    <body>
        <h1>Lista de Músicas e Cantores</h1>
        <table>
            <thead>
                <tr>
                    <th>Música</th>
                    <th>Cantor</th>
                    <th>Visualizações</th>
                    <th>Imagem</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for musica, cantor, visualizacoes, img_link in resultados:
        html_content += f"""
                <tr>
                    <td>{musica}</td>
                    <td>{cantor}</td>
                    <td>{visualizacoes}</td>
                    <td><img src="{img_link}" alt="{musica}" width="100"></td>
                </tr>
        """
    
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    # Salvar o conteúdo HTML em um arquivo
    with open("musicas_cantores.html", "w", encoding="utf-8") as file:
        file.write(html_content)