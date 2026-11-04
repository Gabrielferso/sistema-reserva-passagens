import tkinter as tk
from tkinter import ttk, messagebox

from data import banco
from data.persistencia import salvar_banco
from models.passageiro import Passageiro
from models.voo import Voo
from models.reserva import Reserva
from models.hotel import Hotel
from models.quarto import Quarto
from models.hospedagem import Hospedagem
from models.pacote import Pacote

# Paleta baseada na imagem de referência
NAVY = "#001027"
BABY_BLUE = "#62C8F4"
BUTTON_BLUE = "#0785C9"
CONTENT_BG = "#DCDCDC"
WHITE = "#FFFFFF"
TEXT = "#101010"
MUTED = "#D4DCE5"


class JanelaPrincipal:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("IN-DOALI | Sistema de Reservas")
        self.janela.geometry("1000x707")
        self.janela.minsize(850, 600)
        self.janela.configure(bg=NAVY)

        self.modulo_atual = "Passageiros"
        self.botoes_menu = {}

        self._configurar_estilos()
        self._montar_cabecalho()
        self._montar_menu_lateral()
        self._montar_conteudo()
        self.mostrar_modulo("Passageiros")

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Tabela.Treeview",
            background=CONTENT_BG,
            foreground=TEXT,
            fieldbackground=CONTENT_BG,
            rowheight=42,
            font=("Arial", 11),
            borderwidth=0
        )
        style.configure(
            "Tabela.Treeview.Heading",
            background=CONTENT_BG,
            foreground=TEXT,
            font=("Arial", 11, "bold"),
            relief="flat",
            padding=(8, 12)
        )
        style.map("Tabela.Treeview", background=[("selected", "#B8DDF0")])

    def _montar_cabecalho(self):
        header = tk.Frame(self.janela, bg=NAVY, height=100)
        header.pack(side="top", fill="x")
        header.pack_propagate(False)

        logo = tk.Label(
            header, text="✈ IN-DOALI", bg=NAVY, fg=WHITE,
            font=("Arial", 19, "bold")
        )
        logo.pack(side="left", padx=32)

        links = tk.Frame(header, bg=NAVY)
        links.pack(side="right", padx=65, fill="y")
        for texto, mensagem in [
            ("Dúvidas", "Entre em contato com a equipe responsável pelo sistema."),
            ("Contato", "IN-DOALI — Sistema de Reserva de Passagens Aéreas."),
            ("Sobre nós", "Projeto acadêmico desenvolvido pela equipe IN-DOALI.")
        ]:
            tk.Button(
                links, text=texto, bg=NAVY, fg=MUTED,
                activebackground=NAVY, activeforeground=WHITE,
                font=("Arial", 11, "bold"), bd=0, cursor="hand2",
                command=lambda t=texto, m=mensagem: messagebox.showinfo(t, m)
            ).pack(side="left", padx=42, pady=35)

    def _montar_menu_lateral(self):
        self.sidebar = tk.Frame(self.janela, bg=NAVY, width=166)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        modulos = [
            "Passageiros", "Voos", "Reservas", "Hotéis e quartos",
            "Hospedagens", "Pacotes", "Consulta de pedidos"
        ]
        for modulo in modulos:
            botao = tk.Button(
                self.sidebar, text=modulo, bg=NAVY, fg=MUTED,
                activebackground=NAVY, activeforeground=BABY_BLUE,
                font=("Arial", 10, "bold"), bd=0, relief="flat",
                cursor="hand2", anchor="center", pady=17,
                command=lambda m=modulo: self.mostrar_modulo(m)
            )
            botao.pack(fill="x", padx=7, pady=2)
            self.botoes_menu[modulo] = botao

    def _montar_conteudo(self):
        self.area = tk.Frame(self.janela, bg=CONTENT_BG)
        self.area.pack(side="left", fill="both", expand=True)

        self.acoes = tk.Frame(self.area, bg=CONTENT_BG)
        self.acoes.pack(fill="x", padx=32, pady=(60, 58))

        self.botao_principal = tk.Button(
            self.acoes, text="", bg=BUTTON_BLUE, fg=WHITE,
            activebackground="#006EAA", activeforeground=WHITE,
            font=("Arial", 11, "bold"), bd=0, relief="flat",
            cursor="hand2", padx=24, pady=15,
            command=self.executar_acao_principal
        )
        self.botao_principal.pack(side="left")

        self.botao_secundario = tk.Button(
            self.acoes, text="", bg="#B9C7D1", fg=TEXT,
            activebackground="#AABBC7", font=("Arial", 10, "bold"),
            bd=0, cursor="hand2", padx=16, pady=14
        )

        self.titulo_tabela = tk.Label(
            self.area, text="", bg=CONTENT_BG, fg=TEXT,
            font=("Arial", 11, "bold")
        )
        self.titulo_tabela.pack(anchor="w", padx=32, pady=(0, 20))

        self.frame_tabela = tk.Frame(self.area, bg=CONTENT_BG)
        self.frame_tabela.pack(fill="both", expand=True, padx=25, pady=(0, 12))

    def mostrar_modulo(self, modulo):
        self.modulo_atual = modulo

        # A opção ativa fica azul-bebê; as demais continuam claras.
        for nome, botao in self.botoes_menu.items():
            selecionado = nome == modulo
            botao.configure(
                fg=BABY_BLUE if selecionado else MUTED,
                activeforeground=BABY_BLUE if selecionado else WHITE
            )

        configuracoes = {
            "Passageiros": ("Cadastrar novo passageiro", "Passageiros cadastrados:"),
            "Voos": ("Cadastrar novo voo", "Voos cadastrados:"),
            "Reservas": ("Criar nova reserva", "Reservas cadastradas:"),
            "Hotéis e quartos": ("Cadastrar novo hotel", "Hotéis e quartos cadastrados:"),
            "Hospedagens": ("Criar nova hospedagem", "Hospedagens cadastradas:"),
            "Pacotes": ("Criar novo pacote", "Pacotes cadastrados:"),
            "Consulta de pedidos": ("Cancelar pedido selecionado", "Pedidos cadastrados:")
        }
        texto_botao, titulo = configuracoes[modulo]
        self.botao_principal.configure(text=texto_botao)
        self.titulo_tabela.configure(text=titulo)

        if modulo == "Hotéis e quartos":
            self.botao_secundario.configure(
                text="Cadastrar quarto", command=self.formulario_quarto
            )
            self.botao_secundario.pack(side="left", padx=12)
        elif modulo == "Consulta de pedidos":
            self.botao_secundario.configure(
                text="Atualizar lista", command=self.atualizar_tabela
            )
            self.botao_secundario.pack(side="left", padx=12)
        else:
            self.botao_secundario.pack_forget()

        self.atualizar_tabela()

    def _dados_tabela(self):
        if self.modulo_atual == "Passageiros":
            return (["ID", "Nome", "Documento", "Telefone", "E-mail"],
                    [[p.id, p.nome, p.documento, p.telefone, p.email] for p in banco.passageiros])

        if self.modulo_atual == "Voos":
            return (["ID", "Origem", "Destino", "Data", "Horário", "Aeronave", "Capacidade"],
                    [[v.id, v.origem, v.destino, v.data, v.horario, v.aeronave, v.capacidade] for v in banco.voos])

        if self.modulo_atual == "Reservas":
            return (["ID", "Passageiro", "Voo", "Assento", "Valor", "Status"],
                    [[r.id, r.passageiro_id, r.voo_id, r.assento, f"R$ {r.valor:.2f}", "Ativa" if r.ativa else "Cancelada"] for r in banco.reservas])

        if self.modulo_atual == "Hotéis e quartos":
            linhas = []
            for h in banco.hoteis:
                linhas.append([h.id, h.nome, h.cidade, "Hotel", "—", "—"])
                for q in h.quartos:
                    linhas.append([q.id, h.nome, h.cidade, f"Quarto {q.numero}", q.capacidade, f"R$ {q.diaria:.2f}"])
            return (["ID", "Hotel", "Cidade", "Tipo", "Capacidade", "Diária"], linhas)

        if self.modulo_atual == "Hospedagens":
            return (["ID", "Passageiro", "Hotel", "Quarto", "Entrada", "Saída", "Valor", "Status"],
                    [[h.id, h.passageiro_id, h.hotel_id, h.quarto_id, h.entrada, h.saida, f"R$ {h.valor:.2f}", "Ativa" if h.ativa else "Cancelada"] for h in banco.hospedagens])

        if self.modulo_atual == "Pacotes":
            return (["ID", "Reserva", "Hospedagem", "Valor adicional", "Status"],
                    [[p.id, p.reserva_id, p.hospedagem_id, f"R$ {p.valor:.2f}", "Ativo" if p.ativo else "Cancelado"] for p in banco.pacotes])

        linhas = []
        for r in banco.reservas:
            linhas.append(["Reserva", r.id, r.passageiro_id, r.voo_id, "Ativa" if r.ativa else "Cancelada"])
        for h in banco.hospedagens:
            linhas.append(["Hospedagem", h.id, h.passageiro_id, h.hotel_id, "Ativa" if h.ativa else "Cancelada"])
        for p in banco.pacotes:
            linhas.append(["Pacote", p.id, p.reserva_id, p.hospedagem_id, "Ativo" if p.ativo else "Cancelado"])
        return (["Tipo", "ID", "Referência 1", "Referência 2", "Status"], linhas)

    def atualizar_tabela(self):
        for widget in self.frame_tabela.winfo_children():
            widget.destroy()

        colunas, linhas = self._dados_tabela()
        tabela = ttk.Treeview(
            self.frame_tabela, columns=colunas, show="headings",
            style="Tabela.Treeview", height=12
        )
        for coluna in colunas:
            tabela.heading(coluna, text=coluna)
            tabela.column(coluna, width=max(100, int(700 / len(colunas))), minwidth=80, anchor="w")
        for linha in linhas:
            tabela.insert("", "end", values=linha)

        scroll = ttk.Scrollbar(self.frame_tabela, orient="vertical", command=tabela.yview)
        tabela.configure(yscrollcommand=scroll.set)
        tabela.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.tabela = tabela

    def executar_acao_principal(self):
        acoes = {
            "Passageiros": self.formulario_passageiro,
            "Voos": self.formulario_voo,
            "Reservas": self.formulario_reserva,
            "Hotéis e quartos": self.formulario_hotel,
            "Hospedagens": self.formulario_hospedagem,
            "Pacotes": self.formulario_pacote,
            "Consulta de pedidos": self.cancelar_pedido_selecionado
        }
        acoes[self.modulo_atual]()

    def abrir_formulario(self, titulo, campos, ao_salvar):
        tela = tk.Toplevel(self.janela)
        tela.title(titulo)
        tela.configure(bg=CONTENT_BG)
        tela.resizable(False, False)
        tela.transient(self.janela)
        tela.grab_set()

        tk.Label(tela, text=titulo, bg=CONTENT_BG, fg=TEXT,
                 font=("Arial", 15, "bold")).pack(padx=25, pady=(22, 12))
        frame = tk.Frame(tela, bg=CONTENT_BG)
        frame.pack(padx=25, pady=5)
        entradas = {}

        for i, (chave, rotulo) in enumerate(campos):
            tk.Label(frame, text=rotulo, bg=CONTENT_BG, fg=TEXT,
                     font=("Arial", 10, "bold")).grid(row=i, column=0, sticky="w", pady=7, padx=(0, 12))
            entrada = tk.Entry(frame, width=34, font=("Arial", 10), relief="solid", bd=1)
            entrada.grid(row=i, column=1, pady=7)
            entradas[chave] = entrada

        def salvar():
            valores = {chave: campo.get().strip() for chave, campo in entradas.items()}
            if any(not valor for valor in valores.values()):
                messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=tela)
                return
            try:
                ao_salvar(valores)
                salvar_banco()
                tela.destroy()
                self.atualizar_tabela()
                messagebox.showinfo("Sucesso", "Operação realizada com sucesso.", parent=self.janela)
            except (ValueError, TypeError, KeyError) as erro:
                messagebox.showerror("Não foi possível salvar", str(erro), parent=tela)

        tk.Button(tela, text="Salvar", command=salvar, bg=BUTTON_BLUE, fg=WHITE,
                  activebackground="#006EAA", font=("Arial", 10, "bold"),
                  bd=0, padx=25, pady=10, cursor="hand2").pack(pady=20)

    def formulario_passageiro(self):
        def salvar(v):
            if any(p.documento == v["documento"] for p in banco.passageiros):
                raise ValueError("Já existe um passageiro com esse documento.")
            banco.passageiros.append(Passageiro(banco.novo_id("passageiro"), v["nome"], v["documento"], v["telefone"], v["email"]))
        self.abrir_formulario("Cadastrar passageiro", [("nome", "Nome"), ("documento", "Documento"), ("telefone", "Telefone"), ("email", "E-mail")], salvar)

    def formulario_voo(self):
        def salvar(v):
            capacidade = int(v["capacidade"])
            if capacidade <= 0 or v["origem"].lower() == v["destino"].lower():
                raise ValueError("Informe uma capacidade positiva e origens/destinos diferentes.")
            banco.voos.append(Voo(banco.novo_id("voo"), v["origem"], v["destino"], v["data"], v["horario"], v["aeronave"], capacidade))
        self.abrir_formulario("Cadastrar voo", [("origem", "Aeroporto/cidade de origem"), ("destino", "Aeroporto/cidade de destino"), ("data", "Data (DD/MM/AAAA)"), ("horario", "Horário (HH:MM)"), ("aeronave", "Aeronave"), ("capacidade", "Capacidade")], salvar)

    def formulario_hotel(self):
        def salvar(v):
            banco.hoteis.append(Hotel(banco.novo_id("hotel"), v["nome"], v["cidade"]))
        self.abrir_formulario("Cadastrar hotel", [("nome", "Nome do hotel"), ("cidade", "Cidade")], salvar)

    def formulario_quarto(self):
        if not banco.hoteis:
            messagebox.showwarning("Atenção", "Cadastre um hotel antes de cadastrar quartos.")
            return
        def salvar(v):
            hotel = next((h for h in banco.hoteis if h.id == int(v["hotel_id"])), None)
            if hotel is None:
                raise ValueError("Hotel não encontrado. Informe um ID existente.")
            capacidade, diaria = int(v["capacidade"]), float(v["diaria"].replace(",", "."))
            if capacidade <= 0 or diaria < 0:
                raise ValueError("Capacidade deve ser positiva e diária não pode ser negativa.")
            if any(q.numero == v["numero"] for q in hotel.quartos):
                raise ValueError("Esse quarto já existe nesse hotel.")
            hotel.quartos.append(Quarto(banco.novo_id("quarto"), v["numero"], capacidade, diaria))
        self.abrir_formulario("Cadastrar quarto", [("hotel_id", "ID do hotel"), ("numero", "Número do quarto"), ("capacidade", "Capacidade"), ("diaria", "Valor da diária")], salvar)

    def formulario_reserva(self):
        def salvar(v):
            pid, vid = int(v["passageiro_id"]), int(v["voo_id"])
            voo = next((x for x in banco.voos if x.id == vid), None)
            if not any(p.id == pid for p in banco.passageiros) or voo is None:
                raise ValueError("Passageiro ou voo não encontrado.")
            if sum(1 for r in banco.reservas if r.voo_id == vid and r.ativa) >= voo.capacidade:
                raise ValueError("Esse voo já atingiu a capacidade.")
            assento = v["assento"].upper()
            if any(r.voo_id == vid and r.assento == assento and r.ativa for r in banco.reservas):
                raise ValueError("Esse assento já está ocupado.")
            valor = float(v["valor"].replace(",", "."))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            banco.reservas.append(Reserva(banco.novo_id("reserva"), pid, vid, assento, valor))
        self.abrir_formulario("Criar reserva", [("passageiro_id", "ID do passageiro"), ("voo_id", "ID do voo"), ("assento", "Assento"), ("valor", "Valor da passagem")], salvar)

    def formulario_hospedagem(self):
        def salvar(v):
            pid, hid, qid = int(v["passageiro_id"]), int(v["hotel_id"]), int(v["quarto_id"])
            hotel = next((h for h in banco.hoteis if h.id == hid), None)
            quarto = next((q for q in hotel.quartos if q.id == qid), None) if hotel else None
            if not any(p.id == pid for p in banco.passageiros) or hotel is None or quarto is None:
                raise ValueError("Confira os IDs do passageiro, hotel e quarto.")
            from services.util import data_obj
            entrada, saida = v["entrada"], v["saida"]
            if data_obj(saida) <= data_obj(entrada):
                raise ValueError("A saída deve ser posterior à entrada.")
            for h in banco.hospedagens:
                if h.quarto_id == qid and h.ativa and data_obj(entrada) < data_obj(h.saida) and data_obj(saida) > data_obj(h.entrada):
                    raise ValueError("Esse quarto já está reservado nesse período.")
            valor = (data_obj(saida) - data_obj(entrada)).days * quarto.diaria
            banco.hospedagens.append(Hospedagem(banco.novo_id("hospedagem"), pid, hid, qid, entrada, saida, valor))
        self.abrir_formulario("Criar hospedagem", [("passageiro_id", "ID do passageiro"), ("hotel_id", "ID do hotel"), ("quarto_id", "ID do quarto"), ("entrada", "Entrada (DD/MM/AAAA)"), ("saida", "Saída (DD/MM/AAAA)")], salvar)

    def formulario_pacote(self):
        def salvar(v):
            rid, hid = int(v["reserva_id"]), int(v["hospedagem_id"])
            reserva = next((r for r in banco.reservas if r.id == rid and r.ativa), None)
            hospedagem = next((h for h in banco.hospedagens if h.id == hid and h.ativa), None)
            if reserva is None or hospedagem is None:
                raise ValueError("Informe uma reserva e uma hospedagem ativas.")
            if reserva.passageiro_id != hospedagem.passageiro_id:
                raise ValueError("A reserva e a hospedagem devem pertencer ao mesmo passageiro.")
            if any(p.ativo and (p.reserva_id == rid or p.hospedagem_id == hid) for p in banco.pacotes):
                raise ValueError("A reserva ou hospedagem já pertence a outro pacote.")
            valor = float(v["valor"].replace(",", "."))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            banco.pacotes.append(Pacote(banco.novo_id("pacote"), rid, hid, valor))
        self.abrir_formulario("Criar pacote", [("reserva_id", "ID da reserva"), ("hospedagem_id", "ID da hospedagem"), ("valor", "Valor adicional")], salvar)

    def cancelar_pedido_selecionado(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione um pedido na tabela.")
            return
        valores = self.tabela.item(selecionado[0], "values")
        tipo, identificador = valores[0], int(valores[1])
        if not messagebox.askyesno("Confirmar cancelamento", f"Deseja cancelar {tipo.lower()} {identificador}?"):
            return

        if tipo == "Reserva":
            item = next((r for r in banco.reservas if r.id == identificador), None)
            if item and item.ativa:
                item.ativa = False
            else:
                messagebox.showwarning("Atenção", "Reserva não encontrada ou já cancelada.")
                return
        elif tipo == "Hospedagem":
            item = next((h for h in banco.hospedagens if h.id == identificador), None)
            if item and item.ativa:
                item.ativa = False
            else:
                messagebox.showwarning("Atenção", "Hospedagem não encontrada ou já cancelada.")
                return
        else:
            item = next((p for p in banco.pacotes if p.id == identificador), None)
            if item and item.ativo:
                item.ativo = False
                reserva = next((r for r in banco.reservas if r.id == item.reserva_id), None)
                hospedagem = next((h for h in banco.hospedagens if h.id == item.hospedagem_id), None)
                if reserva:
                    reserva.ativa = False
                if hospedagem:
                    hospedagem.ativa = False
            else:
                messagebox.showwarning("Atenção", "Pacote não encontrado ou já cancelado.")
                return

        salvar_banco()
        self.atualizar_tabela()
        messagebox.showinfo("Sucesso", "Pedido cancelado.")


def abrir_janela():
    janela = tk.Tk()
    JanelaPrincipal(janela)
    janela.mainloop()