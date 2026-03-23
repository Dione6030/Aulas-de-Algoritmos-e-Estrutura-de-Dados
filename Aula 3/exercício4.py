# 4. faça um verificador para ver se a palavra é um palíndrome

palavra = input("Palvra: ").lower()

if palavra == palavra[::-1]:
    print(f"{palavra} é um Palíndrome.")
else:
    print(f"{palavra} não é um Palíndrome.")