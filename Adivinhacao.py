import random

print('**************************')
print('*****Jogo adivinhação*****')
print('**************************')

numero_secreto = random.randrange(1,101)
total_tentativas = 5
rodada = 1

for rodade in range(1, total_tentativas + 1):
    print("Tentativa {} de {}". format(rodada, total_tentativas))

    chute_str = input("Digite o seu numero: ")

    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("O número deve ser entre 1 e 100")
        continue


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print("É isso meno você é foda! ")
        break
    else:
        if(maior):
            print("Diminuii")
        elif(menor):
            print("Aumenta o bagulho")
    rodada = rodada + 1

print(numero_secreto)
print("Boa meno tenta de novo se tu é bem home")