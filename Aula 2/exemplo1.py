nome = input("Nome do Aluno: ")
idade = int(input("Idade: "))
salario = float(input("Salário R$: "))

print("\n-------------Dados do Aluno-------------")
print(f"Nome do Aluno: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:9.2f}")

if idade < 18:
    print("\nCategoria: Juvenil")
    print("Você é menor de idade...")
    bonus = 300
elif idade < 60:
    print("\nCategoria: Adulto")
    bonus = 500
else:
    print("\nCategoria: Sênior")
    bonus = 700

print(f"\nVocê receberá um bônus de R$: {bonus:9.2f}")

if idade >= 20 and idade <= 30:
    print("Haverá premiação especial para esta categoria...")

print("Bye, bye...")