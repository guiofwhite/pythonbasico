while True:
    try:
        quantidade = int(input("Qual a quantidade de produtos que você quer: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero!" )
        else:
            break
    except ValueError:
        print("Digite apenas números inteiros. ")

print("A quantidade de produtos que você pegou:", quantidade)