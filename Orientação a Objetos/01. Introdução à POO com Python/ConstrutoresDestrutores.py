class Cachorro:
    # MÉTODO CONSTRUTOR - inicializamos o estado do objeto, cria-se um método com nome __init__
    def __init__(self, nome):
        self.nome = nome
        print(nome)

    # MÉTODO DESTRUTOR - destrutor de classe, nome __del__
    def __del__(self):
        print("Destruindo a instância...")

    def latir(self):
        print("auau")


c = Cachorro("Mel")
c.latir() # Executa e depois destrói mesmo estando fora de ordem

print("Exemplo")

del c # Força a destruição

print("Exemplo")
print("Exemplo")
print("Exemplo")