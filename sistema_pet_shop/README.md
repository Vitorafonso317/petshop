# Sistema de Pet Shop

## Descrição
Sistema de gerenciamento de Pet Shop desenvolvido em Python aplicando os 4 pilares da Programação Orientada a Objetos.

## Funcionalidades
- Cadastro de animais (Cachorro, Gato, Pássaro)
- Cadastro de clientes
- Venda de animais
- Listagem de animais disponíveis
- Relatório de vendas
- Interface gráfica intuitiva
- Demonstração de polimorfismo

## Estrutura do Projeto
```
sistema_pet_shop/
├── models/
│   ├── __init__.py
│   ├── animal.py          # Classe base Animal
│   ├── cachorro.py        # Classe Cachorro (herda de Animal)
│   ├── gato.py           # Classe Gato (herda de Animal)
│   ├── passaro.py        # Classe Passaro (herda de Animal)
│   ├── cliente.py        # Classe Cliente
│   └── petshop.py        # Classe PetShop
├── data/                 # Pasta para dados (opcional)
├── PetShop_Vitor.py     # Arquivo principal
├── interface_grafica.py # Interface gráfica (tkinter)
└── README.md            # Documentação
```

## Como Executar

### Opção 1: Interface Gráfica (Recomendado)
```bash
cd sistema_pet_shop
python PetShop_Vitor.py
# Escolha opção 1 para interface gráfica
```

### Opção 2: Menu em Texto
```bash
cd sistema_pet_shop
python PetShop_Vitor.py
# Escolha opção 2 para menu em texto
```

### Opção 3: Executar apenas interface gráfica
```bash
cd sistema_pet_shop
python interface_grafica.py
```

## Pilares da POO Implementados

### 1. Encapsulamento
- Atributos privados: `__preco` na classe Animal e `__compras` na classe Cliente
- Métodos getter: `get_preco()` e `get_total_gasto()`

### 2. Herança
- Classes Cachorro, Gato e Passaro herdam da classe Animal
- Reutilização de código da classe base

### 3. Polimorfismo
- Método `fazer_som()` implementado de forma diferente em cada classe filha
- Mesmo método, comportamentos diferentes

### 4. Abstração
- Classes representam entidades do mundo real
- Métodos específicos para cada tipo de animal

## Interface Gráfica
A interface gráfica possui:
- **Abas organizadas** para cada funcionalidade
- **Formulários intuitivos** para cadastro
- **Combos de seleção** para vendas
- **Área de relatórios** com scroll
- **Botões coloridos** para melhor usabilidade
- **Validações** de entrada de dados

## Exemplo de Uso
O sistema inicia com alguns dados de exemplo (Rex, Mimi, Piu e cliente João Silva) para facilitar os testes.

## Tecnologias Utilizadas
- Python 3.x
- tkinter (interface gráfica)
- Programação Orientada a Objetos

## Recursos da Interface Gráfica
- 🐕 Ícones e emojis para melhor visualização
- 🎨 Cores organizadas por funcionalidade
- 📋 Abas para organização do conteúdo
- ✅ Validações de formulário
- 📊 Relatórios formatados
- 🔄 Atualização automática de listas

## Autor
Vitor