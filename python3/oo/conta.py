class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo um objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do titular {}'.format(self.__saldo, self.__titular))

    def sacar(self, valor):
        self.__saldo -= valor
    
    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_numero(self, numero):
        self.__numero = numero

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def set_titular(self, titular):
        self.__titular = titular

    def set_limite(self, limite):
        self.__limite = limite