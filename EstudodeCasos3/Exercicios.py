# Exercicio 1

# Escreva uma função que receba os valores de três lados de um triângulo e o classifique como "Equilátero" (todos os lados iguais),
# "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).

def classifica_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return 'triangulo_equilatero'

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return 'triangulo isosceles'

    else:
        return 'triangulo escaleno'


print(f'Lados 1,1,1: {classifica_triangulo(1, 1, 1)}')
print(f'Lados 1,2,1: {classifica_triangulo(1, 2, 1)}')
print(f'Lados 1,2,3: {classifica_triangulo(1, 2, 3)}')

# Exercicio 2

# Escreva uma função que recebe um número inteiro e exibe a tabuada de multiplicação desse número, do 1 ao 10.


def exibe_tabuada(numero):
    print(f'Tabuado do {numero}')

    for x in range(1, 11):
        resultado = numero * x
        print(f'{numero} x {x} = {resultado}')


exibe_tabuada(7)


# Exercício 3

# Você recebeu um dicionário com os nomes dos alunos e suas respectivas notas.
# Escreva uma função que calcula a média da turma e retorna uma lista com os nomes dos alunos que tiveram nota acima da média.


def alunos_com_media_alta(turma):
    if not turma:
        return 'Dicionario de turma vazio'

    soma_notas = sum(turma.values())
    media = soma_notas / len(turma)

    print(f'A media da turma é: {media:.2f}')

    aprovados = []

    for aluno, nota in turma.items():
        if nota > media:
            aprovados.append(aluno)

    return aprovados


notas_da_turma = {'Ana': 8.5,
                  'Bob': 6.0,
                  'Cris': 9.5,
                  'Pedro': 7.0,
                  'Marcelo': 5.5
}


print(f'Alunos com media alta: {alunos_com_media_alta(notas_da_turma)}')
