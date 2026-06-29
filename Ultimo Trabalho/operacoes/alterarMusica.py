from rich import print
from rich.table import Table
from rich.console import Console

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def alterarMusica():
    cursor.execute("select * from musica")
    musicas = cursor.fetchall()
    
    console = Console()
    tabela = Table(title="Músicas")
    
    tabela.add_column("ID", style="yellow", justify="right")
    tabela.add_column("Nome", style="cyan")
    tabela.add_column("Cantor", style="magenta")
    tabela.add_column("Visualizações", style="green", justify="right")
    
    for musica in musicas:
        cursor.execute("select c.nome from cantor c where c.id = %s", (musica[2],))
        cantor = cursor.fetchone()
        tabela.add_row(
            str(musica[0]),
            musica[1], 
            cantor[0], 
            f"R$ {musica[3]:,}".replace(",", ".")
        )
    
    console.print(tabela)
    
    opcao = int(input("Digite o ID da música que deseja alterar: "))
    
    nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    visualizacoes = input("Digite o novo número de visualizações (ou pressione Enter para manter o atual): ")
    img_link = input("Digite o novo link da imagem (ou pressione Enter para manter o atual): ")
    
    if visualizacoes.strip() == "":
        visualizacoes = None
    else:
        visualizacoes = int(visualizacoes)
        if visualizacoes < 0:
            print("[red]O número de visualizações deve ser um valor não negativo[/red]")
            return
    
    sql= """
        update musica
        set nome = coalesce(nullif(%s, ''), nome),
            visualizacoes = coalesce(%s, visualizacoes),
            img_link = coalesce(nullif(%s, ''), img_link)
        where id = %s
        """
    
    cursor.execute(sql, (nome, visualizacoes, img_link, opcao))
    conexao.commit()