from animal import Animal

class Mamifero(Animal):

    def __init__(self, peso, idade, cor_pelo):
        super().__init__(peso, idade)
        self._cor_pelo = cor_pelo

    @property
    def cor_pelo(self):
        return self._cor_pelo

    def alimentar(self):
        print('Leite')

    def emitirSom(self):
        print('Som de mamífero')

    
m = Mamifero(70, 23, 'branco')
m.locomover()
m.alimentar()
m.emitirSom()
print(m.peso)
print(m.cor_pelo)