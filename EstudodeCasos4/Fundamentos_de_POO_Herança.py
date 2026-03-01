# Fundamentos de POO - Herança

# A herança permite que uma nova classe (chamada de classe filha ou subclasse) herde atributos e métodos de uma classe existente
# (chamada de classe pai ou superclasse). Isso promove a reutilização de código.

# Vamos criar uma classe Veiculo genérica e fazer Carro e Moto herdarem dela.#

# Classe Pai (Superclasse)
class Veiculo:
    # Construtor (criado para inicializar atributos da classe), (atributos sao dados que representamos sobre determinado objeto)
    # Método construtor da classe pai 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.modelo} foi ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O {self.modelo} foi desligado.")

# Classe Filha (Subclasse) que herda de Veiculo
class Carro(Veiculo):

    # Método construtor da classe filha
    def __init__(self, marca, modelo, portas):
        # super().__init__() chama o construtor da classe pai
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_info_carro(self):
        print(f"Carro: {self.marca} {self.modelo}, Portas: {self.portas}")

# Outra Classe Filha
class Moto(Veiculo):

    # Método construtor da classe filha
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Este método é específico da classe Moto
    def empinar(self):
        print(f"A moto {self.modelo} está empinando! Cuidado!")

    def exibir_info_moto(self):
        print (f'Moto: {self.marca} {self.modelo} {self.cilindradas}')


meu_carro = Carro("Volkswagen", "Golf", 4)

minha_moto = Moto("Honda", "CB 500", 500)

meu_carro.exibir_info_carro()

meu_carro.ligar() # Método herdado de Veiculo

minha_moto.exibir_info_moto()

minha_moto.ligar() # Método herdado de Veiculo

minha_moto.empinar() # Método específico de Moto

# Exemplo 2

class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chama o construtor da classe pai (Animal)
        super().__init__(nome) 
        self.raca = raca

meu_pet = Cachorro("Rex", "Labrador")

print(f"Nome: {meu_pet.nome}")  # Atributo vindo da classe Animal
print(f"Raça: {meu_pet.raca}")  # Atributo definido na classe Cachorro