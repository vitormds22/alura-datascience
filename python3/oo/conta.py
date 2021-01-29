class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo um objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do titular {}'.format(self.__saldo, self.__titular))

    def __valida_saldo(self, valor_saque):
        valor_disponível_saque = self.__limite + self.__saldo
        return valor_saque <= valor_disponível_saque

    def sacar(self, valor):
        if self.__valida_saldo(valor):
            self.__saldo -= valor
        else:
            print('Você não tem saldo o suficiente!')
    
    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite