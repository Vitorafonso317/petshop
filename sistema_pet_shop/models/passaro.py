from .animal import Animal

class Passaro(Animal):
    def fazer_som(self):
        return "Piu piu!"
    
    def voar(self):
        return "O pássaro está voando!"