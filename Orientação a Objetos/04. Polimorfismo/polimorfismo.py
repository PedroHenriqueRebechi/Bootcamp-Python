# POLIMORFISMO - Significa o mesmo nome da função (mas assinaturas diferentes) sendo usado para tipos diferentes

# Exemplo
len("python")
len([10,20,30]) # Funciona com objetos de tipos diferentes

# Polimorfismo com herança
class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal Voando")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


def plano_de_voo(objeto): # Função - Polimorfismo
    objeto.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
print(Passaro().voar())
