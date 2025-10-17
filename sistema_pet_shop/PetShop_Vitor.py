from models.animal import Animal
from models.cachorro import Cachorro
from models.gato import Gato
from models.passaro import Passaro
from models.cliente import Cliente
from models.petshop import PetShop

def menu_principal():
    pet_shop = PetShop("Bichinhos & Cia")
    
    # Adicionar alguns dados de exemplo
    cachorro = Cachorro("Rex", 2, 500.00)
    gato = Gato("Mimi", 1, 300.00)
    passaro = Passaro("Piu", 1, 150.00)
    
    pet_shop.adicionar_animal(cachorro)
    pet_shop.adicionar_animal(gato)
    pet_shop.adicionar_animal(passaro)
    
    cliente = Cliente("João Silva", "11999999999")
    pet_shop.cadastrar_cliente(cliente)
    
    print(f"\n🐾 Bem-vindo ao {pet_shop.nome}! 🐾")
    print("Sistema iniciado com dados de exemplo.")
    
    while True:
        print("\n=== PET SHOP SYSTEM ===")
        print("1. Cadastrar Animal")
        print("2. Cadastrar Cliente")
        print("3. Vender Animal")
        print("4. Listar Animais Disponíveis")
        print("5. Relatório de Vendas")
        print("6. Demonstrar Polimorfismo")
        print("7. Sair")
        
        escolha = input("Escolha: ")
        
        if escolha == "1":
            cadastrar_animal(pet_shop)
        elif escolha == "2":
            cadastrar_cliente(pet_shop)
        elif escolha == "3":
            vender_animal(pet_shop)
        elif escolha == "4":
            listar_animais(pet_shop)
        elif escolha == "5":
            relatorio_vendas(pet_shop)
        elif escolha == "6":
            demonstrar_polimorfismo(pet_shop)
        elif escolha == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

def cadastrar_animal(pet_shop):
    print("\n=== CADASTRAR ANIMAL ===")
    print("1. Cachorro")
    print("2. Gato")
    print("3. Pássaro")
    
    tipo = input("Tipo do animal: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    preco = float(input("Preço: R$ "))
    
    if tipo == "1":
        animal = Cachorro(nome, idade, preco)
    elif tipo == "2":
        animal = Gato(nome, idade, preco)
    elif tipo == "3":
        animal = Passaro(nome, idade, preco)
    else:
        print("Tipo inválido!")
        return
    
    pet_shop.adicionar_animal(animal)
    print(f"{animal.nome} cadastrado com sucesso!")

def cadastrar_cliente(pet_shop):
    print("\n=== CADASTRAR CLIENTE ===")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    
    cliente = Cliente(nome, telefone)
    pet_shop.cadastrar_cliente(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def vender_animal(pet_shop):
    print("\n=== VENDER ANIMAL ===")
    nome_animal = input("Nome do animal: ")
    nome_cliente = input("Nome do cliente: ")
    
    resultado = pet_shop.vender_animal(nome_animal, nome_cliente)
    print(resultado)

def listar_animais(pet_shop):
    print("\n=== ANIMAIS DISPONÍVEIS ===")
    animais = pet_shop.listar_animais_disponiveis()
    
    if isinstance(animais, str):
        print(animais)
    else:
        for animal in animais:
            print(animal)

def relatorio_vendas(pet_shop):
    print("\n=== RELATÓRIO DE VENDAS ===")
    relatorio = pet_shop.relatorio_vendas()
    
    if isinstance(relatorio, str):
        print(relatorio)
    else:
        for linha in relatorio:
            print(linha)

def demonstrar_polimorfismo(pet_shop):
    print("\n=== SONS DOS ANIMAIS ===")
    if not pet_shop.animais:
        print("Nenhum animal disponível")
    else:
        for animal in pet_shop.animais:
            print(f"{animal.nome}: {animal.fazer_som()}")
            
            # Demonstrar métodos específicos
            if hasattr(animal, 'latir'):
                print(f"  -> {animal.latir()}")
            elif hasattr(animal, 'miar'):
                print(f"  -> {animal.miar()}")
            elif hasattr(animal, 'voar'):
                print(f"  -> {animal.voar()}")

if __name__ == "__main__":
    print("=== SISTEMA PET SHOP ===")
    print("Escolha o modo de execução:")
    print("1. Interface Gráfica (Recomendado)")
    print("2. Menu em Texto")
    print("3. Exemplo de Demonstração")
    
    escolha = input("Opção: ")
    
    if escolha == "1":
        try:
            from interface_grafica import PetShopGUI
            app = PetShopGUI()
            app.executar()
        except ImportError:
            print("Erro: tkinter não disponível. Executando menu em texto...")
            menu_principal()
    elif escolha == "2":
        menu_principal()
    elif escolha == "3":
        # Exemplo de uso conforme especificado
        pet_shop = PetShop("Bichinhos & Cia")
        
        # Cadastrar animais
        cachorro = Cachorro("Rex", 2, 500.00)
        gato = Gato("Mimi", 1, 300.00)
        passaro = Passaro("Piu", 1, 150.00)
        
        pet_shop.adicionar_animal(cachorro)
        pet_shop.adicionar_animal(gato)
        pet_shop.adicionar_animal(passaro)
        
        # Cadastrar cliente
        cliente = Cliente("João Silva", "11999999999")
        pet_shop.cadastrar_cliente(cliente)
        
        # Demonstrar polimorfismo
        demonstrar_polimorfismo(pet_shop)
        
        # Iniciar menu
        menu_principal()
    else:
        print("Opção inválida! Executando menu em texto...")
        menu_principal()