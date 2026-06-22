from rich import print
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt


import psycopg2
from conectar import conexao
cursor = conexao.cursor()

def incluirMusica():
    print("\n[bold green]Inclusão de Música[/bold green]")
    
    nome = input("Nome da música: ")
    print("")
    
    cursor.execute("SELECT id, nome FROM cantor")
    cantores = cursor.fetchall()
    console = Console()
    tabela = Table(title="Cantores")
    
    tabela.add_column("ID", style="blue")
    tabela.add_column("Nome", style="cyan")
    
    for cantor in cantores:
        tabela.add_row(
            str(cantor[0]), 
            cantor[1]
        )
    console.print(tabela)

    cantor_id = Prompt.ask("\nID do cantor: ", choices=[str(cantor[0]) for cantor in cantores])
    visualizacoes = float(input("Visualizações: "))
    img_link = input("Link da imagem: ")
    
    if visualizacoes < 0:
        print("[bold red]Número de visualizações não pode ser negativo[/bold red]")
        return
    
    try:
        sql = """
        insert into musica (nome, cantor_id, visualizacoes, img_link) 
        values (%s, %s, %s, %s)
        """
        
        musica = (nome, cantor_id, visualizacoes, img_link)
        
        cursor.execute(sql, musica)
        conexao.commit()
        print("[green]Música cadastrada com sucesso![/green]")
    except Exception as e:
        print(f"[red]Erro ao cadastrar música: {e}[/red]")
        conexao.rollback()