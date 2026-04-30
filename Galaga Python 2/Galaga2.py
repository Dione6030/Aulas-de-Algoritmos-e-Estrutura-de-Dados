import random
import time
import os
import subprocess
import curses
from colorama import init, Fore

init(autoreset=True)

inimigo = "👾"
obstaculo = "☄️"
personagem = "🚀"
tiro = "⚡"
morte = "💥"
espaco = "✨"

vidas = 3
level = 1
pontuacao = 0

linhas = 15
colunas = 10

tiros = []
jogador_col = colunas // 2

print(Fore.RED + "==" + Fore.BLUE + "==" + Fore.GREEN + "==" + Fore.YELLOW + "==" + Fore.CYAN + "==" + Fore.MAGENTA + " JOGO DO GALAGA " + Fore.CYAN + "==" + Fore.YELLOW + "==" + Fore.GREEN + "==" + Fore.BLUE + "==" + Fore.RED + "==")
mostrar_placar = input(Fore.YELLOW + "Deseja ver o placar? (S/N): ").lower()
if mostrar_placar == "s":
    if os.path.isfile("placar_galaga.txt"):
        with open("placar_galaga.txt", "r") as arq:
            dados = arq.readlines()
            
            if dados:
                print()
                print("="*43)
                print(Fore.YELLOW + "------------< PLACAR DO GALAGA >------------")
                print("="*43)
                print(Fore.CYAN + "Nº Nome do Jogador.........: Pontos.: Level: Tempo.:")
                
                for posicao, linha in enumerate(dados, start=1):
                    partes = linha.split(";")
                    print(Fore.WHITE + f"{posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}     {int(partes[2]):2d}   {float(partes[3]):6.2f} seg")
            else:
                print(Fore.YELLOW + "Nenhum jogo registrado no placar.")
    else:
        print(Fore.YELLOW + "Placar não encontrado. Jogue para criar um novo placar!")

nome = input(Fore.MAGENTA + "Nome do Jogador: ")

tutorial = input(Fore.YELLOW + "Deseja ver o tutorial? (S/N): ").lower()
if tutorial == "s":
    print(Fore.CYAN + "\nTutorial:")
    print(Fore.GREEN + "1. Use as teclas A e D para mover o foguete (🚀) para a esquerda ou direita.")
    print(Fore.GREEN + "2. Use a tecla S para atirar.")
    print(Fore.GREEN + "3. Use a tecla Enter para continuar ou pular turno.")
    print(Fore.GREEN + "4. Evite colidir com os inimigos (👾) e obstáculos (🌠).")
    print(Fore.GREEN + "5. Destrua os inimigos para ganhar pontos.")
    print(Fore.GREEN + "6. Obstáculos são indestrutíveis.")
    time.sleep(15)

def cria_matriz():
    return [[espaco for _ in range(colunas)] for _ in range(linhas)]

def mostra_matriz():
    