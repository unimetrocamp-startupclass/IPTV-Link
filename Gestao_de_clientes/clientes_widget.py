from functools import partial
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox,
    QDialog, QFormLayout
)
import sqlite3

class ClientesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # 🔍 Linha de filtros
        filtro_layout = QHBoxLayout()

        self.nome_input = QLineEdit(); self.nome_input.setPlaceholderText("Nome")
        self.usuario_input = QLineEdit(); self.usuario_input.setPlaceholderText("Usuário")
        self.senha_input = QLineEdit(); self.senha_input.setPlaceholderText("Senha")
        self.email_input = QLineEdit(); self.email_input.setPlaceholderText("Email")
        self.data_criacao_input = QLineEdit(); self.data_criacao_input.setPlaceholderText("Data Criação")
        self.expiracao_input = QLineEdit(); self.expiracao_input.setPlaceholderText("Expiração")
        self.status_input = QLineEdit(); self.status_input.setPlaceholderText("Status")
        self.telas_input = QLineEdit(); self.telas_input.setPlaceholderText("Telas")
        self.criado_por_input = QLineEdit(); self.criado_por_input.setPlaceholderText("Criado por")

        self.btn_pesquisar = QPushButton("🔍 Pesquisar")
        self.btn_pesquisar.clicked.connect(self.filtrar_dados)

        # Adiciona todos os campos ao layout de filtro
        for widget in [
            self.nome_input, self.usuario_input, self.senha_input,
            self.email_input, self.data_criacao_input, self.expiracao_input,
            self.status_input, self.telas_input, self.criado_por_input, self.btn_pesquisar
        ]:
            filtro_layout.addWidget(widget)

        # 🧾 Tabela
        self.tabela = QTableWidget()
        self.carregar_dados()  # Mostra todos inicialmente

        layout.addWidget(QLabel("Lista de Clientes"))
        layout.addLayout(filtro_layout)
        layout.addWidget(self.tabela)
        self.setLayout(layout)

    def carregar_dados(self, filtros=None):
        try:
            conn = sqlite3.connect("usuarios.db")
            cursor = conn.cursor()

            query = "SELECT nome, usuario, senha, email, data_criacao, expiracao, status, telas, criado_por FROM usuarios"
            parametros = []
            condicoes = []

            if filtros:
                for campo, valor in filtros.items():
                    if valor:
                        condicoes.append(f"{campo} LIKE ?")
                        parametros.append(f"%{valor}%")

            if condicoes:
                query += " WHERE " + " AND ".join(condicoes)

            cursor.execute(query, parametros)
            dados = cursor.fetchall()
            conn.close()

            colunas = ["Nome", "Usuário", "Senha", "Email", "Data Criação", "Expiração", "Status", "Telas", "Criado por", "Ações"]
            self.tabela.setColumnCount(len(colunas))
            self.tabela.setRowCount(len(dados))
            self.tabela.setHorizontalHeaderLabels(colunas)

            for i, linha in enumerate(dados):
                for j, valor in enumerate(linha):
                    self.tabela.setItem(i, j, QTableWidgetItem(str(valor)))

                # Botões de editar e excluir
                btn_editar = QPushButton("✏️ Editar")
                btn_editar.clicked.connect(lambda _, b=btn_editar: self.editar_linha(b))  

                btn_excluir = QPushButton("🗑️ Excluir")
                btn_excluir.clicked.connect(lambda _, b=btn_excluir: self.excluir_linha(b))  

                botoes_layout = QHBoxLayout()
                botoes_layout.addWidget(btn_editar)
                botoes_layout.addWidget(btn_excluir)

                widget_botoes = QWidget()
                widget_botoes.setLayout(botoes_layout)

                self.tabela.setCellWidget(i, len(colunas) - 1, widget_botoes)
                self.tabela.setRowHeight(i, 45)


            self.tabela.resizeColumnsToContents()

        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    def filtrar_dados(self):
        filtros = {
            "nome": self.nome_input.text().strip(),
            "usuario": self.usuario_input.text().strip(),
            "senha": self.senha_input.text().strip(),
            "email": self.email_input.text().strip(),
            "data_criacao": self.data_criacao_input.text().strip(),
            "expiracao": self.expiracao_input.text().strip(),
            "status": self.status_input.text().strip(),
            "telas": self.telas_input.text().strip(),
            "criado_por": self.criado_por_input.text().strip(),
        }
        self.carregar_dados(filtros=filtros)

    def excluir_linha(self, botao):
        row = self.tabela.indexAt(botao.parent().pos()).row()
        if row < 0:
            return

        usuario = self.tabela.item(row, 1).text()

        confirmacao = QMessageBox.question(
            self,
            "Confirmar exclusão",
            f"Tem certeza que deseja excluir o cliente '{usuario}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )

        if confirmacao == QMessageBox.StandardButton.Yes:
            try:
                conn = sqlite3.connect("usuarios.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM usuarios WHERE usuario = ?", (usuario,))
                conn.commit()
                conn.close()

                self.carregar_dados()

            except Exception as e:
                print(f"Erro ao excluir: {e}")



    def editar_linha(self, botao):
        row = self.tabela.indexAt(botao.parent().pos()).row()
        if row < 0:
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Editar Cliente")
        layout = QFormLayout()

        campos = ["nome", "usuario", "senha", "email", "data_criacao", "expiracao", "status", "telas", "criado_por"]
        inputs = {}

        for i, campo in enumerate(campos):
            valor = self.tabela.item(row, i).text()
            entrada = QLineEdit(valor)
            inputs[campo] = entrada
            layout.addRow(campo.capitalize(), entrada)

        btn_salvar = QPushButton("💾 Salvar")
        usuario_original = self.tabela.item(row, 1).text()
        btn_salvar.clicked.connect(lambda: self.salvar_edicao(row, inputs, dialog, usuario_original))

        layout.addRow(btn_salvar)

        dialog.setLayout(layout)
        dialog.exec()



    def salvar_edicao(self, row, inputs, dialog, usuario_original):
        try:
            dados = {campo: inputs[campo].text().strip() for campo in inputs}

            conn = sqlite3.connect("usuarios.db")
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE usuarios
                SET nome = ?, usuario = ?, senha = ?, email = ?, data_criacao = ?, expiracao = ?, status = ?, telas = ?, criado_por = ?
                WHERE usuario = ?
            """, (
                dados["nome"], dados["usuario"], dados["senha"], dados["email"],
                dados["data_criacao"], dados["expiracao"], dados["status"],
                dados["telas"], dados["criado_por"], usuario_original
            ))
            conn.commit()
            conn.close()

            self.carregar_dados()
            dialog.accept()

        except Exception as e:
            print(f"Erro ao salvar edição: {e}")

