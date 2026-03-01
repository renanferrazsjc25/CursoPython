# Conteúdo do arquivo dsaprincipal.py

# Importa o módulo inteiro
import Modulo_Criado

# Usa a função e a variável do módulo
mensagem = Modulo_Criado.dsa_saudacao("Mundo")
print(mensagem)
print(f"O valor de PI do nosso módulo é: {Modulo_Criado.PI}")

# Outra forma: importando itens específicos
from Modulo_Criado import dsa_saudacao, PI

mensagem_direta = dsa_saudacao("Aluno DSA")
print(mensagem_direta)
print(f"Valor de PI importado diretamente: {PI}")