n = q = t = 0
while True:
    n = int(input("Digite um número [999/stop]: "))
    if n == 999:
        break
    q += 1;
    t += n;
print("Total da Soma:",t)
print("Quantidade de números:",q)