"""
Arquivo de exemplo para testar o sistema Pet Shop
Execute este arquivo para ver uma demonstração completa
"""

from models.cachorro import Cachorro
from models.gato import Gato
from models.passaro import Passaro
from models.cliente import Cliente
from models.petshop import PetShop

def exemplo_completo():
    print("🐾" * 20)
    print("   DEMONSTRAÇÃO SISTEMA PET SHOP")
    print("🐾" * 20)
    
    # Criar pet shop
    pet_shop = PetShop("Bichinhos & Cia")
    print(f"\n✅ Pet Shop '{pet_shop.nome}' criado!")
    
    # Cadastrar animais
    print("\n📝 Cadastrando animais...")
    animais = [
        Cachorro("Rex", 2, 500.00),
        Cachorro("Buddy", 3, 600.00),
        Gato("Mimi", 1, 300.00),
        Gato("Garfield", 4, 400.00),
        Passaro("Piu", 1, 150.00),
        Passaro("Tweety", 2, 200.00)
    ]
    
    for animal in animais:
        pet_shop.adicionar_animal(animal)
        print(f"   🐕🐱🐦 {animal.nome} cadastrado!")
    
    # Cadastrar clientes
    print("\n👥 Cadastrando clientes...")
    clientes = [
        Cliente("João Silva", "11999999999"),
        Cliente("Maria Santos", "11888888888"),
        Cliente("Pedro Oliveira", "11777777777")
    ]
    
    for cliente in clientes:
        pet_shop.cadastrar_cliente(cliente)
        print(f"   👤 {cliente.nome} cadastrado!")
    
    # Demonstrar polimorfismo
    print("\n🔊 DEMONSTRAÇÃO DE POLIMORFISMO:")
    print("-" * 40)
    for animal in pet_shop.animais:
        print(f"🐾 {animal.nome} ({animal.__class__.__name__}): {animal.fazer_som()}")
        
        # Métodos específicos
        if hasattr(animal, 'latir'):
            print(f"   ➤ {animal.latir()}")
        elif hasattr(animal, 'miar'):
            print(f"   ➤ {animal.miar()}")
        elif hasattr(animal, 'voar'):
            print(f"   ➤ {animal.voar()}")
    
    # Listar animais disponíveis
    print("\n📋 ANIMAIS DISPONÍVEIS:")
    print("-" * 40)
    animais_disponiveis = pet_shop.listar_animais_disponiveis()
    for animal in animais_disponiveis:
        print(f"   • {animal}")
    
    # Realizar algumas vendas
    print("\n💰 REALIZANDO VENDAS:")
    print("-" * 40)
    vendas = [
        ("Rex", "João Silva"),
        ("Mimi", "Maria Santos"),
        ("Piu", "Pedro Oliveira")
    ]
    
    for nome_animal, nome_cliente in vendas:
        resultado = pet_shop.vender_animal(nome_animal, nome_cliente)
        print(f"   💳 {resultado}")
    
    # Relatório de vendas
    print("\n📊 RELATÓRIO DE VENDAS:")
    print("-" * 40)
    relatorio = pet_shop.relatorio_vendas()
    for linha in relatorio:
        print(f"   {linha}")
    
    # Animais restantes
    print("\n📋 ANIMAIS AINDA DISPONÍVEIS:")
    print("-" * 40)
    animais_restantes = pet_shop.listar_animais_disponiveis()
    if isinstance(animais_restantes, str):
        print(f"   {animais_restantes}")
    else:
        for animal in animais_restantes:
            print(f"   • {animal}")
    
    # Demonstrar encapsulamento
    print("\n🔒 DEMONSTRAÇÃO DE ENCAPSULAMENTO:")
    print("-" * 40)
    cliente_teste = pet_shop.clientes[0]
    print(f"Cliente: {cliente_teste.nome}")
    print(f"Total gasto: R$ {cliente_teste.get_total_gasto():.2f}")
    print("Compras realizadas:")
    compras = cliente_teste.listar_compras()
    if isinstance(compras, list):
        for compra in compras:
            print(f"   • {compra}")
    else:
        print(f"   {compras}")
    
    print("\n" + "🎉" * 20)
    print("   DEMONSTRAÇÃO CONCLUÍDA!")
    print("🎉" * 20)
    print("\n💡 Para usar a interface gráfica, execute:")
    print("   python PetShop_Vitor.py")
    print("   e escolha a opção 1")

if __name__ == "__main__":
    exemplo_completo()