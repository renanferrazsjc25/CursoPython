class Video_Game:

    def __init__(self, marca, modelo, jogadores):
        self.marca = marca
        self.modelo = modelo
        self.jogadores = jogadores

    def exibir_info(self):
        print(f'Meu filho tem: {self.marca}, {self.modelo}, para {self.jogadores} jogadores')


meu_video_game = Video_Game('Sony', 'Playstation 5', 4)

meu_video_game.exibir_info()

# Classe Filha (Subclasse) que herda de Video Game


class Game_Portatil(Video_Game):

    # Método construtor da classe filha
    def __init__(self, marca, modelo, jogadores, portatil):
        # super().__init__() chama o construtor da classe pai
        super().__init__(marca, modelo, jogadores)
        self.portatil = portatil

    def exibir_info_game(self):
        print(f"Minha filha tem: {self.marca} {self.modelo}, Portátil: {self.portatil}")


meu_portatil = Game_Portatil('Nintendo', 'Game Boy', 1, 'Sim')

meu_portatil.exibir_info_game()
