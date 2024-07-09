# Com property() você pode criar atributos gerenciados em suas classes. 

class Foo:
    def __init__(self, numero=None):
        self._numero = numero

    @property
    def numero(self):
        return self._numero or 0

    @numero.setter
    def numero(self, valor):
        self._numero += valor

    @numero.deleter
    def numero(self):
        self._numero = -1


foo = Foo(1) # Acessou método __init__
print(foo.numero) 

foo.numero = 10 # Acessou property -> numero.setter, definiu valor
print(foo.numero)  

del foo.numero
print(foo.numero)