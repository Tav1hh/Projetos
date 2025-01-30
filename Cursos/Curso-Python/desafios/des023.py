# Lé um número de 0 a 9999 e mostra na tela a unidade, dezena, centena e milhar
n = " ".join(str(input('Número: '))).split()
print("Únidade:", n[3])
print("Dezena:", n[2])
print("Centena:", n[1])
print("Milhar:", n[0])