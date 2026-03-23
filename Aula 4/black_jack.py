import random
import time
import sys

naipes = "♠♥♦♣"
extras = "JQKA"

# declara uma lista (vetor) que irá conter as cartas
baralho = []

# declara um função definida pelo usuário
def monta_baralho():
    # para cartas de 2 ao 10
    for i in range(2, 11):
        for nipe in naipes:
            # append: adicionar elementos à lista
            baralho.append(str(i)+nipe)

    # para as cartas com JQKA
    for extra in extras:
        for naipe in naipes:
            baralho.append(extra+naipe)
            
# chama a função monta_baralho
monta_baralho()
# print(baralho)

def verifica_pontos(carta):
    if len(carta) == 3:         # 10♠, ...
        num = 10
    elif carta[0].isdigit():     # é um número
        num = int(carta[0])
    elif carta[0] == "A":       # Às vale 11
        num = 11
    else:                       # outras letras JQK : 10
        num = 10
    return num

contador = 0
pontos_jogador = 0      # total de pontos do jogador

while True:
    # gera um número aleatório entre 0 e tam.baralho-1
    num = random.randint(0, len(baralho)-1)
    
    # pop(): para remover uma carta do baralho (lista)
    carta = baralho.pop(num)
    
    contador += 1
    print(f"Sua {contador}ª Carta é: {carta}")
    time.sleep(2)
    
    pontos_jogador += verifica_pontos(carta)
    
    if pontos_jogador >= 21:
        break
    
    if contador >= 2:
        outra = input("Outra Carta (S/N)? ").upper()
        if outra == "N":
            break

print()
print("="*40)
print(f"=> Total de Pontos do Jogador: {pontos_jogador} <=")
print("="*40)
print()

if pontos_jogador > 21:
    print("Bah... Você perdeu. Tente outra vez 🙁😢")
    sys.exit()

################################################# Jogada do Computador

contador = 0
pontos_pc = 0      # total de pontos do computador

while True:
    # gera um número aleatório entre 0 e tam.baralho-1
    num = random.randint(0, len(baralho)-1)
    
    # pop(): para remover uma carta do baralho (lista)
    carta = baralho.pop(num)
    
    contador += 1
    print(f"A {contador}ª Carta do Computador é: {carta}")
    time.sleep(2)
    
    pontos_pc += verifica_pontos(carta)
    
    if pontos_pc >= pontos_jogador or pontos_pc > 21:
        break

print()
print("="*40)
print(f"=> Total de Pontos do Computador: {pontos_pc} <=")
print("="*40)
print()

if pontos_pc > 21:
    print("Parabéns! Você Venceu! 😂🎉")
elif pontos_pc == pontos_jogador:
    print("Xi... Deu Empate! 🤗👍")
else:
    print("Você perdeu! 😡🤬")