volta = 0
while True:
    n = int(input("Digite um número:"))
    if volta == 0:
        maior = n;
        menor = n;
    else:
        if n > maior:
            maior = n;
        if n < menor:
            menor = n;
    volta += 1;
    # Verifica se o programa deve continuar
    continuar = str(input("Deseja continuar?[S/N]:")).upper()[0]
    while continuar not in "SN":
        continuar = str(input("ERRO!!, Deseja continuar?[S/N]:")).upper()[0]
    if continuar == 'N':
        break
print("Programa Finalizado!")
print("Maior número:",maior)
print("Menor número:",menor)