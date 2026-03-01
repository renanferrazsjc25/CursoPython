# Poliformismo significa "muitas formas". Em POO, refere-se a capacidade de um metodo se comportar de maneiras diferentes para diferentes objetos.

# Um exemplo classico é quando classes filhas sobrescrevem (redefinem) um metodo da classe pai.

# Vamos criar um metodo exibir_detalhes na classe Veiculo e sobrescreve-lo na classe filha.

# Cria Super Classe

class Veiculo:
    # Construtor (criado para inicializar atributos da classe), (atributos sao dados que representamos sobre determinado objeto)
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f'Veiculo Generico: {self.marca} {self.modelo}')

# Cria a Subclasse


class Carro(Veiculo):

    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    # Sobrescrevendo o metodo da classe pai
    def exibir_detalhes(self):
        print(f'Carro: {self.marca} {self.modelo} | Portas: {self.portas}')

# Cria a Subclasse


class Moto(Veiculo):

    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Sobrescrevendo o metodo da classe pai
    def exibir_detalhes(self):
        print(
            f'Moto: {self.marca} {self.modelo} | Cilindradas: {self.cilindradas}')


# Lista de Veiculos de diferentes tipos
veiculos = [Carro('Toyota', 'Corolla', 4),
            Moto('Yamaha', 'MT-07', 700),
            Veiculo('Caloi', 'Ceci')
]


# O mesmo metodo se comporta de forma diferente para cada objeto

for v in veiculos:
    v.exibir_detalhes() # Poliformismo em ação