#Crie uma classe ContaBancaria com os atributos saldo e titular. Adicione métodos para depositar, sacar e exibir o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print(f"Saldo de {self.titular}: {self.saldo} reais")

conta1 = ContaBancaria("João")
conta1.depositar(1000)
conta1.sacar(500)
conta1.exibir_saldo()
