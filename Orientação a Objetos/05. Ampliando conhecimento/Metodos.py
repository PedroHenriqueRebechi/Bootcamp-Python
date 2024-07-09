# Metodos de classe - Criar métodos de fábrica

# Metodos estaticos - Não recebe argumento explicito, cria funções utilitárias

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome): # Convenção usar cls inves de self
        print(cls)
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod # Praticamente como se fosse uma função mas dentro da classe
    def e_maior_idade(idade):
        return idade >= 18

    
pessoa_1 = Pessoa("Gui", 19)
print(pessoa_1.nome, pessoa_1.idade)

pessoa_2 = Pessoa.criar_de_data_nascimento(1993,3,2,"joão")
print(pessoa_2.nome, pessoa_2.idade)

pessoa_3 = Pessoa.e_maior_idade(18)
pessoa_4 = Pessoa.e_maior_idade(14)
print(pessoa_3, pessoa_4)

