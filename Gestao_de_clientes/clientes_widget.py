from functools import partial
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
)

import sqlite3

class ClientesWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        # 🔍 Linha de filtros lado a lado
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

        # Adiciona todos os campos e botão ao layout horizontal
        filtro_layout.addWidget(self.nome_input)
        filtro_layout.addWidget(self.usuario_input)
        filtro_layout.addWidget(self.senha_input)
        filtro_layout.addWidget(self.email_input)
        filtro_layout.addWidget(self.data_criacao_input)
        filtro_layout.addWidget(self.expiracao_input)
        filtro_layout.addWidget(self.status_input)
        filtro_layout.addWidget(self.telas_input)
        filtro_layout.addWidget(self.criado_por_input)
        filtro_layout.addWidget(self.btn_pesquisar)

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

            colunas = ["Nome", "Usuário", "Senha", "Email", "Data Criação", "Expiração", "Status", "Telas", "Criado por", "Excluir"]
            self.tabela.setColumnCount(len(colunas))
            self.tabela.setRowCount(len(dados))
            self.tabela.setHorizontalHeaderLabels(colunas)

            for i, linha in enumerate(dados):
                for j, valor in enumerate(linha):
                    self.tabela.setItem(i, j, QTableWidgetItem(str(valor)))

                # Botão de excluir na última coluna
                btn_excluir = QPushButton("🗑️ Excluir")
                btn_excluir.clicked.connect(partial(self.excluir_linha, i))
                self.tabela.setCellWidget(i, len(colunas) - 1, btn_excluir)

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

    def excluir_linha(self, row):
        usuario = self.tabela.item(row, 1).text()  # coluna 1 = usuário

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

                self.tabela.removeRow(row)  # remove da interface

            except Exception as e:
                print(f"Erro ao excluir: {e}")

        

