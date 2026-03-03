# Iterar significa percorrer os elementos de uma coleção de dados

# Defina uma Tupla

# Itera pela tupla e mostra apenas os números pares

numeros = (3, 7, 10, 15, 20)

for num in numeros:
    if num % 2 == 0:
        print(f'{num} é par')

# Defina uma Lista

# Itera pela lista e mostra apenas os nomes que começam com 'A'

nomes = ['Ana', 'Bruno', 'Carlos', 'Amanda', 'Bia']

for nome in nomes:
    if nome.startswith('A'):
        print(f'Nome encontrado com a letra A: {nome}')

# Defina Dicionarios

# Itera pelo dicionário e mostra apenas produtos acima de 20 reais

produtos = {'Arroz': 25,
            'Feijao': 12,
            'Carne': 45,
            'Macarrao': 8
            }

for item, preco in produtos.items():
    if preco > 20:
        print(f'{item} custa {preco} reais (Acima de 20)')

