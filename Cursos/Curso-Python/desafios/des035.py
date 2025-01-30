# Lé 3 retas e diz se elas podem formar um triangulo
r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))
lista = [r1,r2,r3]
lista.sort()
if lista[0] + lista[1] < lista[2]:
    print("Não podem formar um triangulo!")
else:
    print("Podem formar um triangulo!")