while True:
    try:
        parcela = int(input("Digite o número de parcelas: "))

        if 1 <= parcela <= 12:
            break
        else:
            print("O número deve estar entre 1 e 12")
    except ValueError:
        print("Digite um número válido")

print("O número de parcelas que você pediu é:", parcela)