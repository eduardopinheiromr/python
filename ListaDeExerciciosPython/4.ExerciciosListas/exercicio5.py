#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def ArrayString2Int(arrayString, arrayInt): #arrayString é a lista a ser convertida, arrayInt é onde irão os objetos convertidos.
    while len(arrayInt) < len(arrayString):
        arrayInt.append(int(arrayString[len(arrayInt)]))
    pass

numerosInteirosStr = input("Digite 20 números inteiros separados por vírgula(ex: 1,2,3,etc): ").split(",")

while len(numerosInteirosStr) != 20:
    print("\nOps, parece que você digitou alguma coisa errada.")
    numerosInteirosStr=input("\nDigite 20 números inteiros separados por vírgula(ex: 1,2,3,etc): ").split(",")

numerosInteirosInt = []

ArrayString2Int(numerosInteirosStr,numerosInteirosInt)

contador = 0
listaPar = []
listaImpar = []

while contador < len(numerosInteirosInt) -1:
    if numerosInteirosInt[contador] % 2 == 0:
        listaPar.append(numerosInteirosInt[contador])
        contador += 1
    else:
        listaImpar.append(numerosInteirosInt[contador])
        contador += 1

#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

print("\nA lista de números fornecida foi {}.\nOs números par desta lista são {}.\nOs números ímpar desta lista são {}.".format(numerosInteirosInt,listaPar,listaImpar))