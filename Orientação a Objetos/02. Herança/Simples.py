class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor 
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'sim,' if self.carregado else "não"} está carregado")


moto = Motocicleta("Verde", "ABC-3255", 2)
moto.ligar_motor()

carro = Carro("branco", "aje-3421", 4)
carro.ligar_motor()

caminhao = Caminhao("Preto", "sko-3920", 6, True)
caminhao.ligar_motor()
caminhao.esta_carregado()