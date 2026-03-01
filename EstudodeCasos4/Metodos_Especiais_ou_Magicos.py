# São metodos com nomes que comecam e terminam com duplo sublinhado.
# Eles permitem que seus objetos se comportem como tipos nativos em Python.
# Os mais comuns são init (construtor) e str (representação em string do objeto)

# Cria Classe

class Livro:

    # Construtor (criado para inicializar atributos da classe), (atributos sao dados que representamos sobre determinado objeto)
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # Chamado quando usamos print() ou str() no objeto
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    # Chamado quando usamos len() no objeto
    def __len__(self):
        return self.paginas


# Cria o objeto
livro_dsa = Livro('Deep Learning Book', 'Data Science Academy', 1000)

# O metodo __str__ é chamado aqui
print(livro_dsa)

# O metodo __len__ é chamado aqui
print(f'O livro tem {len(livro_dsa)} paginas.')
