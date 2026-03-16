produto = input("Produto: ")
etiquetas = int(input("N° de etiquetas: "))

for i in range(0, etiquetas, 2):
    if i + 1 < etiquetas:
        print(produto, " ", produto)
    else:
        print(produto)