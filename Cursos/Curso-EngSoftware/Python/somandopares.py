lista = input('Digite uma sequencia de números: ').split()
pares = 0
impares = 0
n = len(lista)

for i in range(n):
    if eval(lista[i])%2 == 0:
        pares += eval(lista[i])

    else:
        impares += eval(lista[i])


print(f'A soma dos números pares é {pares}')    
print(f'A soma dos números impares é: {impares}')