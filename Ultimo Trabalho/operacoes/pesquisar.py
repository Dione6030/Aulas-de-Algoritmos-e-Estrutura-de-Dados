from rich import print
from rich.table import Table
from rich.console import Console
from rich.panel import Panel

import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def pesquisarMusica():
    console = Console()
    
    menu = ("""
    1. Pesquisar por Nome da Música
    2. Pesquisar por Nome do Cantor
    """)
    
    console.print(Panel.fit(menu, title="Pesquisar Música"))
    opcao = int(input("Opção: "))
    
    if opcao == 1:
        nome_musica = input("Digite o nome da música: ")
        
        cursor.execute("""
            SELECT m.id, m.nome, c.nome AS cantor_nome, m.visualizacoes
            FROM musica m
            JOIN cantor c ON m.cantor_id = c.id
            WHERE m.nome ILIKE %s
            OR similarity(m.nome, %s) > 0.2
            ORDER BY similarity(m.nome, %s) DESC
        """, (f"%{nome_musica}%", nome_musica, nome_musica))
        
        musicas = cursor.fetchall()
        
        if not musicas:
            console.print("[bold red]Nenhuma música encontrada com esse nome.[/bold red]")
            return
        
        console = Console()
        tabela = Table(title="Músicas")
        
        tabela.add_column("Nome", style="cyan")
        tabela.add_column("Cantor", style="magenta")
        tabela.add_column("Visualizações", style="green", justify="right")
        
        for musica in musicas:
            cursor.execute("select c.nome from cantor c where c.nome = %s", (musica[2],))
            cantor = cursor.fetchone()
            tabela.add_row(
            musica[1], 
            musica[2], 
            f"{musica[3]:,}".replace(",", ".")
        )
        
        console.print(tabela)
        
    elif opcao == 2:
        nome_cantor = input("Digite o nome do cantor: ")
        
        cursor.execute("""
            SELECT c.id, c.nome
            FROM cantor c
            WHERE c.nome ILIKE %s
            OR similarity(c.nome, %s) > 0.2
            ORDER BY similarity(c.nome, %s) DESC
        """, (f"%{nome_cantor}%", nome_cantor, nome_cantor))
        
        cantores = cursor.fetchall()
        
        if not cantores:
            console.print("[bold red]Nenhum cantor encontrado com esse nome.[/bold red]")
            return
        
        console = Console()
        tabela = Table(title="Cantores")
        
        tabela.add_column("Nome", style="cyan")
        tabela.add_column("Músicas", style="green")
        
        for cantor in cantores:
            cursor.execute("""
                SELECT nome FROM musica WHERE cantor_id = %s ORDER BY visualizacoes DESC LIMIT 1
            """, (cantor[0],))
            musica = cursor.fetchone()

            tabela.add_row(
                cantor[1],
                musica[0] if musica else "Nenhuma"
            )
        
        console.print(tabela)
        
    else:
        console.print("[bold red]Opção inválida![/bold red]")
        return