#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def ArrayString2Float(arrayString, arrayFloat): #arrayString é a lista a ser convertida, arrayInt é onde irão os objetos convertidos.
    while len(arrayFloat) < len(arrayString):
        arrayFloat.append(float(arrayString[len(arrayFloat)]))
    pass

def ArraySigma(numberArrayToReduce):
    sigma = 0
    contador=0
    while contador < len(numberArrayToReduce):
        sigma = numberArrayToReduce[contador] + sigma
        contador = contador + 1
    return sigma

listaNotasStr = input("Digite 4 notas separadas por vírgula: ").split(",")
listaNotasFloat = []

while len(listaNotasStr) != 4:
    print("Por favor, digite apenas 4.")
    listaNotasStr = input("Digite 4 notas separadas por vírgula: ").split(",")

ArrayString2Float(listaNotasStr,listaNotasFloat)

divisor = len(listaNotasFloat)
media = ArraySigma(listaNotasFloat) / divisor

print("\nA média das notas {} foi de {}.".format(listaNotasFloat, media))