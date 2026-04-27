import csv

F1 = []

with open("winners.csv") as arq:
    dados = csv.DictReader(arq)
    for linha in dados:
        F1.append(linha)

def titulo(text, traco="-"):
    print()
    print(text.upper())
    print(traco*40)

def top_pilotos():
    titulo("Top 10 Pilotos com Mais Vitórias")
    grupos = {}
    vitorias = {}
    
    print("1. Melhores dos anos 50 a 70")
    print("2. Melhores dos anos 80 a 90")
    print("3. Melhores dos anos 90 a 2000")
    print("4. Melhores dos anos 2000 a 2010")
    print("5. Melhores dos anos 2010 a 2020")
    print("6. Melhores dos anos 2020")
    
    opcao = input("Opção: ")
    
    intervalo = {
        "1": (1950, 1979),
        "2": (1980, 1989),
        "3": (1990, 1999),
        "4": (2000, 2009),
        "5": (2010, 2019),
        "6": (2020, 2024)
    }
    
    if opcao not in intervalo:
        print("Opção inválida!")
        return
    
    ano_inicio, ano_fim = intervalo[opcao]
    
    for corrida in F1:
        ano = int(corrida['Date'][:4])
        piloto = corrida['Winner']
        trofeis = corrida['Grand Prix']
        
        if ano_inicio <= ano <= ano_fim:
            grupos[piloto] = grupos.get(piloto, 0) + 1
            
            if piloto not in vitorias:
                vitorias[piloto] = {}
            vitorias[piloto][trofeis] = vitorias[piloto].get(trofeis, 0) + 1
        
    grupos2 = sorted(grupos.items(), key=lambda x: x[1], reverse=True)
    print("\nNº Piloto.............: Vitórias: Top 3 Troféus:")
    for piloto, vitórias in grupos2[:10]:
        top3 = sorted(vitorias[piloto].items(), key=lambda x: x[1], reverse=True)
        top3_str = ", ".join([f"{trofeis}({qtd})" for trofeis, qtd in top3[:3]])
        print(f"{piloto:25s}   {vitórias:2d}   {top3_str}")

while True:
    titulo("Menu Principal")
    print("1. Top 10 Pilotos com Mais Vitórias")
    print("2. Equipes com Mais Vitórias")
    print("3. Top 10 Pistas com mais Tempo de Corrida")
    print("4. Sair")
    
    opcao = input("Opção: ")
    if opcao == "1":
        top_pilotos()
    else:
        break