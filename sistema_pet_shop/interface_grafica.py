import tkinter as tk
from tkinter import ttk, messagebox
from models.cachorro import Cachorro
from models.gato import Gato
from models.passaro import Passaro
from models.cliente import Cliente
from models.petshop import PetShop

class PetShopGUI:
    def __init__(self):
        self.pet_shop = PetShop("Bichinhos & Cia")
        self.root = tk.Tk()
        self.root.title("Sistema Pet Shop")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        self.criar_interface()
        
    def criar_interface(self):
        # Título
        titulo = tk.Label(self.root, text="🐾 SISTEMA PET SHOP 🐾", 
                         font=("Arial", 20, "bold"), bg='#f0f0f0', fg='#2c3e50')
        titulo.pack(pady=20)
        
        # Frame principal com notebook (abas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Aba Cadastrar Animal
        self.frame_animal = ttk.Frame(notebook)
        notebook.add(self.frame_animal, text="Cadastrar Animal")
        self.criar_aba_animal()
        
        # Aba Cadastrar Cliente
        self.frame_cliente = ttk.Frame(notebook)
        notebook.add(self.frame_cliente, text="Cadastrar Cliente")
        self.criar_aba_cliente()
        
        # Aba Vender Animal
        self.frame_venda = ttk.Frame(notebook)
        notebook.add(self.frame_venda, text="Vender Animal")
        self.criar_aba_venda()
        
        # Aba Relatórios
        self.frame_relatorio = ttk.Frame(notebook)
        notebook.add(self.frame_relatorio, text="Relatórios")
        self.criar_aba_relatorio()
        
    def criar_aba_animal(self):
        # Frame para formulário
        form_frame = tk.Frame(self.frame_animal, bg='white', relief='raised', bd=2)
        form_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(form_frame, text="Cadastrar Novo Animal", font=("Arial", 14, "bold"), 
                bg='white').pack(pady=10)
        
        # Tipo do animal
        tk.Label(form_frame, text="Tipo:", bg='white').pack(anchor='w', padx=20)
        self.tipo_var = tk.StringVar(value="Cachorro")
        tipo_frame = tk.Frame(form_frame, bg='white')
        tipo_frame.pack(anchor='w', padx=20, pady=5)
        
        tk.Radiobutton(tipo_frame, text="🐕 Cachorro", variable=self.tipo_var, 
                      value="Cachorro", bg='white').pack(side='left', padx=10)
        tk.Radiobutton(tipo_frame, text="🐱 Gato", variable=self.tipo_var, 
                      value="Gato", bg='white').pack(side='left', padx=10)
        tk.Radiobutton(tipo_frame, text="🐦 Pássaro", variable=self.tipo_var, 
                      value="Passaro", bg='white').pack(side='left', padx=10)
        
        # Nome
        tk.Label(form_frame, text="Nome:", bg='white').pack(anchor='w', padx=20, pady=(10,0))
        self.nome_animal = tk.Entry(form_frame, width=30, font=("Arial", 10))
        self.nome_animal.pack(anchor='w', padx=20, pady=5)
        
        # Idade
        tk.Label(form_frame, text="Idade:", bg='white').pack(anchor='w', padx=20)
        self.idade_animal = tk.Entry(form_frame, width=30, font=("Arial", 10))
        self.idade_animal.pack(anchor='w', padx=20, pady=5)
        
        # Preço
        tk.Label(form_frame, text="Preço (R$):", bg='white').pack(anchor='w', padx=20)
        self.preco_animal = tk.Entry(form_frame, width=30, font=("Arial", 10))
        self.preco_animal.pack(anchor='w', padx=20, pady=5)
        
        # Botão cadastrar
        tk.Button(form_frame, text="Cadastrar Animal", command=self.cadastrar_animal,
                 bg='#3498db', fg='white', font=("Arial", 10, "bold"), 
                 width=20).pack(pady=20)
        
    def criar_aba_cliente(self):
        # Frame para formulário
        form_frame = tk.Frame(self.frame_cliente, bg='white', relief='raised', bd=2)
        form_frame.pack(pady=20, padx=20, fill='x')
        
        tk.Label(form_frame, text="Cadastrar Novo Cliente", font=("Arial", 14, "bold"), 
                bg='white').pack(pady=10)
        
        # Nome
        tk.Label(form_frame, text="Nome:", bg='white').pack(anchor='w', padx=20)
        self.nome_cliente = tk.Entry(form_frame, width=40, font=("Arial", 10))
        self.nome_cliente.pack(anchor='w', padx=20, pady=5)
        
        # Telefone
        tk.Label(form_frame, text="Telefone:", bg='white').pack(anchor='w', padx=20, pady=(10,0))
        self.telefone_cliente = tk.Entry(form_frame, width=40, font=("Arial", 10))
        self.telefone_cliente.pack(anchor='w', padx=20, pady=5)
        
        # Botão cadastrar
        tk.Button(form_frame, text="Cadastrar Cliente", command=self.cadastrar_cliente,
                 bg='#2ecc71', fg='white', font=("Arial", 10, "bold"), 
                 width=20).pack(pady=20)
        
    def criar_aba_venda(self):
        # Frame para venda
        form_frame = tk.Frame(self.frame_venda, bg='white', relief='raised', bd=2)
        form_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        tk.Label(form_frame, text="Realizar Venda", font=("Arial", 14, "bold"), 
                bg='white').pack(pady=10)
        
        # Seleção de animal
        tk.Label(form_frame, text="Selecionar Animal:", bg='white').pack(anchor='w', padx=20)
        self.animal_combo = ttk.Combobox(form_frame, width=40, state="readonly")
        self.animal_combo.pack(anchor='w', padx=20, pady=5)
        
        # Seleção de cliente
        tk.Label(form_frame, text="Selecionar Cliente:", bg='white').pack(anchor='w', padx=20, pady=(10,0))
        self.cliente_combo = ttk.Combobox(form_frame, width=40, state="readonly")
        self.cliente_combo.pack(anchor='w', padx=20, pady=5)
        
        # Botões
        button_frame = tk.Frame(form_frame, bg='white')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Atualizar Listas", command=self.atualizar_combos,
                 bg='#f39c12', fg='white', font=("Arial", 10, "bold")).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="Realizar Venda", command=self.realizar_venda,
                 bg='#e74c3c', fg='white', font=("Arial", 10, "bold")).pack(side='left', padx=10)
        
    def criar_aba_relatorio(self):
        # Frame para relatórios
        relatorio_frame = tk.Frame(self.frame_relatorio, bg='white', relief='raised', bd=2)
        relatorio_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        tk.Label(relatorio_frame, text="Relatórios", font=("Arial", 14, "bold"), 
                bg='white').pack(pady=10)
        
        # Botões de relatório
        button_frame = tk.Frame(relatorio_frame, bg='white')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Animais Disponíveis", command=self.mostrar_animais,
                 bg='#9b59b6', fg='white', font=("Arial", 10, "bold")).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="Relatório de Vendas", command=self.mostrar_vendas,
                 bg='#34495e', fg='white', font=("Arial", 10, "bold")).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="Sons dos Animais", command=self.mostrar_sons,
                 bg='#16a085', fg='white', font=("Arial", 10, "bold")).pack(side='left', padx=10)
        
        # Área de texto para relatórios
        self.texto_relatorio = tk.Text(relatorio_frame, height=20, width=80, 
                                      font=("Courier", 10))
        self.texto_relatorio.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Scrollbar para o texto
        scrollbar = tk.Scrollbar(relatorio_frame, command=self.texto_relatorio.yview)
        scrollbar.pack(side='right', fill='y')
        self.texto_relatorio.config(yscrollcommand=scrollbar.set)
        
    def cadastrar_animal(self):
        try:
            nome = self.nome_animal.get().strip()
            idade = int(self.idade_animal.get())
            preco = float(self.preco_animal.get())
            tipo = self.tipo_var.get()
            
            if not nome:
                messagebox.showerror("Erro", "Nome é obrigatório!")
                return
            
            if tipo == "Cachorro":
                animal = Cachorro(nome, idade, preco)
            elif tipo == "Gato":
                animal = Gato(nome, idade, preco)
            else:  # Passaro
                animal = Passaro(nome, idade, preco)
            
            self.pet_shop.adicionar_animal(animal)
            messagebox.showinfo("Sucesso", f"{animal.nome} cadastrado com sucesso!")
            
            # Limpar campos
            self.nome_animal.delete(0, tk.END)
            self.idade_animal.delete(0, tk.END)
            self.preco_animal.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número inteiro e preço um número decimal!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar animal: {str(e)}")
    
    def cadastrar_cliente(self):
        try:
            nome = self.nome_cliente.get().strip()
            telefone = self.telefone_cliente.get().strip()
            
            if not nome or not telefone:
                messagebox.showerror("Erro", "Nome e telefone são obrigatórios!")
                return
            
            cliente = Cliente(nome, telefone)
            self.pet_shop.cadastrar_cliente(cliente)
            messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado com sucesso!")
            
            # Limpar campos
            self.nome_cliente.delete(0, tk.END)
            self.telefone_cliente.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {str(e)}")
    
    def atualizar_combos(self):
        # Atualizar combo de animais
        animais = [f"{animal.nome} ({animal.__class__.__name__})" for animal in self.pet_shop.animais]
        self.animal_combo['values'] = animais
        
        # Atualizar combo de clientes
        clientes = [cliente.nome for cliente in self.pet_shop.clientes]
        self.cliente_combo['values'] = clientes
        
        messagebox.showinfo("Sucesso", "Listas atualizadas!")
    
    def realizar_venda(self):
        try:
            animal_selecionado = self.animal_combo.get()
            cliente_selecionado = self.cliente_combo.get()
            
            if not animal_selecionado or not cliente_selecionado:
                messagebox.showerror("Erro", "Selecione um animal e um cliente!")
                return
            
            # Extrair nome do animal (antes do parênteses)
            nome_animal = animal_selecionado.split(" (")[0]
            
            resultado = self.pet_shop.vender_animal(nome_animal, cliente_selecionado)
            
            if "realizada" in resultado:
                messagebox.showinfo("Sucesso", resultado)
                # Limpar seleções
                self.animal_combo.set('')
                self.cliente_combo.set('')
                self.atualizar_combos()  # Atualizar listas após venda
            else:
                messagebox.showerror("Erro", resultado)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao realizar venda: {str(e)}")
    
    def mostrar_animais(self):
        self.texto_relatorio.delete(1.0, tk.END)
        animais = self.pet_shop.listar_animais_disponiveis()
        
        self.texto_relatorio.insert(tk.END, "=== ANIMAIS DISPONÍVEIS ===\n\n")
        
        if isinstance(animais, str):
            self.texto_relatorio.insert(tk.END, animais)
        else:
            for animal in animais:
                self.texto_relatorio.insert(tk.END, f"• {animal}\n")
    
    def mostrar_vendas(self):
        self.texto_relatorio.delete(1.0, tk.END)
        relatorio = self.pet_shop.relatorio_vendas()
        
        if isinstance(relatorio, str):
            self.texto_relatorio.insert(tk.END, relatorio)
        else:
            for linha in relatorio:
                self.texto_relatorio.insert(tk.END, f"{linha}\n")
    
    def mostrar_sons(self):
        self.texto_relatorio.delete(1.0, tk.END)
        self.texto_relatorio.insert(tk.END, "=== SONS DOS ANIMAIS ===\n\n")
        
        if not self.pet_shop.animais:
            self.texto_relatorio.insert(tk.END, "Nenhum animal disponível")
        else:
            for animal in self.pet_shop.animais:
                self.texto_relatorio.insert(tk.END, f"🔊 {animal.nome}: {animal.fazer_som()}\n")
    
    def executar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PetShopGUI()
    app.executar()