# INTRODUÇÃO

# CLASSE - Define as características de um objeto, porém não é usado diretamente

# OBJETO - Possuem as características definidas nas classes mas pode ser usado

# MÉTODO - Define um comportamento 

# EXEMPLO 1
class Cachorro: 
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self): # Método
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")


cao_1 = Cachorro("Roger", "Amarelo", False)
cao_2 = Cachorro("Aladim", "Branco")

cao_1.latir()

print(f"Acordado: {cao_2.acordado}")
cao_2.dormir()
print(f"Acordado: {cao_2.acordado}")


# EXEMPLO 2
class Bicicleta_vendida:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BIBI")
    
    def parar(self):
        print("Parando...")

    def correr(self):
        print("Correndo..")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

caloi = Bicicleta_vendida("Verde", "Caloi", 2022, 800)
print(caloi)

caloi

caloi.buzinar()
caloi.correr()
print(caloi.ano)

caloi_2 = Bicicleta_vendida("Vermelha", "Caloi", 2000, 200)

# Mesmo resultado
Bicicleta_vendida.buzinar(caloi_2)
caloi_2.buzinar()

