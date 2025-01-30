from math import sqrt
a = input('Valor de a: ')
b = input('Valor de b: ')
c = input('Valor de c: ')

a = 1
b = 5
c = 6

d = b**2 -4*a*c
d = sqrt(d)
r2 = (-b + d)/2
r1 = (-b - d)/2

print(f'as raizes sâo {r1} e {r2}')