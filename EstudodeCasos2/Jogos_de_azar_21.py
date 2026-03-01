from random import randint

print('------- BEM VINDO AO JOGO DE 21 -------')

nome = input('Qual é o seu nome? ')
cartas = 0

while cartas < 21:
    nova_carta = randint(1, 10)
    cartas += nova_carta
    print(f"{nome}...Você tirou um {nova_carta}. Total atual: {cartas} pontos.")

    if cartas == 21:
        print('Você ganhou! Parabéns!!!')
    elif cartas > 21:
        print('Você é um perdedor! Tente novamente!')
