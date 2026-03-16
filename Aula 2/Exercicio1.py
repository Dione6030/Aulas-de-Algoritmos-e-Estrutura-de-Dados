# Exercício 1:

pessoas = int(input("N° Pessoas: "))
peixes = int(input("N° Peixes: "))

preco = 20 * pessoas

precoPorPeixe = 12 * (peixes - pessoas)
if peixes > pessoas:
    preco += precoPorPeixe

print(f"Pagar: R${preco:.2f}")
