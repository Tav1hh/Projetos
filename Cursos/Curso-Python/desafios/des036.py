# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, o Programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo sera negado.
print("\033[33m=\033[m"*20)
valorCasa = float(input("Qual o Valor da casa? "))
salario = float(input("Qual o seu salário? "))
anosEmprestimo = int(input("Em quantos anos? "))
print("\033[33m=\033[m"*20)

mensalidade = valorCasa/(anosEmprestimo*12)
margem = 30*salario/100
anos = valorCasa/margem/12+1

if mensalidade > margem:
    print("Emprestimo \033[31mNEGADO!\033[m")
    print("O recomendado seria parcelar em {:.0f} anos".format(anos))
else:
    print("Emprestimo \033[32mAPROVADO!\033[m")
    print("Valor das parcelas: \033[33mR${}\033[m".format(mensalidade))

