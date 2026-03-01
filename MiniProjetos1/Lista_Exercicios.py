# Exercício 1

# Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais),
#  "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

# Solução

import random


def classificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"


print(f'Se lados forem: 5, 5, 5: {classificar_triangulo(5, 5, 5)}')
print(f'Se lados forem: 5, 6, 5: {classificar_triangulo(5, 6, 5)}')
print(f'Se lados forem: 5, 6, 7: {classificar_triangulo(5, 6, 7)}')

# Exercício 2

# Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.

# Solução


def exibir_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for x in range(1, 11):
        resultado = numero * x
        print(f"{numero} x {x} = {resultado}")


exibir_tabuada(7)

# Exercício 3

# Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas.
# Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.

# Solução


def dsa_alunos_acima_da_media(turma):

    if not turma:
        return 'Dicionario de Turma Vazio'

    soma_notas = sum(turma.values())
    media = soma_notas / len(turma)

    print(f'A media da turma é:{media:.2f}')

    aprovados = []

    for aluno, nota in turma.items():
        if nota > media:
            aprovados.append(aluno)

    return aprovados


notas_turma = {'Ana': 8.5, 'Bruno': 6.0,
               'Carla': 9.5, 'Marcelo': 7.0, 'Eliane': 5.5}

print(f'Alunos acima da media: {dsa_alunos_acima_da_media(notas_turma)}')

# Exercício 4

# Dada uma lista de números, crie uma nova lista usando list comprehension que contenha o quadrado de cada número par da lista original.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado_pares = [x ** 2 for x in numeros if x % 2 == 0]

print(quadrado_pares)

# Exercício 5

# Crie uma função chamada dsa_calcula_imc que aceite dois argumentos: peso (em kg) e altura (em metros).
# A função deve calcular o Índice de Massa Corporal (IMC) usando a fórmula IMC=peso/altura^2 e retornar o valor do IMC.


def calcula_imc(peso, altura):
    if altura <= 0:
        return 'Altura invalida. Deve ser maior que zero'

    imc = peso / (altura ** 2)

    return imc


meu_imc = calcula_imc(98, 1.87)
print(f'Seu Imc é: {meu_imc:.2f}')


def pode_votar(idade):
    if idade >= 16:
        return "Pode votar"
    else:
        return "Não pode votar"


voto = pode_votar(19)

print(voto)


# Exercício 6

# Você tem uma lista de dicionários, onde cada dicionário representa uma pessoa com nome e idade.
# Use a função sorted() com uma expressão lambda como chave (key) para ordenar a lista de pessoas da mais nova para a mais velha.

pessoas = [
    {'nome': 'Carla', 'idade': 32},
    {'nome': 'Bruno', 'idade': 25},
    {'nome': 'Ana', 'idade': 45},
    {'nome': 'Daniel', 'idade': 22},]

pessoas_ordenadas = sorted(pessoas, key=lambda p: p['idade'])

print('Lista Origimal:')
print(pessoas)
print('\nLista ordenada por idade:')
print(pessoas_ordenadas)


# Exercício 7

# Crie uma função que receba uma lista de números inteiros e retorne um dicionário contendo a contagem de quantos números,
# são pares e quantos são ímpares.

Lista_inteiros = []

for x in range(21):
    if x % 2 == 0:
        print(f'{x} é Par:')
    else:
        print(f'{x} é Impar:')


def funcao_conta_pares_impares(lista_numeros):

    contagem = {'pares': 0, 'impares': 0}

    for x in lista_numeros:
        if x % 2 == 0:
            contagem['pares'] += 1
        else:
            contagem['impares'] += 1

    return contagem


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
resultado = funcao_conta_pares_impares(numeros)
print(
    f'Na lista, há {resultado['pares']} numeros pares e {resultado['impares']} numeros impares')


# Exercício 8

# Crie uma função que receba uma lista de strings (potenciais e-mails) e um parâmetro opcional dominio_desejado (com valor padrão "gmail.com").
# A função deve retornar uma nova lista, usando list comprehension, contendo apenas os e-mails que terminam com o domínio desejado.

def filtra_emails_por_dominios(emails, dominio_desejado='gmail.com'):

    return [email for email in emails if email.endswith(f'@{dominio_desejado}')]


lista_emails = ['contato@gmail.com', 'vendas@yahoo.com',
                'suporte@gmail.com', 'admin@outlook.com']

emails_gmail = filtra_emails_por_dominios(
    lista_emails, dominio_desejado='gmail.com')
print(f'Emails do Gmail:{emails_gmail}')

# exemplo sem comprehension


def filtra_emails_por_dominios(emails, dominio_desejado='gmail.com'):

    emails_filtrados = []  # 1. Cria a lista para guardar os resultados

    for email in emails:
        # 2. Verifica se o email termina com o domínio (ex: @gmail.com)
        if email.endswith(f'@{dominio_desejado}'):
            emails_filtrados.append(email)  # 3. Adiciona à lista

    return emails_filtrados  # 4. Retorna a lista completa


lista_emails = ['contato@gmail.com', 'vendas@yahoo.com',
                'suporte@gmail.com', 'admin@outlook.com']

# Agora a variável abaixo receberá a lista de retorno
emails_gmail = filtra_emails_por_dominios(
    lista_emails, dominio_desejado='gmail.com')

print(f'Emails do gmail: {emails_gmail}')


# Exercício 9

# Dada uma lista de frases, use a função map() em conjunto com uma expressão lambda para criar uma nova lista onde cada frase,
# é convertida para letras maiúsculas e tem a palavra "PYTHON" anexada ao final.

frases = ['Aprendendo a programar', 'Dominando estruturas de dados',
          'Funcoes anonimas são poderosas']

# map() aplica a funcao lambda a cada item da lista 'frases'

frases_modificadas = list(map(lambda f: f.upper() + ' EM PYTHON', frases))

for frase in frases_modificadas:
    print(frase)


# Exercício 10

# Crie um jogo onde o computador escolhe um número secreto entre 1 e 20.
# O jogador tem 5 tentativas para adivinhar. A cada tentativa, o programa informa se o palpite foi muito alto ou muito baixo.
# Se o jogador acertar, o loop deve ser interrompido com uma mensagem de vitória.


def jogo_adivinhacao():

    numero_secreto = random.randint(1, 20)

    tentativas = 5

    print('Adivinhe o numero secreto entre 1 e 20. Voce tem 5 tentativas!')

    while tentativas > 0:
        print(f'\nVoce tem {tentativas} tentativas(s) restantes(s).')

        palpite = int(input('Digite seu palpite:'))

        if palpite == numero_secreto:
            print('Parabens! Voce acertou!')
            break

        elif palpite < numero_secreto:
            print('Muito baixo!')

        else:
            print('Muito alto')

        tentativas -= 1

    else:
        print(f'\nFim de jogo! O numero secreto era {numero_secreto}')
        print (f'\nTente outra vez !!! ')


jogo_adivinhacao()
