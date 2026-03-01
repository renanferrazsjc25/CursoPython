# Operadores Aritmeticos

a = 10
b = 3

soma = a + b
subtração = a - b
multiplicação = a * b
# A divisão com uma barra sempre resulta em um resultado Float, ou seja ex: 3.33
divisão = a / b
# a divisão com duas barras sempre resulta em um resultado Integer, ou seja elimina a parte decimal
divisão_inteira = a // b
modulo = a % b  # Pega o valor restante da divisão, ou seja ex: 10 / 3 = 3.33, o modulo pega o valor restate no caso 1
potencia = a ** b

print(f'{a} + {b} = {soma}')
print(f'{a} - {b} = {subtração}')
print(f'{a} * {b} = {multiplicação}')
# usar :.2f, faz com que as casas decimais após a virgula sejam apenas 2, ou seja ex: 3.33
print(f'{a} / {b} = {divisão:.2f}')
print(f'{a} // {b} = {divisão_inteira}')
print(f'{a} % {b} = {modulo}')
print(f'{a} ** {b} = {potencia}')
