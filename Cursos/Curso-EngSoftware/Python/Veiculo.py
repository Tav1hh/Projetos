class veiculo:
    def __init__(self,nome,velocidade,km):
        self.nome=nome
        self.velocidade=velocidade
        self.km=km
    
    def capacidade_assentos(self,capacidade):
        print(f'A capacidade maxima de assentos do veiculo {self.nome}, é {capacidade}')

    def imprimir(self):
        print(f'A Velocidade Máxima do carro é {self.velocidade}')
        print(f'Ele percorre {self.km}Km por litro')
        
class onibus(veiculo):
    def capacidade_assentos(self,capacidade=70):
        return super().capacidade_assentos(capacidade)