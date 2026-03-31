import time
import os
palavras = []
dicas = []
while True:
    print("Bem-vindo ao Jogo da Forca!")
    print("1. Incluir palavra")
    print("2. Listar palavras")
    print("3. Alterar dica")
    print("4. Excluir palavra")
    print("5. Listar palavras em ordem")
    print("6. Finalizar")
    
    opcao = int(input("Escolha uma opção: ").strip())
    
    palavras = []
    if opcao == 1:
        palavra = input("Palavra: ").strip()
        dica = input("Uma palavra de dica: ").strip()
        palavras.append((palavra))
        dicas.append((dica))
    
    elif opcao == 2:
        print(palavras)
        break