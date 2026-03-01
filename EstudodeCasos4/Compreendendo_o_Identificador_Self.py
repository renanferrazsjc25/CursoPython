# Uma forma didática de compreendero self é pensar que ele funciona como o “cartão de identificação”
# do próprio objeto que está sendo criado ou manipulado.
# 
# Quando você escreve a classe Cliente e depois cria,por exemplo:
# 
# c1 = Cliente("Maria", "123.456.789-00")

# c2 = Cliente("João", "987.654.321-00")

# Python precisa de uma forma de saber qual objeto (c1 ou c2) está sendo modificado ou acessado dentro dos métodos da classe.

# Esse papel é do self.

# No  método  __init__,  o  parâmetro  self  representa  a  instância  atual  da  classe.

# Então, quando você faz:

# self.nome = nome

# Python entende: “o atributo nome deste objeto específico (como c1 ou c2), vai receber o valor passado na criação”.

# Assim, cada objeto guarda seus próprios dados,sem confusão entre eles.

# Resumindo de forma didática:

# •O self é sempre uma referência ao objeto que está chamando o método.

# •É  ele  que  permite  que  cada  instância  da  classe  tenha  seus  próprios  atributos  e comportamentos.

# •Sem o self, o Python não teria como distinguir se você está se referindo ao cliente c1 ou ao cliente c2.

class identificação:
    # Construtor (criado para inicializar atributos da classe), (atributos sao dados que representamos sobre determinado objeto)
    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf

    def exibir_info(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}')


c1 = identificação('Joao', '123.456.789-00')

c1.exibir_info()

c2 = identificação('Maria', '987.654.321-00')

c2.exibir_info()
