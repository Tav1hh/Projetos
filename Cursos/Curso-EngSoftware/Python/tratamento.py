while True:
    try:
        a = int(input('Digite um número: '))
        break
    except ValueError:
        print('Entre com um número valido.')