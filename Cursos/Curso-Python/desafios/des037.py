# Escreva um programa que leia um número inteiro qualquer e peça para o úsuario escolher qual será a Base da Conversão
# 1 - Decimal
# 2 - Octal
# 3 - Hexadecimal
import decimal

print("\033[33m=\033[m"*20)
n = int(input("Digite um número: "))
print("1 - Octal")
print("2 - Hexadecimal")
print("3 - Binario")
opt = int(input("Escolha uma opção: "))
print("\033[33m=\033[m"*20)

if opt == 1:
    print("O número {} na base \033[33mOCTAL\033[m fica {}".format(n,oct(n)[2:]))
elif opt == 2:
    print("O número {} na base \033[33mHEXADECIMAL\033[m fica {}".format(n,hex(n)[2:]))
elif opt == 3:
    print("O número {} na base \033[33mBINARIA\033[m fica {}".format(n,bin(n)[2:]))