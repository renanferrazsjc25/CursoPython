# Convertendo de String para numero Integer

numero_em_texto = "123"
numero_inteiro = int(numero_em_texto)
print(f'String {numero_em_texto}, para inteiro: {numero_inteiro}, {type(numero_inteiro)}')

# Convertendo de String para numero Float

numero_decimal_em_texto = '45.67'
numero_float = float(numero_decimal_em_texto)
print(f'String {numero_decimal_em_texto}, para Float: {numero_float}, {type(numero_float)}')

# Convertendo de Numeros para String

idade = 25
idade_texto = str(idade)
print(f'Inteiro {idade}, para String {idade_texto}, {type(idade_texto)}')

# Convertendo entre Estruturas de Dados

lista_com_duplicatas = [1, 2, 2, 3, 3, 4, 4, 4, 6]
conjunto_unico = set(lista_com_duplicatas)
lista_sem_duplicatas = list(conjunto_unico)
print(f'\nLista Original: {lista_com_duplicatas}')
print(f'\nConvertida para Conjunto (remove duplicatas): {conjunto_unico}')
print(f'\nConvertida de volta para Lista: {lista_sem_duplicatas}\n')


