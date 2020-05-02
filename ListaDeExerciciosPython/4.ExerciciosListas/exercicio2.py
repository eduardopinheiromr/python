#2.Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def ArrayString2Float(arrayString, arrayFloat): #arrayString é a lista a ser convertida, arrayInt é onde irão os objetos convertidos.
    while len(arrayFloat) < len(arrayString):
        arrayFloat.append(float(arrayString[len(arrayFloat)]))
        pass

listaStr = input("Digite 10 números reais separados por vírgula(Ex: 5.42,-15.32, etc): ").split(",")

while len(listaStr) < 10 or len(listaStr) > 10:
    print("Por favor, digite apenas 5 números")
    listaStr=input("Digite 5 números inteiros separados por vírgula: ").split(",")

listaFloat = []

ArrayString2Float(listaStr,listaFloat)

listaFloat.sort(reverse=True)

print("\nA lista de números reais em ordem decrescente é {}".format(listaFloat))