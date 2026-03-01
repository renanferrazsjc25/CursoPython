# Variaveis Globais sao acessadas fora da função

saudação = 'Ola, Mundo!'
nome = 'Aluno Dsa Renan'

# Função
# Variaveis Locais sao acessadas dentro da função


def minha_função_dsa():
    nome = 'Ana'
    print(f'\nDentro da função: {nome}')
    print(f'\nAcessando variavel global de dentro da função: {saudação}')


minha_função_dsa()

print(f'\nfora da função: {saudação}')
print(f'\nfora da função: {nome}')
