class Animal:
    def __init__(self, nome, idade, preco):
        self.nome = nome
        self.idade = idade
        self.__preco = preco  # Privado
    
    def fazer_som(self):
        return "Som genérico"
    
    def get_preco(self):
        return self.__preco
    
    def info(self):
        return f"{self.nome} - {self.idade} anos"