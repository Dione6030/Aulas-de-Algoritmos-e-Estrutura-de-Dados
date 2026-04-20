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
    
    print("1. Melhores dos anos 50 a 70")
    print("2. Melhores dos anos 80 a 90")
    print("3. Melhores dos anos 90 a 2000")
    print("4. Melhores dos anos 2000 a 2010")
    print("5. Melhores dos anos 2010 a 2020")
    print("6. Melhores dos anos 2020")
    
    opcao = input("Opção: ")
    
    for corrida in F1:
        ano = int(corrida['Date'][:4])
        piloto = corrida['Winner']
        trofeis = corrida['Grand Prix']
        
        if opcao == "1" and 1950 <= ano <= 1979:
            if piloto not in grupos:
                grupos[piloto] = 0
            grupos[piloto] += 1
        elif opcao == "2" and 1980 <= ano <= 1989:
            if piloto not in grupos:
                grupos[piloto] = 0
            grupos[piloto] += 1
        elif opcao == "3" and 1990 <= ano <= 1999:
            if piloto not in grupos:
                grupos[piloto] = 0
            grupos[piloto] += 1
        elif opcao == "4" and 2000 <= ano <= 2009:
            if piloto not in grupos:
                grupos[piloto] = 0
            grupos[piloto] += 1
        elif opcao == "5" and 2010 <= ano <= 2019:
            if piloto not in grupos:
                grupos[piloto] = 0
            grupos[piloto] += 1
        elif opcao == "6" and 2020 <= ano <= 2024:
            if piloto not in grupos:
                grupos[piloto] = 0
            grupos[piloto] += 1
    
    grupos2 = sorted(grupos.items(), key=lambda x: x[1], reverse=True)
    print("\nNº Piloto.............: Vitórias: Top 3 Troféus:")
    for piloto, vitórias in grupos2[:10]:
        print(f"{piloto:25s}   {vitórias:2d}   {trofeis[:3]}")

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