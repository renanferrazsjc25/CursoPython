# Manipulação de String

frase = ' Aprender Python é muito divertido! '

# Concatenação

nome = 'Maria'
saudação = 'Ola, ' + nome + '!'

print(saudação)

# Tamanho da String

# len() é usado para calcular a quantidade de caracteres em uma string, elementos em uma tupla/lista, numero de chaves em um dicionario
print(f'Tamanho da frase: {len(frase)}')

# Maiusculas ou Minusculas

print(f'Maiusculas: {frase.upper()}')
print(f'Minusculas: {frase.lower()}')

# (strip) para remover espaços em brancos do inicio e do fim

frases_sem_espaços = frase.strip()
print(f"Frase sem espaços: '{frases_sem_espaços}'")

# (replace)para substituir texto

# quando precisar usar aspas dentro de aspas, usar a aspas opostas a do inicio, para que nao de erro de sintaxe
print(f"Substituindo 'divertido' por 'legal': {frases_sem_espaços.replace('divertido', 'legal')}")

# (slicing) é um método de fatiamento, para extrair partes específicas de sequências como strings, listas, tuplas e intervalos

print(frases_sem_espaços)
print(f'O primeiro caractere: {frases_sem_espaços[0]}')
# o indice em python, começa sempre em 0 ex: Maria (0,1,2,3,4,5)
print(f'A palavra "Python": {frases_sem_espaços[9:15]}')
