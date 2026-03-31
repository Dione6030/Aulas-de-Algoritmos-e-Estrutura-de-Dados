import time
import os
import subprocess
palavras = []
dicas = []

def limpa_tela():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def carrega_dados():
    if not os.path.isfile("palavras.txt"):
        print("Nenhum arquivo contendo as palavras foi encontrado.")
        return
    else:
        print("Rastreando palavras.")
    
    with open("palavras.txt", "r") as arq:
        dados = arq.readlines()
        
        for linha in dados:
            linha = linha.strip()
            if not linha:
                continue
            
            partes = linha.split(";", 1)
            if len(partes) == 2:
                palavras.append(partes[0])
                dicas.append(partes[1])

carrega_dados()

print("Bem-vindo ao Jogo da Forca!")
while True:
    print("1. Incluir palavra")
    print("2. Listar palavras")
    print("3. Alterar dica")
    print("4. Excluir palavra")
    print("5. Listar palavras em ordem")
    print("6. Finalizar")
    
    opcao = int(input("Escolha uma opção: ").strip())
    
    if opcao == 1:
        limpa_tela()
        palavra = input("Palavra: ").strip()
        dica = input("Uma palavra de dica: ").strip()
        palavras.append((palavra))
        dicas.append((dica))
        print("Palavra e Dica adicionadas.")
        time.sleep(2)
        limpa_tela()
    
    elif opcao == 2:
        if not palavras:
            print("Não há palavras cadastradas.")
        else:
            largura_palavra = max(len("Palavra"), max(len(p) for p in palavras))
            largura_dica = max(len("Dica"), max(len(d) for d in dicas))

            linha = f"+-{'-' * largura_palavra}-+-{'-' * largura_dica}-+"
            print(linha)
            print(f"| {'Palavra':<{largura_palavra}} | {'Dica':<{largura_dica}} |")
            print(linha)

            for palavra, dica in zip(palavras, dicas):
                print(f"| {palavra:<{largura_palavra}} | {dica:<{largura_dica}} |")
        print(linha)
        print()

    elif opcao == 6:
        print("Desligando...")
        time.sleep(2)
        limpa_tela()
        break
    
    else:
        print()
        print("Opção inválida!")
        print()

def salva_dados():
    with open("palavras.txt", "w") as arq:
        for palavra, dica in zip(palavras, dicas):
            arq.write(f"{palavra};{dica}\n")

salva_dados()