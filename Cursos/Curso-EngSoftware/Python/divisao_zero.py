while True:
    try:
        a = int(input('Digite um número:'))
        if a == 999:
            break
        b = int(input('Digite outro número: '))
        print(f'O resultado da divisão é {a/b}')
    except:
        print('Entre com um valor válido.')

print('Programa Finalizado.')
    