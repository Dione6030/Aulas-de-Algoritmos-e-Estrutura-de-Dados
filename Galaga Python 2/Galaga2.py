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

def cria_frame(matriz, jogador_col, tiros):
    frame = [linha[:] for linha in matriz]
    frame[linhas - 1][jogador_col] = personagem
    for (tiro_linha, tiro_col) in tiros:
        if 0 <= tiro_linha < linhas and 0 <= tiro_col < colunas:
            frame[tiro_linha][tiro_col] = tiro
    return frame

def garante_linhas_colunas(frame, stdscr):
    Y0 = 2
    CELL_W = 2
    for num, linha in enumerate(frame):
        branco = "".join(ch + " "*(CELL_W-1) for ch in linha)
        stdscr.addstr(Y0 + num, 0, branco)

def mostra_matriz(stdscr, matriz, jogador_col, hud, tiros):
    stdscr.clear()
    stdscr.addstr(0, 0, hud)
    frame = cria_frame(matriz, jogador_col, tiros)
    garante_linhas_colunas(frame, stdscr)
    stdscr.refresh()

def escolhe_inimigo_obstaculo(linha):
    for num in range(colunas):
        aleatorio = random.random()
        if aleatorio < 0.35:
            linha[num] = inimigo
        elif aleatorio < 0.45:
            linha[num] = obstaculo

def gera_desafio():
    linha = [espaco for _ in range(colunas)]
    escolhe_inimigo_obstaculo(linha)
    return linha

def main(stdscr):
    global vidas, level, pontuacao, jogador_col, tiros
    stdscr.timeout(33)
    matriz = cria_matriz()
    
    while vidas > 0:
        hud = (f"Jogador: {nome} | Vidas: {'❤️' * max(vidas, 0)} | Pontos: {pontuacao} | Level: {level}")
        mostra_matriz(stdscr, matriz, jogador_col, hud, tiros)
        
        key = stdscr.getch()
        if key in [ord('a'), ord('A')]:
            jogador_col = max(0, jogador_col -1)
        elif key in [ord('d'), ord('D')]:
            jogador_col = min(colunas - 1, jogador_col + 1)

if __name__ == "__main__":
    curses.wrapper(main)