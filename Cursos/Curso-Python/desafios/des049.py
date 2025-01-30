# Refaça o Desafio 009, mostrando a tabuada de um número que o usuario escolher, só que agora utilizando um Laço for. 
n = int(input("Digite um número para ver a sua tabuada: "))

for c in range(1,11):
    print("{} x {} = {}".format(n,c,n*c))