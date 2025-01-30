# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("Digite um número: "))
lista = [2,3,5,7,11]
for c in range(2,n+1):
    for i in lista:
        if c%i==0:
            break
    else:
        lista.append(c)
print(lista)
if n in lista:
    print("{} é primo".format(n))
else:
    print("{} não é primo..".format(n))
