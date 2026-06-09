def contagem_regressiva(n):
    # Caso base
    if n == 0:
        print("FIM!")
    else:
        print(n)
        # Chamada recursiva
        contagem_regressiva(n - 1)
contagem_regressiva(5)

print("\n")

def fatorial(n):
    # Caso base
    if n == 1:
        return 1
    # Chamada recursiva
    return n * fatorial(n - 1)
print(fatorial(5))