# Um Programa que lé um número real e mostra sua porção inteira
from math import trunc
n = float(input("Digite um número real: "))
print("Sua porção inteira é {}".format(trunc(n)))