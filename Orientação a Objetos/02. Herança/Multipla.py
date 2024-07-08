class Animal:
    def __init__(self, numero_patas, ):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # Utiliza-se **kw para substituir a repetição do argumento numero_patas e poder executar sem problemas a classe Ornitorrinco
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        

class Cachorro(Mamifero):
    pass 

class falar:
    def falar(self):
        return "Oi!"

class Ornitorrinco(Mamifero, Ave, falar):
    pass


cachorro = Cachorro(numero_patas = 4, cor_pelo = "Cinza")
print(cachorro)

ornitorrinco = Ornitorrinco(numero_patas = 4, cor_pelo = "Preto", cor_bico = "Laranja")
print(ornitorrinco)
print(ornitorrinco.falar())
