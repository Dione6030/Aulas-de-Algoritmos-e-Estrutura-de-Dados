import random
import time
import os
import subprocess
from colorama import init, Fore

init(autoreset=True)

inimigo = "👾"
obstaculo = "☄️"
personagem = "🚀"
tiro = "⚡"
morte = "💥"
espaco = "✨"


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

vidas = 3
level = 1
turno = 1
pontuacao = 0

linhas = 5
colunas = 7

def limpa_tela():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def cria_matriz():
    matriz = [[espaco for _ in range(colunas)] for _ in range(linhas)]
    pos_jogador = colunas // 2
    matriz[linhas - 1][pos_jogador] = personagem
    return matriz, pos_jogador

def mostra_matriz(matriz):
    limpa_tela()
    global obstaculos, espacos
    
    print(Fore.WHITE + "| " + Fore.GREEN + f"{nome}" + Fore.WHITE + " | " + Fore.YELLOW + f"Vidas: {'❤️' * max(vidas, 0)}" + Fore.WHITE + " | " + Fore.CYAN + f"Level: {level}" +Fore.WHITE + " | " + Fore.BLUE + f"Pontuação: {pontuacao}" + Fore.WHITE + " |")
    
    for linha in matriz:
        print(" ".join(linha))

def faixa_ativa(colunas_ativas):
    inicio = (colunas - colunas_ativas) // 2
    fim = inicio + colunas_ativas
    return inicio, fim

def colunas_por_level(level):
    return min(3 + (level - 1), 7)

def gera_desafios(colunas_ativas):
    linha = [espaco] * colunas
    
    inicio, fim = faixa_ativa(colunas_ativas)
    
    for i in range(inicio, fim):
        r = random.random()
        if r < 0.35:
            linha[i] = inimigo
        elif r < 0.45:
            linha[i] = obstaculo
    return linha

def move_jogador(matriz, pos_jogador, comando):
    matriz[linhas - 1][pos_jogador] = espaco
    if comando == "a" and pos_jogador > 0:
        pos_jogador -= 1
    elif comando == "d" and pos_jogador < colunas - 1:
        pos_jogador += 1
    matriz[linhas - 1][pos_jogador] = personagem
    return pos_jogador

def atira(matriz, pos_jogador):
    for i in range(linhas - 2, -1, -1):
        if matriz[i][pos_jogador] == inimigo:
            matriz[i][pos_jogador] = morte
            mostra_matriz(matriz)
            time.sleep(0.3)
            matriz[i][pos_jogador] = espaco
            return 10
        elif matriz[i][pos_jogador] == obstaculo:
            return 0
        else:
            matriz[i][pos_jogador] = tiro
            mostra_matriz(matriz)
            time.sleep(0.1)
            matriz[i][pos_jogador] = espaco
    return 0

def passa_turno(matriz, colunas_ativas, pos_jogador):
    colidiu = matriz[linhas - 2][pos_jogador] in (inimigo, obstaculo)
    
    matriz[linhas - 1][pos_jogador] = espaco
    
    for i in range(linhas - 2, 0, -1):
        for j in range(colunas_ativas):
            matriz[i][j] = matriz[i - 1][j]
    
    topo = gera_desafios(colunas_ativas)
    for j in range(colunas_ativas):
        matriz[0][j] = topo[j]
    
    for i in range(linhas - 1):
        for j in range(colunas_ativas, colunas):
            matriz[i][j] = espaco
    
    matriz[linhas - 1][pos_jogador] = personagem
    return colidiu

tempo_inicial = time.time()

################################ Programa Principal ###############################

matriz, pos_jogador = cria_matriz()

while vidas > 0:
    colunas_ativas = colunas_por_level(level)
    mostra_matriz(matriz)

    comando = input(
        Fore.YELLOW + "Comando: "
    ).lower()

    if comando in ("a", "d"):
        pos_jogador = move_jogador(matriz, pos_jogador, comando)
    elif comando == "s":
        pontuacao += atira(matriz, pos_jogador)

    if passa_turno(matriz, colunas_ativas, pos_jogador):
        vidas -= 1

    turno += 1
    if turno % 5 == 0:
        level += 1

limpa_tela()
mostra_matriz(matriz)
print(Fore.RED + "\nGame Over! Você perdeu todas as vidas.")

tempo_final = time.time()
duracao = int(tempo_final - tempo_inicial)

print(Fore.CYAN + f"Tempo de Jogo: {duracao:.2f} segundos")
print(Fore.GREEN + f"Pontuação Final: {pontuacao} pontos")

dados = []
if os.path.isfile("placar_galaga.txt"):
    with open("placar_galaga.txt", "r") as arq:
        dados = arq.readlines()

dados.append(f"{nome};{pontuacao};{level};{duracao:.2f}\n")

with open("placar_galaga.txt", "a+") as arq:
    arq.write(f"{nome};{pontuacao};{level};{duracao:.2f}\n")

ranking = sorted(dados, key=lambda x: (int(x.split(';')[1]), int(x.split(';')[2]), float(x.split(';')[3]) * -1), reverse=True)

print()
print("="*43)
print(Fore.YELLOW + "------------< PLACAR DO GALAGA >------------")
print("="*43)
print(Fore.CYAN + "Nº Nome do Jogador.........: Pontos.: Level: Tempo.:")

posicao = 0
for posicao, linha in enumerate(ranking, start=1):
    partes = linha.split(";")
    
    if partes[0] == nome and int(partes[1]) == pontuacao and int(partes[2]) == level and float(partes[3]) == duracao:
        print(Fore.RED + f"{posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}   {int(partes[2]):2d}   {float(partes[3]):6.2f} seg")
    else:
        print(Fore.WHITE + f"{posicao:2d} {partes[0]:25s}   {int(partes[1]):2d}   {int(partes[2]):2d}   {float(partes[3]):6.2f} seg")