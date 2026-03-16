num = int(input("Numero: "))

print(f"Divisores de {num}: ", end="")
i=1
while i < num//2 + 1:
    if num % i == 0:
        print(i, end=", ")
    i +=1

divisoresSoma = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        divisoresSoma += i
print("\nSoma dos divisores: ", divisoresSoma)

if divisoresSoma == num:
    print(num, "é um número perfeito")
else:
    print(num, "não é um número perfeito")