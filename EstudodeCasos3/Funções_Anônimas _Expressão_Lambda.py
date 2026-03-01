# São pequenas funções anônimas definidas com a palavra-chave lambda.

# Uma função lambda que dobra um número

# exemplo 1 - usando lambda

def dobro(x): return x * 2


print(f'O dobro de 7 é:{dobro(7)}')

# Exemplo 2 - usando uma funçao comum


def dobro(x):
    return x * 2


print(f'O dobro de 7 é:{dobro(7)}')

# A grande vantagem de usar expressões lambda em Python é a simplicidade e concisão para criar funções pequenas, temporárias e sem nome (anônimas).

# Normalmente, quando você precisa de uma função, define com def. Mas às vezes a função é muito simples e usada apenas uma vez,
# dentro de outra operação (como um map, filter ou sorted). Nesses casos, a lambda evita código extra e deixa o fluxo mais direto.

# Você pode combinar uma expressão lambda com a função map() para aplicar uma operação a cada elemento da lista, por exemplo.

# Lista de números

numeros = [1, 2, 3, 4, 5]


# Lambda que retorna o quadrado de cada elemento
quadrados = list(map(lambda x: x ** 2, numeros))

print(quadrados)

# Aqui:

# lambda x: x**2 define uma função anônima que calcula o quadrado.

# map() aplica essa função a cada elemento da lista.

# list() converte o resultado do map (um iterador) de volta para lista.

# Também daria para fazer com list comprehension, mas aí não seria lambda

# Lista de numeros

numeros = [1, 2, 3, 4, 5, 6]

# Primeiro calculamos os quadrados com map + lambda
quadrados = list(map(lambda x: x ** 2, numeros))

# Agora filtramos apenas os pares com filter + lambda
quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))
quadrados_impares = list(filter(lambda x: x % 2 != 0, quadrados))
print('Quadrados:', quadrados)
print('Quadrados pares:', quadrados_pares)
print('Quadrados impares:', quadrados_impares)
