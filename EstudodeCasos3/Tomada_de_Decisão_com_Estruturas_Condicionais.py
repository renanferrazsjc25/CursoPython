# As estruturas condicionais (if, elif, else) permitem que o programa execute diferentes blocos de código com base em certas condições.

# Exemplo 1

nota = 6.9

if nota >= 7.0:
    print('Aprovado!')
else:
    print('Reprovado!')

# Exemplo 2

idade = 66

if idade < 18:
    print('Voce é menor de idade')

elif idade >= 18 and idade < 65:
    print('Voce é um adulto')

else:
    print('Voce é um idoso')
