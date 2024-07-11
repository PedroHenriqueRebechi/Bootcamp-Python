# Permite economizar processamento para objetos muito grandes

# É um objeto que contem um numero contavel de valores que podem ser iterados, ou seja, pode percorrer todos

# Serve para ler arquivos grandes, economizar memória

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[1,2,3]):
    print(i)

class Soma:
    def __iter__(self):
        self.num = 0
        return self
    
    def __next__(self):
        if self.num < 10:
            self.num += 1
            return self.num
        else:
            raise StopIteration
        
for numero in Soma():
    print(numero)