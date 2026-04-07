import random
import time
from colorama import init, Fore

# inicializa o colorama
init(autoreset=True)

print(Fore.BLUE + "===== JOGO DO DESCUBRA A PALAVRA =====")
nome = input(Fore.MAGENTA + "Nome do Jogador: ")

hora_inicial = time.time()

palavras = []
dicas = []
erros = 0
max_erros = 6
pontuacao = 0

def carregar_palavras():
    try:
        with open("palavras.txt", "r", encoding="utf-8") as arq:
            dados = arq.readlines()
            for linha in dados:
                partes = linha.split(";")
                palavras.append(partes[0])
                dicas.append(partes[1])
    except FileNotFoundError:
        print(Fore.RED + "Erro... Arquivo com as palavras não existe")
        exit(1)     # 1: indica erro de execução

carregar_palavras()
#print(palavras)
#print(dicas)

num = random.randint(0, len(palavras)-1)

palavra = palavras[num]
dica = dicas[num]

letras_usadas = [palavra[0]]
palavra_escondida = ["_"] * len(palavra)

for i in range(0, len(palavra)):
    if palavra[i] == palavra[0]:
        palavra_escondida[i] = palavra[0]

#print(palavra)
#print(palavra_escondida)

carinhas = [
    "😀😀😀😀😀",
    "😡😀😀😀😀",
    "😡😡😀😀😀",
    "😡😡😡😀😀",
    "😡😡😡😡😀",
    "😡😡😡😡😡"
]

def mostrar_status():
    print(Fore.YELLOW + f"Status: {carinhas[erros]}")
    print(Fore.GREEN + f"Palavra: {''.join(palavra_escondida)}")
    print(Fore.CYAN + f"Erros: {erros}/{max_erros}")

################################## Programa Principal #########################################
while True:
    # Verifica se perdeu
    if erros == max_erros:
        print(Fore.RED + f"Perdeu... A palavra era {palavra} 🥺🥺")
        break
    
    mostrar_status()
    
    # Verifica se ganhou
    if "".join(palavra_escondida) == palavra:
        print(Fore.BLUE + f"Parabéns {nome}! Acertou! 🎉🎉")
        break
    
    letra = input("\nLetra ou * para ver dica (vale 1 vida): ").upper()
    
    if letra.strip() == "" or len(letra.strip()) > 1:
        print(Fore.RED + "Informe uma letra ou *")
        continue
    
    if letra == "*":
        if "*" in letras_usadas:
            print(Fore.RED + "Dica já foi informada")
        else:
            print(Fore.YELLOW + f"Dica: {dica}")
            erros +=1
            letras_usadas.append("*")
        continue
    
    if letra in letras_usadas:
        print(Fore.RED + f"Você já informou a letra: '{letra}'")
        continue
    
    letras_usadas.append(letra)
    
    if letra in palavra:
        print(Fore.GREEN + f"Letra '{letra}' encontrada!")
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida[i] = letra
    else:
        erros += 1
        print(Fore.RED + f"Letra: '{letra}' NÃO EXITE na palavra!")

hora_final = time.time()
duracao = hora_final - hora_inicial
print(f"Jogo durou {duracao:.2f} segundos")