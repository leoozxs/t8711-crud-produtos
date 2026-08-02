import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
 
from app.models.estado import Estado
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Estado_View:
    def __init__(self, root, controller=None):
        self.controller = controller
        self.root = root
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Estados")
        self.root.geometry("500x600")
        self.root.resizable(False,False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text="Gestão de Estados",
            font=("Arial",16,"bold")
        )
        self.lbl_titulo.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=5,
            pady=5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text="Dados do estado",
            labelanchor="n"
        )
        self.frm_dados.grid(
            row=1,
            column=3,
            padx=13
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text="ID"
        )
        self.lbl_id.grid(
            row=0,
            column=0,
            padx=20,
            pady=5,
            sticky="w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width=5,
            state="readonly"
        )
        self.txt_id.grid(
            row=0,
            column=0,
            padx=20,
            pady=5
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text="Nome"
        )
        self.lbl_nome.grid(
            row=0,
            column=1,
            pady=5,
            sticky="w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width=20
        )
        self.txt_nome.grid(
            row=0,
            column=1,
            pady=5,
            sticky="e"
        ) 
        self.lbl_sigla = tk.Label(
            self.frm_dados,
            text="Sigla"
        )
        self.lbl_sigla.grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
            sticky="e"
        )
        self.txt_sigla = tk.Entry(
            self.frm_dados,
            width=5
        )
        self.txt_sigla.grid(
            row=0,
            column=3,
            pady=5,
            sticky="w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border=2,
            relief="groove"
        )
        self.frm_botoes.grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            columnspan=4
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text="Novo",
            width=10
        )
        self.btn_novo.grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text="Salvar",
            width=10
        )
        self.btn_salvar.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text="Alterar",
            width=10
        )
        self.btn_alterar.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text="Excluir",
            width=10
        )
        self.btn_excluir.grid(
            row=0,
            column=4,
            padx=5,
            pady=5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text="Fechar",
            width=10
        )
        self.btn_fechar.grid(
            row=0,
            column=5,
            padx=5,
            pady=5
        )


    def configurar_treeview(self):
        self.tbl_estados = ttk.Treeview(
            self.root,
            columns=("id", "nome", "sigla"),
            show="headings",
            height=20            
        )
        self.tbl_estados.grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            columnspan=4,
            sticky="nsew"
        )
        self.tbl_estados["columns"] = (
            "id",
            "nome",
            "sigla"
        )
        self.tbl_estados.column(
            "#0",
            width=0,
            stretch=False
        )
        self.tbl_estados.column(
            "id",
            width=5
        )
        self.tbl_estados.column(
            "nome",
            width=10
        )
        self.tbl_estados.column(
            "sigla",
            width=5
        )
        self.tbl_estados.heading(
            "id",
            text="ID"
        )
        self.tbl_estados.heading(
            "nome",
            text="Nome"
        )
        self.tbl_estados.heading(
            "sigla",
            text="Sigla"
        )

    def configurar_eventos(self):
        pass

    def iniciar(self):
        self.root.mainloop()

e = Estado_View(tk.Tk())
e.iniciar()
        