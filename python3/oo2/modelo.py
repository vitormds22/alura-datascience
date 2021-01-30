class Filme: 
    
    def __init__(self, nome, ano, duracao):
        self.nome = nome 
        self.ano = ano 
        self.duracao = duracao

class Serie:

    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano 
        self.temporadas = temporadas

vingadores = Filme('Matrix', 2006, 160)
print(f'*FILME* \nNome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}\n')

breaking_bad = Serie('Breaking Bad', 2008, 5)
print('*SERIE*\nA melhor série do mundo é {}, estreou em {} e tem {} temporadas'.format(breaking_bad.nome, breaking_bad.ano, breaking_bad.temporadas))