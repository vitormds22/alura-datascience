class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo um objeto ... {}'.format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('Saldo {} do titular {}'.format(self.saldo, self.titular))

    def sacar(self, valor):
        self.saldo -= valor
    
    def depositar(self, valor):
        self.saldo += valor