class Sistema:

    def __init__(self):
        self.texto = ''
        pass

    def le_entrada(self):
        self.texto = input('Digite o que quiser: ')

    def exibe_saida(self):
        print('Você digitou: {}'.format(self.texto))