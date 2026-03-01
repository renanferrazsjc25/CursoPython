from random import randint

for x, y in enumerate(range(1, 8), start=1):
    print(f'{x} Gol da Alemanha')

print(f'Brasil fez apenas 1 gol, que VERGONHA!')


sexo = ('lado', 'quatro', 'papai', 'quicando', 'chupando')

for x in sexo:
    if x.startswith('q'):
        print(f'Eu amo comer a minha mulher de :{x}')


print(f'Mas ela nao quer me dar')

cardapio = ['Arroz', 'Feijao', 'Carne', 'Camarao',
            'Bolinho de Bacalhau', 'Feijoada', 'Bife Acebolado']

x = cardapio.pop(0)

while x != 'Bife Acebolado':
    print('Esse item nao é Bife Acebolado')
    x = cardapio.pop(0)
if x == 'Bife Acebolado':
    print(f'Achei a Bife Acebolado')
