# Sistema
while True:
    print("\033[31m="*20)
    print("\033[33m1 - Somar")
    print("\033[33m2 - Subtrair")
    print("\033[33m3 - Dividir")
    print("\033[33m4 - Multiplicar")
    print("\033[31m="*20)
    opt = int(input("\033[mOpção: "))

    if opt == 1:
        print("Números Somados!")
    elif opt == 2:
        print("Números Subtraidos!")
    elif opt == 3:
        print("Números Divididos!")
    elif opt == 4:
        print("Números Múltiplicados!")
    else:
        print("OPÇÂO INVALIDA!")