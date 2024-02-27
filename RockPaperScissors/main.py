import random

userPoints = 0
computerPoints = 0 

# Estrutura de listas, essa é uma lista que contém Strings
options = ["r", "t","p"]

while True:
    userChoice = input("Escolha R{Pedra}/P{Papel}/T{Tesoura} ou Q para sair. ").lower()
   
    if userChoice == 'q':
        break 
    
    if userChoice not in options:
        continue

    computerChoice = random.randint(0,2)
    computerOption = options[computerChoice]

    print("O computador escolheu " + computerOption)

    if userChoice == computerOption:
        print("Empate.")

    elif userChoice == "r" and computerOption == "t":
        print("Você ganhou!")
        userPoints = userPoints +1

    elif userChoice == "p" and computerOption == "r":
        print("Você ganhou!")
        userPoints = userPoints +1

    elif userChoice == "t" and computerOption == "p":
        print("Você ganhou!")
        userPoints = userPoints +1

    else:
        print("Você perdeu :(")
        computerPoints = computerPoints +1

print("Sua pontuação: " + str(userPoints))
print("Pontuação do Computador: " + str(computerPoints)) 

if computerPoints > userPoints:
    print("Derrota.")
elif computerPoints == userPoints:
    print("Empatou.")
else:
    print("Vitória!!!")