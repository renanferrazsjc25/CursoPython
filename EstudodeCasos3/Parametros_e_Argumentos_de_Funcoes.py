# Parâmetros e Argumentos de Funções

# Diferentes formas de passar informações para as funções.

# Argumentos posicionais

def dsa_apresentaçao(nome, idade):
    print(f'Nome: {nome}, idade: {idade}')


dsa_apresentaçao('Ana', 25)

# Chamando a Funçao (CUIDADO), definir corretamente a ordem dos parametros

dsa_apresentaçao(25, 'Ana')

# Argumentos Nomeados

dsa_apresentaçao(idade = 30, nome = 'Bob')

# Parametros com valores padrao (DEFAULT)

def dsa_saudaçao_completa(nome, saudaçao= 'Ola'):
    print (f'{saudaçao}, {nome}!')


dsa_saudaçao_completa('Maria')