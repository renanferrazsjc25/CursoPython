# As estruturas de repetição (for e while) são usadas para executar um bloco de código várias vezes

# Loop for

# O loop for é usado para iterar sobre uma sequência (como uma lista, tupla, dicionário, conjunto ou string).

# Defina uma lista

frutas = ['maça', 'banana', 'cereja']

print('frutas disponiveis')

for fruta in frutas:
    print(f'- {fruta}')

# Defina uma Tupla


cores = ('vermelho', 'azul', 'amarelo')

print('Cores:')

for cor in cores:
    print(f'- {cor}')


# Defina um Dicionario

formacoes_dsa = {
    "Formação Cientista de Dados": 6,
    "Formação Analista de Dados": 4,
    "Formação Engenheiro de Dados": 5
}

for chave, valor in formacoes_dsa.items():
    print(chave, ':', valor)

usuario = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "email": "joao.silva@exemplo.com"
}

for chave, valor in usuario.items():
    print(chave, ':', valor)


# Exemplo com a função range()

print(f'\nContagem ate 5:')

for numero in range(6):
    print(numero)
