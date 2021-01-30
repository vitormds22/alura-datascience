class Filme: 
    
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano 
        self.duracao = duracao
        self.__likes = 0

    def add_likes(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano 
        self.temporadas = temporadas
        self.__likes = 0

    def add_likes(self):
        self.__likes += 1
    
    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome.title()

vingadores = Filme('o menino de pijama listrado', 2006, 160)
vingadores.add_likes()
print(f'*FILME* \nFilme: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}\n')

breaking_bad = Serie('breaking bad', 2008, 5)
breaking_bad.add_likes()
print(f'*SERIE* \nSérie: {breaking_bad.nome} - Ano: {breaking_bad.ano} - Temporadas: {breaking_bad.temporadas} - Likes: {breaking_bad.likes}')
