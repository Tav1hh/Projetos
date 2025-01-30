# Verifica a velocidade do veiculo e diz se ele foi multado
v = int(input("Velocidade do Veiculo: "))
if v > 80:
    multa = (v - 80) * 7
    print("Você foi MULTADO em R${:.2f}".format(multa))
print("Dirija com segurança..")