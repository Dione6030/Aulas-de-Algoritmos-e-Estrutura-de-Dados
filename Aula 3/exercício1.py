print("Coloque uma senha entre 8 e 12 caracteres, possuir letras maiúsculas, minúsculas e números.")

senha = input("Senha: ")
if len(senha) < 8 or len(senha) > 12:
    print("Senha inválida. A senha deve conter entre 8 e 12 caracteres.")
    
elif not any(c.isupper() for c in senha):
    print("Senha inválida. A senha deve conter pelo menos uma letra maiúscula.")
    
elif not any(c.islower() for c in senha):
    print("Senha inválida. A senha deve conter pelo menos uma letra minúscula.")
    
elif not any(c.isdigit() for c in senha):
    print("Senha inválida. A senha deve conter pelo menos um número.")
    
else:
    print("Senha válida.")