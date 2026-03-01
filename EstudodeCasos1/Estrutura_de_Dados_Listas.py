# Listas

# Sao colecoes ordenadas e mutaveis de itens, que pode ser modificada, usamos colchetes [] para criar uma lista

frutas = ['maça', 'banana', 'laranja', 'abacaxi']
print(f'Lista de Frutas: {frutas}')

# Acessando um item pelo indice

print(f'A primeira fruta é: {frutas[0]}')
print(f'A ultima fruta é: {frutas[-1]}') # podemos usar -1 para buscar o ultimo item da lista

# Removendo um item

frutas.remove('laranja')
print (f'Lista apos remover "laranja":{frutas}')

# Adicionando um item no final da lista

frutas.append('uva')
print (f'Lista apos adicionar "uva" {frutas}')

# 1. Criando uma lista de preços
precos = [10.50, 45.00, 100.00, 25.90, 150.00]

# 2. Modificando um item (o preço do primeiro produto subiu)
precos[0] = 12.00

# 3. List Comprehension: Criando uma nova lista com 10% de desconto
# Isso é muito usado em Python para transformar dados rapidamente
precos_com_desconto = [p * 0.9 for p in precos]

# 4. Filtragem: Selecionando apenas produtos "Premium" (acima de 50 reais)
produtos_premium = [p for p in precos if p > 50]

# 5. Operações de resumo
print(f"Lista original atualizada: {precos}")
print(f"Preços com desconto: {precos_com_desconto}")
print(f"Produtos acima de R$ 50: {produtos_premium}")
print(f"Valor total da compra: R$ {sum(precos):.2f}")