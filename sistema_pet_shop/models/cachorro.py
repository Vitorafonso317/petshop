from .animal import Animal

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"
    
    def latir(self):
        return "O cachorro está latindo!"