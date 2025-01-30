# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5.0: Reprovado
# média entre 5.0 e 6.9: Recuperação
# média 7.0 ou superior: Aprovado

print("\033[33m=\033[m"*20)
print("Aprovado ou Reprovado?")
print("\033[33m=\033[m"*20)
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
print("\033[33m=\033[m"*20)
media = (nota1 + nota2)/2
if media < 5:
    print("\033[31mReprovado!\033[m")
elif media >= 7:
    print("\033[32mAprovado!\033[m")
else:
    print("\033[33mRecuperação!\033[m")
