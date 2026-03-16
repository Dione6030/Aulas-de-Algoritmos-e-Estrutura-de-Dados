chinchilas = int(input("Número de chinchilas: "))
anos = int(input("Anos de criação: "))

for i in range(anos):
    print(f"{i+1}° Ano: {chinchilas} chinchilas")
    chinchilas *= 3