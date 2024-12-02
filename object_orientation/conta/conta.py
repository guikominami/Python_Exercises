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
        
        if valor_pos_saque > 0:
            self.saldo -= valor
            self.detalhe(f'Efetuado saque de: {valor}.')
            return self.saldo
            
        print(f'Não foi possível efetuar o saque de : {valor}. Seu saldo é de {self.saldo}')
                        
if __name__ == "__main__":
    
    c1 = ContaPoupanca("0123", "12345", 1000)
    c1.depositar(1000)
    c1.depositar(1000)
    c1.depositar(1000)
    c1.sacar(3001)
