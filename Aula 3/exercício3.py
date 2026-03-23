# 3. Elaborar um programa que leia uma palavra. Exiba a letra inicial (e suas ocorrências) e "_" nas demais posições.

palavra = input("Palavra: ").upper()

for letra in palavra:
    if letra == palavra[0]:
        print(letra, end="")
    else:
        print("_", end="")