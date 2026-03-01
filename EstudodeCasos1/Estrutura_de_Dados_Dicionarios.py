# Dicionarios

# é uma estrutura de dados que permite armazenar dados em pares. Chamamos cada par de dados de par chave:valor, usamos {}

aluno = {
    'nome': 'Bob',
    'idade': 22,
    'curso': 'Python',
    'aluno_ativo': True
}
print(f'Dicionario do Aluno: {aluno}')

# Acessando um valor pela sua chave

print(f'Nome do aluno: {aluno['nome']}')
# .get para acessar valores de dicionários de forma segura, retornando None ou um valor padrão se a chave não existir, evitando erros
print(f'Curso: {aluno.get('curso')}')

# Adicionando um novo par chave-valor

aluno['cidade'] = 'São Paulo'
print(f'Dicionario Atualizado:\n{aluno}')

# \n comando usado para uma nova linha

print('Ola, Mundo!')
print('Ola, \nMundo!')

# Modificando um valor existente

aluno['idade'] = 23
print(f'idade atualizada:{aluno['idade']}')

# Removendo um valor

del aluno['aluno_ativo']
print(f'Dicionario apos remover a chave"ativo": \n{aluno}')
