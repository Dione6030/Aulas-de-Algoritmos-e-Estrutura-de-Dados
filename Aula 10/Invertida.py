def inverte(palavra):
    # Caso base
    if len(palavra) == 1:
        print(palavra)
    else:
        print(palavra[-1])
        # Chamada recursiva
        inverte(palavra[:-1])
inverte("hello")

def invert_hard(palavra):
    if len(palavra) == 1:
        return palavra
    else:
        # Chamada recursiva
        return palavra[-1] + invert_hard(palavra[0:-1])
print("\n")
print(invert_hard("hello"))