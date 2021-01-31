class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    def add_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('o menino de pijama listrado', 2006, 160)
vingadores.add_likes()
print(f'*FILME* \nFilme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}\n')

breaking_bad = Serie('breaking bad', 2008, 5)
breaking_bad.add_likes()
breaking_bad.add_likes()
print(f'*SERIE* \nSérie: {breaking_bad.nome} - Ano: {breaking_bad.ano} - Temporadas: {breaking_bad.temporadas} - Likes: {breaking_bad.likes}')
