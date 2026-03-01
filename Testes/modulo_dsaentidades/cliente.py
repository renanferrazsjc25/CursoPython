# Modulo da Entidade Cliente

# Define a classe Cliente
class Cliente:

    # Metodo construtor que inicializa os atributos da classe
    def __init__(self, nome: str, cpf: str):
        # Armazena o nome do cliente
        self.nome = nome
        # Armazena o cpf do cliente
        self.cpf = cpf
        # lista para armazenar as contas associadaa ao cliente
        self.contas = []

# Metodo para adicionar uma conta a lista de conta do cliente

def adicionar_conta(self, conta):

    # Insere o objeto conta na lista de contas
    self.contas.append(conta)

# Metodo Especial que define a representação em string do objeto

def __str__(self):
    # Retorna uma string formatada com nome e CPF do cliente
    return f'Cliente: {self.nome} (CPF:{self.cpf})'
