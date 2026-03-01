# Estas estruturas são consideradas construtores sintáticos (syntactic constructs) ou, mais formalmente,
# expressões de compreensão (comprehension expressions).

# Na documentação oficial Python, os nomes são:

# List comprehension → expressão que gera listas.

# Set comprehension → expressão que gera conjuntos.

# Dict comprehension → expressão que gera dicionários.

# Generator expression → expressão que gera iteradores (e pode ser convertido em tupla, lista, etc.).

# Ou seja, o termo técnico mais amplo é comprehension: uma forma mais curta e expressiva de construir coleções (ou geradores)
# a partir de iteráveis com filtros e transformações aplicadas inline.

# Criando uma Lista de quadrados dos números de 0 a 9

quadrado = [x ** 2 for x in range(10)]

print(f'\nQuadrados de 0 a 9: {quadrado}')
print(type(quadrado))

# Criando uma Lista de numeros pares de 0 a 20

pares = [x for x in range(21) if x % 2 == 0]

print(f'Numeros pares de 0 a 20: {pares}')

# Criando uma Dicionario com numeros e seus quadrados

quadrados_dict = {x: x ** 2 for x in range(6)}

print(quadrados_dict)

print(type(quadrados_dict))

# Conjunto de quadrados (sem valores repetidos)

quadrados_set = {x ** 2 for x in [1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7]}

quadrados_set_ordem = sorted(quadrados_set)
print(quadrados_set_ordem)

# Generator expression (não é tupla ainda), mas conseguimos gerar com generator

gen = (x ** 2 for x in range(6))

print(gen)

quadrados_tuple = tuple(x ** 2 for x in range(6))

print(quadrados_tuple)
print(type(quadrados_tuple))
