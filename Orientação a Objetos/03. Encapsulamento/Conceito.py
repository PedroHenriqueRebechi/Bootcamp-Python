# ENCAPSULAMENTO - Agrupa dados e os métodos para protege-los de alterações indevidas

# Variável pública - Pode ser acessado fora da classe

# Variável privada - Só pode ser acessado pela classe, começa com underline

class Conta: 
    def __init__(self, numero_agencia, saldo=0,): 
        self._saldo = saldo  # Privado
        self.numero_agencia = numero_agencia # Público
    
    def depositar(self, valor): 
        self._saldo += valor

    def sacar(self, valor): 
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    

conta = Conta("0001", 100)

print(conta._saldo) # ERRADO - O Python permite mas é uma convenção não acessar valores privados fora do escopo

print(conta.numero_agencia) # CERTO - Variável pública

print(conta.mostrar_saldo()) # CERTO - Para acessar a variável privada, crie um método especifíco