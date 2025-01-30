# Faça um programa que leia um número qualquer e mostre o seu fatorial.abs
num = int(input("Digite um número: "))
res = 1
print("{}! = ".format(num),end="")
while num != 1:
    print(num,end='x')
    res = res * num
    num = num - 1
print("1 = ",res)
