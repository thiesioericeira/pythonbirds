class Pessoa:
    def __init__(self,*filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar (self):
        return f'olá {id(self)}'
        self.nome = none

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    Luciano = Pessoa(renzo, nome='luciano')
    print(Pessoa.cumprimentar(Luciano))
    print(id(Luciano))
    print(Luciano.cumprimentar())
    print(Luciano.nome)
    print(Luciano.idade)
    for filho in Luciano.filhos:
        print(filho.nome)
    print(Luciano.filhos)



