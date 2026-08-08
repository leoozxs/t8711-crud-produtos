import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


from app.models.cidade import Cidade

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Cidade_View:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self._estados = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
        
    def configurar_janela(self):
        self.root.title("CRUD de Cidades")
        self.root.geometry("680x600")
        self.root.resizable(False,False)
    
    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text="Cadastro de Cidades",
            font=("Arial",16,"bold")
        )
        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=5,
        )
        self.frm_dados = tk.LabelFrame(
           self.root,
           text="Dados da Cidade",
           labelanchor="n"
        )
        self.frm_dados.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=10,
            pady=5,
            sticky="ew"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text="ID"
        )
        self.lbl_id.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width=6,
            state="readonly"
        )
        self.txt_id.grid(
            row=0,
            column=0,
            sticky="e",
            padx=20
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text="Nome"
        )
        self.lbl_nome.grid(
            row=0,
            column=1,
            padx=10,
            sticky="w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_nome.grid(
            row=0,
            column=1,
            sticky="e"
        )
        self.lbl_estado = tk.Label(
            self.frm_dados,
            text="Estado"
        )
        self.lbl_estado.grid(
            row=0,
            column=2,
            sticky="w",
            padx=20
        )
        self.cmb_estados = ttk.Combobox(
            self.frm_dados,
            width=25,
            state="readonly"
        )
        self.cmb_estados.grid(
            row=0,
            column=2,
            padx=10,
            sticky="e"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = "Novo",
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = "Salvar",
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = "Alterar",
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = "Excluir",
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = "Fechar",
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
    
    def configurar_treeview(self):
        self.tbl_cidades = ttk.Treeview(
            self.root,
            height=17
        )
        self.tbl_cidades.grid(
            row=2,
            column=0,
            columnspan=4,
            padx=10,
            pady=10,
            sticky="nsew"
        )
        
        self.tbl_cidades["columns"] = (
            "id",
            "nome",
            "estado"
        )
        self.tbl_cidades.column(
            "#0",
            width=0,
            stretch=False
        )
        self.tbl_cidades.column(
            "id",
            width=10,
            anchor="center"
        )
        self.tbl_cidades.column(
            "nome",
            width=30
        )
        self.tbl_cidades.column(
            "estado",
            width=30
        )
        self.tbl_cidades.heading(
            "id",
            text="ID"
        )
        self.tbl_cidades.heading(
            "nome",
            text="Nome"
        )
        self.tbl_cidades.heading(
            "estado",
            text="Estado"
        )
        
        
    def configurar_eventos(self):
        self.btn_novo.config(
            command=self.controller.new
        )
        self.btn_salvar.config(
            command=self.controller.save
        )
        self.btn_alterar.config(
            command=self.controller.update
        )
        self.btn_excluir.config(
            command=self.controller.delete
        )
        self.btn_fechar.config(
            command=self.fechar
        )
        self.tbl_cidades.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_produto
        )

    def carregar_estados(self, estados):
        self._estados = estados
        valores = []
        for estado in estados:
            valores.append(
                f"{estado.id} - {estado.nome}"
            )
        self.cmb_estados["values"] = valores
        self.cmb_estados.set("")
    
    def preencher_campos(self, estado):
        pass
    
    def limpar_campos(self):
        pass
    
    def limpar_treeview(self):
        pass
    
    def get_id_selecionado(self):
        pass
    
    def confirmar_exclusao(self):
        pass
    
    def ler_dados_estado(self):
        pass
    
    def exibir_mensagem(self):
        pass
    
    def exibir_estados(self):
        pass
    
    def fechar(self):
        self.root.destroy()
    
    def iniciar(self):
        self.controller.carregar_fornecedores()
        self.controller.get_all()
        self.root.mainloop()
        

if __name__ == "__main__":
    root = tk.Tk()
    Cidade_View(root)
    root.mainloop()