# Lé 3 números diz qual é o maior e qual o menor
n1 = int(input("Número 1:"))
n2 = int(input("Número 2:"))
n3 = int(input("Número 3:"))

lista = [n1,n2,n3]
lista.sort()

print("Maior:",lista[-1])
print("Menor:",lista[0])