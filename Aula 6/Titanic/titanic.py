import csv

# lista (vetor) de dicionários (objetos) com os passageiros do Titanic
titanic = []

# lê os dados do arquivo e atribui para a lista (titanic)
with open("train.csv") as arq:
    dados = csv.DictReader(arq)
    for linha in dados:
        titanic.append(linha)

# print(titanic[0])
# print(titanic[0]['Name'])

def titulo(texto, traco="-"):
    print()
    print(texto.upper())
    print(traco*40)

def compara_sexo():
    titulo("Compara Passageiros por Sexo x Sobreviventes")
    
    # Masculino: XX
    # Sobreviventes: XX
    # Mortos: XX
    
    # Feminino: XX
    # Sobreviventes: XX
    # Mortos: XX
    
    masculino = masc_sobreviveu = masc_morreu = 0
    feminino = fem_sobreviveu = fem_morreu = 0
    
    for passageiro in titanic:
        sexo = passageiro['Sex']
        sobreviveu = passageiro['Survived']
        
        if sexo == 'male':
            masculino += 1
            if sobreviveu == '1':
                masc_sobreviveu += 1
            else:
                masc_morreu += 1
        else:
            feminino += 1
            if sobreviveu == '1':
                fem_sobreviveu +=1
            else:
                fem_morreu +=1
    
    print(f"Masculino: {masculino}")
    print(f"Sobreviventes: {masc_sobreviveu}")
    print(f"Masculino: {masc_morreu}")
    print()
    print(f"Feminino: {feminino}")
    print(f"Sobreviventes: {fem_sobreviveu}")
    print(f"Masculino: {fem_morreu}")

def media_idosos():
    titulo("Media de Idade e Top 10 Idosos")
    # Média de Idade: XX
    
    # Lista dos 10 Passageiros + Idosos
    # 1. Nome   80 Anos
    
    media = 0
    
    nome = []
    idade = []
    
    for quantidade, passageiro in enumerate(titanic):
        nome.append(passageiro['Name'])
        idade.append(passageiro['Age'])
        
        if passageiro['Age'] != '':
            media += float(passageiro['Age'])

    media /= len(titanic)
    print(f"Média de Idade: {media:.2f}")
    
    print()
    print("Lista dos 10 Passageiros + Idosos")
    
    for i in range(10):
        print(f"{i+1}. {nome[i]}   {idade[i]} Anos")

def compara_classe():
    titulo("Comparação dos Passageiros Classe x Sobreviventes")
    
    # 1ª Classe: XX
    # Sobreviventes: XX
    # Mortos: XX
    
    # 2ª Classe: XX
    # Sobreviventes: XX
    # Mortos: XX
    
    # 3ª Classe: XX
    # Sobreviventes: XX
    # Mortos: XX

while True:
    titulo("Passageiros do Titanic", "=")
    print("1. Comparação por Sexo e Sobreviventes")
    print("2. Média de Idade e Top 10 +Idosos")
    print("3. Comparação por Classe e Sobreviventes")
    print("4. Finalizar")
    
    opcao = int(input("Opção: "))
    if opcao == 1:
        compara_sexo()
    elif opcao == 2:
        media_idosos()
    else:
        break