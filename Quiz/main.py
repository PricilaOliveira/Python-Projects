print("Seja bem vindo ao Quiz!")
answerUser = input("Quer começar ? (S/N)")

# A indentação no Python refere-se à maneira como o código
# é estruturado através do uso de espaços ou tabulações
if answerUser != "S" : 
    quit()

score = 0

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA) ? \n (A) Rockstar Games \n (B) Ubisoft \n (C) EA")
answer1 = input("Resposta ")

if answer1 == "A":
    score = score +1
    print("Correto.")
else: 
    print("Incorreto.")

print("Qual o nome do protagonista do jogo Grand Theft Auto (GTA) ? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline")
answer2 = input("Resposta ")

if answer2 == "B":
    score = score +1
    print("Correto.")
else: 
    print("Incorreto.")

print("Que ano foi lançado o jogo Grand Theft Auto San Andreas (GTA) ? \n (A) 2015 \n (B) 2004 \n (C) 2000")
answer3 = input("Resposta ")

if answer3 == "B":
    score = score +1
    print("Correto.")
else: 
    print("Incorreto.")

# As f-strings vão servir para que você consiga
#  colocar uma variável dentro de um texto, basta colocar {}
print(f"O Quiz acabou. \n Pontuação: {score}/3")