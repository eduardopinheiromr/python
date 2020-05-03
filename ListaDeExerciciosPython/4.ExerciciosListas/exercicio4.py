#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def SearchChars(stringAVerificar, caracteresAVerificar):
    arrayCharInput=list(stringAVerificar)
    arrayCharVerify=list(caracteresAVerificar)
    arrayVerified=[]
    indiceCI=0
    indiceCV=0

    while indiceCI < len(arrayCharInput):
        if arrayCharVerify[indiceCV] == arrayCharInput[indiceCI]:
            arrayVerified.append(arrayCharVerify[indiceCV])
            indiceCI=indiceCI + 1
            indiceCV=0
        else:
            if indiceCV < len(arrayCharVerify) - 1:
                indiceCV=indiceCV + 1
            else:
                indiceCI=indiceCI + 1
                indiceCV=0
    return arrayVerified

caracteresInseridos = input("\nDigite uma sequência de 10 caracteres(ex: referência, amo vocês!, etc): ").lower()

while len(caracteresInseridos) != 10:
    print("\nPor favor, digite apenas 10 caracteres.")
    caracteresInseridos = input("\nDigite uma sequência de 10 caracteres(ex: referência, amo vocês!, etc): ")

caracteresAVerificar = "BCDFGJKLMNPQRSTVWXZ"
caracteresAVerificar = caracteresAVerificar.lower()

resultado = SearchChars(caracteresInseridos, caracteresAVerificar)

print("\nForam lidas {} consoantes. São elas: {}.".format(len(resultado), resultado))