# Um programa que lé os 2 catetos e mostra o comprimento da hipotenusa
from math import hypot
cat1 = float(input("Cateto 1: "))
cat2 = float(input("Cateto 2: "))

h = hypot(cat1,cat2)
print("A Hipotenusa é {}".format(h))