# Importando Lib
import random

print("Seja bem vindo ao Guess Number.")
choiceNumber = input("Digite um número teto para o desafio: ")

if choiceNumber.isdigit():
   choiceNumber = int(choiceNumber)
else:
   print("Erro: Valor informado não é numérico. Tente novamente.")
   quit()

randomNumber = random.randint(0, choiceNumber)

countingChoices = 0

while True:
    answerUser = input("Advinhe o número: ")

    countingChoices = countingChoices +1
    if answerUser.isdigit():
        answerUser = int(answerUser)
    else:
        print("Erro: Valor informado não é numérico. Tente novamente.")    
        continue
    
    if answerUser == randomNumber:
        print("Você acertou!!!")
        break
    elif answerUser > randomNumber:
        print("Chutou alto, o número é menor.")
    else:
        print("Chutou baixo, o número é maior.")

print("Número de tentativas: " + str(countingChoices))