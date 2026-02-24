import random

print('**************************')
print('*****Jogo adivinhação*****')
print('**************************')

numero_secreto = random.randrange(1,101)
total_tentativas = 10
rodada = 1
dificuldade = (1, 2, 3)

print("Qual dificuldade você gostaria de jogar? ")
print("(1) Fácil (2) Médio (3) Difícil ")

dificuldade = int(input("Defina a dificuldade: "))

if(dificuldade == 1):
    total_tentativas
if(dificuldade == 2):
    total_tentativas = 5
elif(dificuldade == 3):
    total_tentativas = 3

    print("Suas tentativas: ", total_tentativas)
#facil = total_tentativas  
#medio = total_tentativas -5
#dificil = total_tentativas -7

    
for rodada in range(1, total_tentativas + 1):
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