# Loop while

# O loop while executa um bloco de código enquanto uma condição for verdadeira.#

# Exemplo1

contador = 5


print("Contagem regressiva:")


while contador > 0:
    print(contador)
    contador -= 1  # -=1 seria a mesma coisa de contador = contador -1, apenas uma forma de simplificar

# Exemplo 2

#  Valor da variavel nao passa na condição

contador = 1

print('Contagem Regressiva')

while contador > 1:
    print(contador)
    contador -= 1
