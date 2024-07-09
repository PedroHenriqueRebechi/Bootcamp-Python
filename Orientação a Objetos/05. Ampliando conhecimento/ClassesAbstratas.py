# O que são interfaces? Definem o que uma classe deve fazer e não como fazer

# Para criar interface em Python, utilizam-se as classes abstratas

# Módulo ABC 
from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self): # Método abstrato, obriga classes filhas a implementar o método
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self): # Implementação que foi obrigada
        print("Ligando") 
    
    def desligar(self):
        print("Desligando")


controle = ControleTV()
controle.ligar()
