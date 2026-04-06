import random
import time
import os
import subprocess

palavras = []
dicas = []

def limpa_tela():
    if os.name == 'nt':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def carrega_dados():
    if not os.path.isfile("palavras.txt"):
        print("Nenhum arquivo contendo as palavras foi encontrado.")
        return
    else:
        print("Rastreando palavras.")
    
    with open("palavras.txt", "r") as arq:
        dados = arq.readlines()
        
        for linha in dados:
            linha = linha.strip()
            if not linha:
                continue
            
            partes = linha.split(";", 1)
            if len(partes) == 2:
                palavras.append(partes[0])
                dicas.append(partes[1])

carrega_dados()

print("="*40)
print("Jogo da Forca")
print("="*40)

jogador = input("\nNome do Jogador: ")

def desenha_forca(erros):
    limpa_tela()
    cabeca = "O" if erros >=1 else " "
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

def palavra_aleatoria():
    aleatorio = random.randint(0, len(palavras)-1)
    return palavras[aleatorio], dicas[aleatorio]

palavra, dica = palavra_aleatoria()


def mostra_palavra(palavra_oculta, letras_erradas):
    
    print("Palavra: ", " ".join(palavra_oculta))
    print("Letras Erradas: ", " ".join(letras_erradas))
    print("\n")

def faz_aposta(palavra_oculta, letras_erradas, erros):
    aposta = input("Digite uma letra ou a palavra completa: ").strip().lower()

    if not aposta.isalpha():
        print("Aposta inválida! Digite apenas letras.")
        time.sleep(2)
        return erros

    if len(aposta) == 1:
        if aposta in palavra:
            for i, letra in enumerate(palavra):
                if letra == aposta:
                    palavra_oculta[i] = aposta

        else:
            if aposta not in letras_erradas:
                letras_erradas.append(aposta)
                erros += 1
            else:
                print("Está letra já foi, tente outra!")
                time.sleep(2)

    else:
        if aposta == palavra:
            palavra_oculta[:] = list(palavra)
        else:
            erros += 1

    return palavra_oculta, letras_erradas, erros

def verifica_palavra(palavra_oculta):
    faltam = palavra_oculta.count("_")
    return faltam

erros = 0
palavra_oculta = ["_" for _ in palavra]
letras_erradas = []

################################ Programa Principal ###############################
while True:
    limpa_tela()
    desenha_forca(erros)
    mostra_palavra(palavra_oculta, letras_erradas)
    if erros >= 4:
        print(f"Dica: {dica}")

    palavra_oculta, letras_erradas, erros = faz_aposta(palavra_oculta, letras_erradas, erros)

    if "_" not in palavra_oculta:
        print("Você venceu! 🎉")
        break

    if erros >= 6:
        limpa_tela()
        desenha_forca(erros)
        print(f"Você perdeu! A palavra era: {palavra}")
        break