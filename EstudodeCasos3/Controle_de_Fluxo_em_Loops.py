# As instruções break e continue alteram o fluxo de execução de um loop.

# Break

# A instrução break para a execução do loop imediatamente.

# Lista

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'\nBuscando pelo numero 5...')

for num in numero:
    if num == 9:
        print(f'Numero 9 encontrado!')
        break
    print(f'Verificando {num}...')


# Continue

# A instrução continue pula a iteração atual e continua com a próxima.

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'\nImprimindo apenas os numeros impares:')

for numero in range(1, 100):
    if numero % 2 == 0:
        continue  # Pula para a próxima iteração se o número for par
    print(numero, end=" ") #argumento (end=) para imprimir na mesma linha
