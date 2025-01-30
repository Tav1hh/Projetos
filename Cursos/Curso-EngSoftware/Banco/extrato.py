from datetime import *
class Extrato:
    def __init_(self):
        self.transacoes = [1,2,3,4,]

    def extrato(self, numeroconta):
        print(f'Extrato: {numeroconta} \n')
        for p in self.transacoes:
             print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3]("%d/%b/%b")}")