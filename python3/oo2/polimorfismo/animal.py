class Animal:
    
    def __init__(self, peso, idade):
        self._peso = peso
        self._idade = idade

    @property
    def peso(self):
        return self._peso
    
    @property
    def idade(self):
        return self._idade

    def locomover(self):
        print('Correndo')

    def alimentar(self):
        print('Comendo')
        pass

    def emitirSom(self):
        print('Que som é esse ?')
        pass