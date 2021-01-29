class Conta:
    
    def __init__(self, numero, saldo, limite):
        self.__numero = numero 
        self.__saldo = saldo 
        self.__limite = limite
        self.__tarifa_tranferencia = 8.0

    def __tem_saldo_disponivel_para(self, valor):
        return valor <= (self.__limite + self.__saldo)
    
    def saca(self, valor):
        if self.__tem_saldo_disponivel_para(valor):
            self.__saldo -= valor
            print('Saque efetuado')
        else:
            print('Saldo insuficiente')

    def transferir(self, valor, destino):
        valor_total = valor + self.__tarifa_tranferencia

        if self.__tem_saldo_disponivel_para(valor):
            self.__saldo -= valor_total
            print('Transferência efetuada.')
        else:
            print('Saldo insuficiente')
    
