#Elabore um programa de implemente um jogo de Craps, conforme descrição a seguir: O jogador lança um par de dados (2 números aleatórios entre 1 e 6), obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você tirou um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "Craps" e você perdeu. Se, na primeira jogada, você fizer um 4, 5, 6, 8, 9 ou 10, este é o seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este "Ponto" novamente.

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