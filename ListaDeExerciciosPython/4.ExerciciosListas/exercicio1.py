# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

def ArrayString2Int(arrayString, arrayInt): #arrayString é a lista a ser convertida, arrayInt é onde irão os objetos convertidos.
    while len(arrayInt) != len(arrayString):
        v = 0
        conversor = arrayInt.append(int(arrayString[v]))
        v += 1
    pass

listastr = input("Digite 5 números inteiros separados por vírgula: ").split(",")

while len(listastr) < 5 or len(listastr) > 5:
    print("Por favor, digite apenas 5 números")
    listastr=input("Digite 5 números inteiros separados por vírgula: ").split(",")

listaint = []

ArrayString2Int(listastr,listaint)

print("\nA lista de números inteiros é {}".format(listaint))