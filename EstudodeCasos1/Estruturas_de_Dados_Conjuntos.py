# Conjuntos (Sets)

# são coleções não ordenadas e de elementos únicos, criados com chaves {} ou set(),
# ideais para remover duplicatas e realizar operações matemáticas de conjuntos como união,
# interseção e diferença, sendo úteis para checagem eficiente de pertencimento,
# embora seus itens devam ser imutáveis (números, strings, tuplas) e não possam ser acessados por índice.

numeros = {1, 2, 3, 4, 2, 3, 5}
# itens duplicados foram removidos automaticamente
print(f'Conjunto de numeros (sem duplicatas): {numeros}')

# Adicionando um item

numeros.add(6)
print(f'Apos adicionar o valor 6:{numeros}')

# Removendo um item

numeros.remove(2)
print(f'Apos remover o numero 2: {numeros}')

# Operaçao de Conjuntos

conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Uniao (faz a uniao dos elementos que estao em ambos os conjuntos, removendo as duplicadas)

uniao = conjunto_a.union(conjunto_b)
print(f'Uniao dos conjuntos A e B: {uniao}')

# Interseçao (pega os elementos que estao em ambos os conjuntos)

interseçao = conjunto_a.intersection(conjunto_b)
print(f'Interseçao de A e B: {interseçao}')
