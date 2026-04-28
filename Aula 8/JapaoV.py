import csv
import os
import time
import subprocess

visitantes = []

with open("Number of foreign visitors to Japan by month_ .csv") as arq:
    dados = csv.DictReader(arq)
    for linha in dados:
        visitantes.append(linha)

def limpar_tela():
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

def titulo(text, traco="-"):
    print()
    print(text.upper())
    print(traco*40)

def paises():
    #paises = set()
    #for linha in visitantes:
    #    paises.add(linha["Country"])
    
    # ------ list comprehensions
    numero = len(set(x['Country'] for x in visitantes))
    
    limpar_tela()
    print(f"A quantidade de países que visitaram o japão é: {numero}")
    time.sleep(5)
    limpar_tela()

def top10():
    limpar_tela()
    titulo("Top 10 Paises com mais visitantes")
    
    print("N. Paises.......................: NºVisitantes:")
    print("-"*47)
    
    grupos = {}
    
    for linha in visitantes:
        paises = linha['Country']
        qtd_visitantes = int(linha["Visitor"])
        grupos[paises] = grupos.get(paises, 0) + qtd_visitantes
    
    grupos2 = sorted(grupos.items(), key=lambda x: x[1], reverse=True)
    
    for i, (paises, qtd_visitantes) in enumerate(grupos2[:10]):
        print(f"{i+1:2} {paises:30} {qtd_visitantes:13}")
    time.sleep(5)
    limpar_tela()

def paises100mil():
    limpar_tela()
    titulo("Paises com Mais de 100 mil Visitantes")
    
    grupos = {}
    
    for linha in visitantes:
        paises = linha['Country']
        qtd_visitantes = int(linha["Visitor"])
        grupos[paises] = grupos.get(paises, 0) + qtd_visitantes
    
    grupos2 = sorted(grupos.items(), key=lambda x: x[1], reverse=True)
    
    for paises, qtd_visitantes in grupos2:
        if qtd_visitantes > 100000:
            print(paises, end= " | ", flush=True)
    time.sleep(10)
    limpar_tela()

def top10PorAno():
    limpar_tela()
    titulo("Top 10 Paises com mais visitantes por ano")
    
    
    print("N. Paises.......................: NºVisitantes:")
    print("-"*47)
    
    grupos = {}
    
    for linha in visitantes:
        paises = linha['Country']
        qtd_visitantes = int(linha["Visitor"])
        grupos[paises] = grupos.get(paises, 0) + qtd_visitantes
    
    grupos2 = sorted(grupos.items(), key=lambda x: x[1], reverse=True)
    
    for i, (paises, qtd_visitantes) in enumerate(grupos2[:10]):
        print(f"{i+1:2} {paises:30} {qtd_visitantes:13}")
    time.sleep(5)
    limpar_tela()

while True:
    titulo("Menu Principal")
    print("1. Quantidade de países diferentes que visitaram o Japão")
    print("2. Top 10 Países que mais visitaram o Japão")
    print("3. Países com mais de 100 mil visitantes")
    print("4. Top 10 países que mais visitaram o Japão por ano")
    print("5. Sair")
    
    opcao = input("Opção: ")
    if opcao == "1":
        paises()
    if opcao == "2":
        top10()
    if opcao == "3":
        paises100mil()
    else:
        break