# Tuplas

# é uma coleção ordenada e imutável de itens, similar a uma lista, mas que não pode ser alterada após sua criação, sendo definida por parênteses ()

coordenadas = (10.0, 30.5)
print(f'tuplas de coordenadas: {coordenadas}')

# Acessando um item pelo indice

print(f'coordenadas x: {coordenadas[0]}')
print(f'coordenadas y: {coordenadas[1]}')
coordenadas[0]

# Tuplas sao uteis para dados que nao devem ser alterados, como meses do ano, coordenadas, e etc

dias_da_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta','Sexta', 'Sexta', 'Sabado', 'Domingo')

print(f'O primeiro dia da semana é :{dias_da_semana[0]}')

# 1. Criando uma tupla com diferentes tipos de dados
# Note que usamos parênteses ()
veiculo = ("Ford", "Mustang", 1964, "Prata")

# 2. Acessando itens pelo índice (começa em 0)
print(f"Marca: {veiculo[0]}")
print(f"Ano: {veiculo[2]}")

# 3. Tuplas permitem "desempacotamento" (unpacking)
marca, modelo, ano, cor = veiculo
print(f"O modelo é {modelo} e a cor é {cor}")

# 4. Verificando o comprimento da tupla
print(f"A tupla tem {len(veiculo)} elementos")

# 5. Demonstração de Imutabilidade
try:
    veiculo[1] = "Fiesta"
except TypeError as e:
    print(f"\nErro de imutabilidade: {e}")
    # Isso acontece porque você não pode alterar um item após a criação