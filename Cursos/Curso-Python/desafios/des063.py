# Escreva um programa que leia um número 'n' inteiro e msotre na tela os 'n' primeiros elementos de uma Sequencia Fibonacci.
# Ex: 0,1,1,2,3,5,8
num = int(input("Digite um número: "))

n = 0;
fib = 0;
ant = 1;
print("0",end="")
while n < num:
    fib = ant+fib
    print(" >",fib,end="")
    ant = fib - ant
    n += 1