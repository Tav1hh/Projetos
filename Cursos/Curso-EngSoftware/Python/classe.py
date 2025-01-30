class Pessoa:
    def __init__(self,nome,ender):
        self.set_ender(ender)
        self.set_nome(nome)
    
    def set_nome(self,nome):
        self.nome = nome
    
    def set_ender(self,ender):
        self.ender = ender

    def get_nome(self):
        return self.get_nome

    def get_ender(self):
        return self.ender
    

pessoa1 = Pessoa('Maria','rua 01234')
pessoa2 = Pessoa('João','rua 56789')

print(pessoa1.get_ender())
