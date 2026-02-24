import random

print('**************************')
print('*****Jogo adivinhação*****')
print('**************************')

numero_secreto = random.randrange(1,101)
total_tentativas = 5
rodada = 1

while(rodada <= total_tentativas):

    chute_str = input("Digite o seu numero: ")

    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("O número deve ser entre 1 e 100")
        continue

    print("Seu chute foi: ", chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print("Você Acertou!! ")
        break
    else:
        if(maior):
            print("O seu chute foi maior que o número secreto")
        elif(menor):
            print("O seu chute foi menor que o número secreto")
    rodada = rodada + 1

print(numero_secreto)
print("Fim de jogo otáro")