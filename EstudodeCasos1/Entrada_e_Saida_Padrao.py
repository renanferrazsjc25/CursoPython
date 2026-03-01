# Saida de dados com Print
from datetime import date
nome = 'Maria Luiza'
idade = 4
cidade = 'São Jose dos Campos'

print(f'Ola, meu nome é {nome}, tenho {idade} anos de idade, e moro em {cidade}')

# Formatando numeros

preco = 49.56789
print(f'O preço do produto é R$ {preco:.2f}')

# Entrada de dados com Input

# Pedindo o nome do usario
nome_usuario = input('Qual o seu nome? ')

# Pedindo a idade do usuario (precisa converter para int)
idade_usuario_str = input('Qual a sua idade? ')
idade_usuario_int = int(idade_usuario_str)


# Pega o ano corrente na data definida no sistema operacional da sua maquina

ano_atual = date.today().year

# Processando os dados

ano_nascimento = ano_atual - idade_usuario_int

print(f'\nOla, {nome}!, Bem Vindo (a)')
print(f'\nVoce tem {idade_usuario_int} anos e nasceu aproximadamente em {ano_nascimento}')
