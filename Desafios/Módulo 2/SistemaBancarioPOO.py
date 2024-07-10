from abc import ABC, abstractmethod

class Conta:
    def __init__(self,saldo,numero,agencia,cliente,historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    def saldo(self):
        return float
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return Conta
    
    def sacar(self, valor):
        return bool
    
    def depositar(self, valor):
        return bool
    
class ContaCorrente(Conta):
    def __init__(self,limite, limite_saques, saldo, numero, agencia, cliente, historico):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self._limite = limite
        self._limite_saques = limite_saques

class Historico:
    def adicionar_transacao(self, transacao):
        return
    
class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        conta.depositar(self, self._valor)
        print(self._valor, conta)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    def registrar(self, conta):
        return

class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        return
    
    def adicionar_conta(self, conta):
        return
    
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

def menu():
    menu = """\n
    ------------------MENU------------------
    [d] DEPOSITAR
    [s] SACAR
    [e] EXTRATO
    [u] CRIAR USUÁRIO
    [c] CRIAR CONTA CORRENTE
    [q] SAIR

    -> """
    return input(menu).lower()

while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Quanto você vai depositar: R$"))
        deposito = Deposito(valor)
        deposito.registrar(Conta)