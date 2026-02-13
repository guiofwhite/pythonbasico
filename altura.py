while True:
    try:
        altura = float(input("Digite uma altura entre 1 e 2: "))

        if 1 <= altura <= 2:
            break
        else:
            print ("A altura deve estar entre 1 ou 2 metros. ")
    except ValueError:
        print(" Digite um valor válido")

print("Sua altura registrada é:", altura)