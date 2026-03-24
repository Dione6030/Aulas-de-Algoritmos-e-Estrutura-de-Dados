# 5: Verificar se um E-mail é valido

while True:
    email = input("E-mail: ").strip()

    if " " in email:
        print("O E-mail não pode conter espaços")
    elif "@" not in email:
        print("Apresente um E-mail valido")
    else:
        usuario, dominio = email.split("@")
        if not usuario or "." not in dominio:
            print("Apresente um E-mail valido")
        else:
            print("Ok, esse E-mail é valido")
            break