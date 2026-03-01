# Operadores Logicos

tem_dinheiro = True
tem_tempo = False

# Operador and (e): Ambas as variaveis precisam ser verdadeiros

print(f'O cliente pode viajar? {tem_dinheiro and tem_tempo}')

# Operador or (ou): pelo menos uma das variaveis precisam ser verdadeiro

print(f'O cliente pode viajar? {tem_dinheiro or tem_tempo}')

# Operador not (não): inverte o valor booleano, transforma True em False e False em True

print(f'O cliente pode viajar? {tem_dinheiro and not tem_tempo}')

# Operador not exemplo 2:

banda = input('Qual melhor banda do mundo? ')

if not banda == 'rush':
    print('Herege!')
else:
    print('Correto, é o Rush!')
