import random
import time
import os
import subprocess
from colorama import init, Fore

init(autoreset=True)

print(Fore.RED + "=" + Fore.BLUE + "=" + Fore.GREEN + "=" + Fore.YELLOW)

tempo_inicial = time.time()

palavras = []
dicas = []
erros = 0
max_erros = 6

def limpa_tela():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def carrega_dados():
    try:
        with open("palavras.txt", "r", encoding="utf-8") as arq:
            dados = arq.readlines()
            for linha in dados:
                partes = linha.split(";")
                palavras.append(partes[0])
                dicas.append(partes[1])
    except FileNotFoundError:
        print(Fore.RED + "Erro... Arquivo com as palavras não existe")
        exit(1)
carrega_dados()

num = random.randint(0, len(palavras)-1)

palavra = palavras[num]
dica = dicas[num]

letras_usadas = [palavra[0]]
palavra_escondida = ["_"] * len(palavra)

for i in range(0, len(palavra)):
    if palavra[i] == palavra[0]:
        palavra_escondida[i] = palavra[0]

def desenha_forca(erros):
    limpa_tela()
    cabeca = "😰" if erros >=1 else " "
    corpo = "|" if erros >= 2 else " "
    braco_esq = "/" if erros >= 3 else " "
    braco_dir = "\\" if erros >= 4 else " "
    perna_esq = "/" if erros >= 5 else " "
    perna_dir = "\\" if erros >= 6 else " "

    print(f"""
     |---|
     |   {cabeca}
     |  {braco_esq}{corpo}{braco_dir}
     |  {perna_esq} {perna_dir}
    ---
    """)
    print("\n")

def mostrar_status():
    desenha_forca(erros)
    print(Fore.GREEN + f"Palavra: {''.join(palavra_escondida)}")
    print(Fore.CYAN + f"Erros: {erros}/{max_erros}")
