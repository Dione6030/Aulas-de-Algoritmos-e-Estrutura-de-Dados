import random

print("Bem-vindo ao jogo de Craps!")
input("Pressione Enter para iniciar...")

dado1 = random.randint(1,6)
dado2 = random.randint(1,6)


soma = dado1 + dado2
print(f"🎲={dado1} 🎲={dado2}, totalizando {soma}.")

if soma in [7, 11]:
    print("Parabéns, você tirou um 'natural' e ganhou!")
    
elif soma in [2, 3, 12]:
    print("Craps! Tente novamente, dessa vez terá mais sorte.")
    
else:
    ponto = soma
    print(f"Seu ponto é {ponto}, tire o novamente para ganhar.")
    
    while True:
        input("Pressione Enter para lançar os dados novamente...")
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        soma = dado1 + dado2
        
        print(f"🎲={dado1} 🎲={dado2}, totalizando {soma}.")
        
        if soma == ponto:
            print("Parabéns, você ganhou!")
            break
        
        elif soma == 7:
            print("Craps! Tente novamente, dessa vez terá mais sorte.")
            break