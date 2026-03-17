#3. Elaborar um programa que leia uma palavra. Exiba a letra inicial (e suas ocorrências) e "_" nas demais posições.

palavra = input("Palavra: ")

if palavra.isspace():
    print("Ops... Por favor, digite uma palavra válida.")

else: 
    palavraFatiada = palavra.split()
    
    letraInicial = palavraFatiada[0][0]
    
    resultado = letraInicial + "_" * (len(palavra)-1)
    
    