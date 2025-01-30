# Programa que lé um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians
a = float(input("Digite um angulo: "))

# sen = a*(1/2)/30
# cos = a*(3**0.5/2)/30
# tan = a*(3**0.5/3)/30

sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print("O Seno é {:.2f}".format(sen))
print("O Cosseno é {:.2f}".format(cos))
print("A Tangente é {:.2f}".format(tan))