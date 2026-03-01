from random import randint

print("------- Bem-vindo ao Jogo de 21 -------")

nome = input('Qual é o seu nome? ')
cartas = 0
continuar = True


while cartas < 21 and continuar:
    # Pergunta ao usuário se ele quer uma carta
    escolha = input(f"{nome}, Deseja pedir uma carta? (s/n): ").lower()

    if escolha == 's':
        nova_carta = randint(1, 10)
        cartas += nova_carta
        print(f"Você tirou um {nova_carta}. Total atual: {cartas} pontos.")

        if cartas == 21:
            print("Vinte e Um! Você ganhou! Parabéns!!!")

        elif cartas > 21:
            print(f"Total: {cartas}. Você estourou e perdeu! Tente novamente!")

    else:
        continuar = False
        print(f"Você parou com {cartas} pontos.")

# Caso o jogador pare antes de estourar ou chegar a 21
    if cartas < 21 and not continuar:
        print("Fim de jogo. Boa estratégia!")

        
