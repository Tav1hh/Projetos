from datetime import date

class pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    #Um método de classe para criar
    #um objeto pessoa através do ano de nascimento.
    @classmethod
    def apartirAnoNascimento(cls,nome,ano):
        return cls(nome, date.today().year - ano)
    #Metodo estático: verificar se é maior de idade.
    @staticmethod
    def eMaiorIdade(idade):
        return idade >=18
    
pessoa1 = pessoa('Maria',26)
pessoa2 = pessoa.apartirAnoNascimento('ana',2006)
print(pessoa1.idade)
print(pessoa2.idade)
#Imprimir o resultado
print(pessoa2.eMaiorIdade(pessoa2.idade))