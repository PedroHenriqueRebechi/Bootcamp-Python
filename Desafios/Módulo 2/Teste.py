from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta, transacao):
        return
    
    def adicionar_conta(self, conta):
        return

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.today().strftime("%d-%m-%Y %H:%M"),
            }
        )
        print(self._transacoes)

class Conta:
    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        #return Conta
        pass
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False
       
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(self._saldo)
            return True
        else:
            print("Informe um valor válido")
            return False
          
class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self._limite = 500.0
        self._limite_saques = 3

    def sacar(self, valor):

        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])


        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)
  
class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass
    
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
    
        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)
        
    
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas=[]):
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

def operacao(objeto, conta): # Polimorfismo - testar
    objeto.registrar(conta)

cliente_1 = Cliente("Rua A", [])
historico_1 = Historico()
conta_1 = Conta(1, "0001")

while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Quanto você vai depositar: R$"))
        deposito = Deposito(valor)
        operacao(deposito, conta_1)
    
    elif opcao == "s":
        valor = float(input("Quanto você vai depositar: R$"))
        saque = Saque(valor)
        operacao(saque, conta_1)

    elif opcao == "e":
        print(conta_1.historico.exibir_extrato())