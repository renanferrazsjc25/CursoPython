# Importando a biblioteca NumPy
import numpy as np

# Imports
import math
import time

# Criando uma lista (vetor) com NumPy de 10 milhões de itens
precos_np = np.random.rand(10_000_000)
type(precos_np)

# Cria uma lista (estrutura de dados padrão em Python Puro)
precos_list = list(precos_np)
type(precos_list)


# Operação com NumPy
t0 = time.time()
desc = precos_np * 0.90
final = desc + 5
raiz = np.sqrt(precos_np)
print("NumPy:", time.time() - t0, "segundos")


# Mesma operação com Python puro
t0 = time.time()
desc = [p * 0.90 for p in precos_list]
final = [p + 5 for p in desc]
raiz = [math.sqrt(p) for p in precos_list]
print("Python puro:", time.time() - t0, "segundos")

# Para 10 milhões de valores, o NumPy normalmente é muito mais rápido. Mas para poucos valores,
# O uso de loops com Python puro pode sair na frente porque o overhead do NumPy pesa mais que o ganho para poucos registros.

# Resumindo:

# Poucos elementos → Loops Python podem ser mais rápidos (overhead do NumPy é maior).

# Muitos elementos → NumPy é muito mais rápido e escalável.

# É pela sua velocidade, que NumPy é amplamente usado em projetos de Ciência de Dados, Machine Learning e IA.
