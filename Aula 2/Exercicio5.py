print("Digite números inteiros (0 para parar):")
digitados = []
while True:
    numero = int(input("Números: "))
    counter = len(digitados) + 1
    if numero == 0:
        print("-------------------")
        break
    digitados.append(numero)
print(f"Números digitados: {counter - 1}")

soma = sum(digitados)
print(f"Soma dos números: {soma}")

maior = max(digitados)
print(f"Maior número: {maior}")