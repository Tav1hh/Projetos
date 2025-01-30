# Um programa que diz se um número é impar ou par
n = int(input("Digite um número: "))
if n%2 == 0:
    print("O número {} é Par".format(n))
else:
    print("O número {} é Impar".format(n))