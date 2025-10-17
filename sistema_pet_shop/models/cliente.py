class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.__compras = []  # Privado
    
    def adicionar_compra(self, animal):
        self.__compras.append(animal)
    
    def get_total_gasto(self):
        return sum(animal.get_preco() for animal in self.__compras)
    
    def listar_compras(self):
        if not self.__compras:
            return "Nenhuma compra realizada"
        return [f"{animal.nome} - R$ {animal.get_preco():.2f}" for animal in self.__compras]