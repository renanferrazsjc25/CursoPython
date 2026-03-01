# Em Python, *args e **kwargs são formas de tornar funções mais flexíveis,
#  permitindo receber um número variável de argumentos sem precisar definí-los todos na assinatura da função.

# *args – argumentos posicionais variáveis

# O asterisco (*) antes do nome indica que a função pode receber qualquer quantidade de argumentos posicionais.
# Esses valores chegam dentro da função como uma tupla.

# **kwargs – argumentos nomeados variáveis

# Os dois asteriscos (**) indicam que a função pode receber qualquer quantidade de argumentos nomeados (chave e valor).
# Esses valores chegam dentro da função como um dicionário.

# Argumentos de tamanho variável (*args)

def dsa_soma_numeros(*args):
    total = 0

    for numero in args:
        total += numero

    return total


print(f"Soma dos Números: {dsa_soma_numeros(1, 2, 3, 4, 5, 29)}")
print(f"Soma dos Números: {dsa_soma_numeros(1, 2, 3)}")
print(f"Soma dos Números: {dsa_soma_numeros(10, 400, 0.3, 120)}")

# Argumentos de tamanho variável (**kwargs)

# Exibe informações passadas como pares chave-valor


def dsa_exibe_info_pessoa(**kwargs):

    print("\nInformações da Pessoa:\n")

    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")


dsa_exibe_info_pessoa(nome='Carla',
                      profissao='Analista Python',
                      hobby='Leitura')


dsa_exibe_info_pessoa(nome="Bob",
                      profissao="Cientista de Dados")
