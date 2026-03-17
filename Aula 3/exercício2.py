while True:
    nome = input("Nome completo: ")
    if not any(c.isspace() for c in nome):
        print("Ops... Por favor, digite o nome completo")
    else:
        nomeFatiado = nome.split()
        print(f"Nome no Crachá: {nomeFatiado[0].upper()}")
        break