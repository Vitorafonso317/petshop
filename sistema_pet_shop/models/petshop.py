class PetShop:
    def __init__(self, nome):
        self.nome = nome
        self.animais = []
        self.clientes = []
    
    def adicionar_animal(self, animal):
        self.animais.append(animal)
    
    def cadastrar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def vender_animal(self, nome_animal, nome_cliente):
        # Buscar animal
        animal = None
        for a in self.animais:
            if a.nome.lower() == nome_animal.lower():
                animal = a
                break
        
        if not animal:
            return "Animal não encontrado!"
        
        # Buscar cliente
        cliente = None
        for c in self.clientes:
            if c.nome.lower() == nome_cliente.lower():
                cliente = c
                break
        
        if not cliente:
            return "Cliente não encontrado!"
        
        # Realizar venda
        cliente.adicionar_compra(animal)
        self.animais.remove(animal)
        return f"Venda realizada! {animal.nome} vendido para {cliente.nome}"
    
    def listar_animais_disponiveis(self):
        if not self.animais:
            return "Nenhum animal disponível"
        
        lista = []
        for animal in self.animais:
            tipo = animal.__class__.__name__
            lista.append(f"{animal.nome} ({tipo}) - {animal.idade} anos - R$ {animal.get_preco():.2f}")
        return lista
    
    def relatorio_vendas(self):
        total_vendas = 0
        vendas_por_cliente = []
        
        for cliente in self.clientes:
            gasto = cliente.get_total_gasto()
            if gasto > 0:
                total_vendas += gasto
                vendas_por_cliente.append(f"{cliente.nome}: R$ {gasto:.2f}")
        
        if not vendas_por_cliente:
            return "Nenhuma venda realizada"
        
        relatorio = ["=== RELATÓRIO DE VENDAS ==="]
        relatorio.extend(vendas_por_cliente)
        relatorio.append(f"Total de vendas: R$ {total_vendas:.2f}")
        return relatorio