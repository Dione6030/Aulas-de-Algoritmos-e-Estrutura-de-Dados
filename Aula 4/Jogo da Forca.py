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
        palavra = input("Palavra: ")
        dica = input("Uma dica: ")
        junta = zip(palavra, dica)
        palavras.insert(0, junta)
    
    elif opcao == 2:
        print(palavras)
        break