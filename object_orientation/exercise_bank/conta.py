from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abstractmethod
    def sacar(self, valor):
        self.detalhe(f'Saque: {valor}')
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhe(f'Depósito: {valor}')
        
    def detalhe(self, msg=''):
        print(f'O seu saldo é: {self.saldo:.2f} {msg}')

            
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhe(f'Saque: {valor}')
            return self.saldo
        
        print("Não foi possível efetuar o saque.")
        self.detalhe(f'Saque negado: {valor}')        

#usa a classe inicial da classe Mãe e cria um atributo a mais (limite)
#é necessário iniciar com super().__init__ depois do método __init__
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)           
        self.limite = limite
        
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhe(f'Saque: {valor}')
            return self.saldo
        
        print("Não foi possível efetuar o saque.")
        self.detalhe(f'Saque negado: {valor}')         

if __name__ == '__main__':
    conta_poupanca1 = ContaPoupanca('0001', '12345', 1000)
    conta_poupanca1.sacar(10)
    conta_poupanca1.depositar(20)
    conta_poupanca1.sacar(10000)
    print('#####')
    conta_corrente1 = ContaCorrente('0001', '12345', 1000, 100)
    conta_corrente1.sacar(10)
    conta_corrente1.depositar(20)
    conta_corrente1.sacar(10000)
    print('#####')    


