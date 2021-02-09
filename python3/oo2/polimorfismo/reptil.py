from animal import Animal

class Reptil(Animal):

    def __init__(self, peso, idade, cor_escama):
        super().__init__(peso, idade)
        self._cor_escama = cor_escama

    @property
    def cor_escama(self):
        return self._cor_escama

    def alimentar(self):
        print('Vegetais, ovos e outros animais')

    def emitirSom(self):
        print('Som de réptil')

r = Reptil(20, 5, 'verde azulada')
print(f'Idade: {r.idade} ano - Peso: {r.peso}kg - Cor: {r.cor_escama}')
