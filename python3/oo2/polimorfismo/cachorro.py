from mamifero import Mamifero

class Cachorro(Mamifero):

    def __init__(self, peso, idade, cor_pelo): 
        super().__init__(peso, idade, cor_pelo)

    def emitirSom(self):
        print('AU AU')