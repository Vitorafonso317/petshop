from .animal import Animal

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
    
    def miar(self):
        return "O gato está miando!"