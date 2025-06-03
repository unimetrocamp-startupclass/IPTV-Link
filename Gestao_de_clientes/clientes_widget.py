from functools import partial
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox,
    QDialog, QFormLayout, QCheckBox, QTextEdit
)
from PyQt6.QtCore import Qt
import sqlite3
import subprocess
import threading
import os

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

        for widget in [
            self.nome_input, self.usuario_input, self.senha_input,
            self.email_input, self.data_criacao_input, self.expiracao_input,
            self.status_input, self.telas_input, self.criado_por_input, self.btn_pesquisar
        ]:
            filtro_layout.addWidget(widget)

        # 🧾 Tabela
        self.tabela = QTableWidget()
        layout.addWidget(QLabel("Lista de Clientes"))
        layout.addLayout(filtro_layout)
        layout.addWidget(self.tabela)

        # 📩 Caixa de mensagem e botão de envio
        self.mensagem_input = QTextEdit()
        self.mensagem_input.setPlaceholderText("Digite a mensagem para enviar pelo WhatsApp...")
        layout.addWidget(self.mensagem_input)

        self.btn_enviar_mensagem = QPushButton("📨 Enviar mensagens para selecionados")
        self.btn_enviar_mensagem.clicked.connect(self.enviar_mensagens)
        layout.addWidget(self.btn_enviar_mensagem)

        self.setLayout(layout)
        self.carregar_dados()

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

            colunas = ["✔", "Nome", "Usuário", "Senha", "Email", "Data Criação", "Expiração", "Status", "Telas", "Criado por", "Ações"]
            self.tabela.setColumnCount(len(colunas))
            self.tabela.setRowCount(len(dados))
            self.tabela.setHorizontalHeaderLabels(colunas)

            for i, linha in enumerate(dados):
                # Checkbox
                checkbox = QCheckBox()
                checkbox_layout = QHBoxLayout()
                checkbox_layout.addWidget(checkbox)
                checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                checkbox_widget = QWidget()
                checkbox_widget.setLayout(checkbox_layout)
                self.tabela.setCellWidget(i, 0, checkbox_widget)

                for j, valor in enumerate(linha):
                    self.tabela.setItem(i, j + 1, QTableWidgetItem(str(valor)))

                # Botões de ação
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

    def enviar_mensagens(self):
        mensagem = self.mensagem_input.toPlainText().strip()
        if not mensagem:
            QMessageBox.warning(self, "Mensagem vazia", "Digite uma mensagem para enviar.")
            return

        telefones = []
        for row in range(self.tabela.rowCount()):
            checkbox_widget = self.tabela.cellWidget(row, 0)
            if checkbox_widget:
                checkbox = checkbox_widget.findChild(QCheckBox)
                if checkbox and checkbox.isChecked():
                    telefone_item = self.tabela.item(row, 1)  # Nome (telefone) agora está na coluna 1
                    if telefone_item:
                        telefones.append(telefone_item.text())

        if not telefones:
            QMessageBox.warning(self, "Nenhum cliente selecionado", "Selecione ao menos um cliente para enviar a mensagem.")
            return

        thread = threading.Thread(target=self.enviar_whatsapp, args=(telefones, mensagem))
        thread.start()

    def enviar_whatsapp(self, telefones, mensagem):
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.by import By
            from selenium.webdriver.common.keys import Keys
            import time

            options = Options()
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver = webdriver.Chrome(options=options)

            for telefone in telefones:
                numero = f'+55{telefone}'
                driver.get(f'https://web.whatsapp.com/send?phone={numero}&text={mensagem}')
                time.sleep(6)
                try:
                    caixa = driver.find_element(By.XPATH, '//div[@data-tab="10"][@contenteditable="true"]')
                    caixa.send_keys(Keys.ENTER)
                    print(f"[✓] Mensagem enviada para {telefone}")
                except Exception as e:
                    print(f"[X] Falha ao enviar para {telefone}: {e}")
                time.sleep(3)

            driver.quit()

            

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao enviar mensagens: {e}")

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
        self.carregar_dados(filtros)

    def excluir_linha(self, botao):
        row = self.tabela.indexAt(botao.parent().pos()).row()
        if row < 0:
            return

        usuario = self.tabela.item(row, 2).text()

        confirmacao = QMessageBox.question(
            self, "Confirmar exclusão",
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
            valor = self.tabela.item(row, i + 1).text()
            entrada = QLineEdit(valor)
            inputs[campo] = entrada
            layout.addRow(campo.capitalize(), entrada)

        btn_salvar = QPushButton("💾 Salvar")
        usuario_original = self.tabela.item(row, 2).text()
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
