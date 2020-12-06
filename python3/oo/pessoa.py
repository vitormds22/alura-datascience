class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome_e_sobrenome(self):
        print('O nome completo é: {} {}'.format(self.nome, self.sobrenome))
