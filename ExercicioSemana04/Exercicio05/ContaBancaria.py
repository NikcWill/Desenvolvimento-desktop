class ContaBancaria:
    def __init__(self, titular, saldo = None):
        self.titular = titular
        self.saldo = float(saldo) if saldo is not None else None

    def depositar (self, valor):
        self.saldo += valor
        print(f'Depositado {valor}')

    def sacar (self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Sacado {valor}')
        else:
            print(f'Saldo insuficiente, seu saldo é {self.saldo}')

    def imprimir (self):
        print(f'Olá sr(a): {self.titular} \n'
        f'e o seu saldo é: {self.saldo} \n')



c1 = ContaBancaria('Nicollas',10)
c1.depositar(50)
c1.imprimir()

c1.sacar(50)
c1.imprimir()
c1.sacar(50)
c1.imprimir()
