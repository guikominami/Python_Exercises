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
            
    def detalhe(self, msg=''):
        print(f'O seu saldo é: {self.saldo:.2f} {msg}')
        
                
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo > 0:
            self.saldo -= valor
            self.detalhe(f'Efetuado saque de: {self.saldo}.')