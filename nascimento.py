while True:
    try:
        nascimento = int(input("Digite que ano você nasceu: "))

        if 1900 <= nascimento <= 2026:
            break
        else:
            print("Seu ano de nascimento deve estar entre 1900 e 2026. ")
    except ValueError:
        print("Digite um ano válido. ")

print("Sua data de nascimento é:", nascimento)