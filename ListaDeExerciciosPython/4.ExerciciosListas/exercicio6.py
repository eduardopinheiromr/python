#6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

def ArraySelfString2Float(arrayString): #O método foi atualizado e deverá ser chamado dentro de uma variável(Podendo ser a própria arrayString)
    arrayFloat = []
    while len(arrayFloat) < len(arrayString):
        arrayFloat.append(float(arrayString[len(arrayFloat)]))
    return arrayFloat

def ArraySigma(numberArrayToReduce):
    sigma = 0
    contador=0
    while contador < len(numberArrayToReduce):
        sigma = numberArrayToReduce[contador] + sigma
        contador = contador + 1
    return sigma

aluno1 = input("Digite as quatro notas do primeiro aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno2 = input("Digite as quatro notas do segundo aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno3 = input("Digite as quatro notas do terceiro aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno4 = input("Digite as quatro notas do quarto aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno5 = input("Digite as quatro notas do quinto aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno6 = input("Digite as quatro notas do sexto aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno7 = input("Digite as quatro notas do sétimo aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno8 = input("Digite as quatro notas do oitavo aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno9 = input("Digite as quatro notas do nono aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")
aluno10 = input("Digite as quatro notas do décimo aluno separadas por vírgula(ex: 7,8.5,10,6): ").split(",")

divisor = len(aluno1)

aluno1 = ArraySigma(ArraySelfString2Float(aluno1)) / divisor
aluno2 = ArraySigma(ArraySelfString2Float(aluno2)) / divisor
aluno3 = ArraySigma(ArraySelfString2Float(aluno3)) / divisor
aluno4 = ArraySigma(ArraySelfString2Float(aluno4)) / divisor
aluno5 = ArraySigma(ArraySelfString2Float(aluno5)) / divisor
aluno6 = ArraySigma(ArraySelfString2Float(aluno6)) / divisor
aluno7 = ArraySigma(ArraySelfString2Float(aluno7)) / divisor
aluno8 = ArraySigma(ArraySelfString2Float(aluno8)) / divisor
aluno9 = ArraySigma(ArraySelfString2Float(aluno9)) / divisor
aluno10 = ArraySigma(ArraySelfString2Float(aluno10)) / divisor

mediaAlunos = [aluno1,aluno2,aluno3,aluno4,aluno5,aluno6,aluno7,aluno8,aluno9,aluno10]
contador = 0
numeroDeAlunos7 = []

while contador < len(mediaAlunos):
    if mediaAlunos[contador] >= 7:
        numeroDeAlunos7.append(mediaAlunos[contador])
        contador += 1
    else:
        contador += 1

print("\n{} alunos tiveram médias maior/igual a 7.".format(len(numeroDeAlunos7)))
