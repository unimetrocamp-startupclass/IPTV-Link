from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sqlite3
from datetime import datetime

class CadastroWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.campos = {
            "nome": QLineEdit(),
            "usuario": QLineEdit(),
            "senha": QLineEdit(),
            "email": QLineEdit(),
            "data_criacao": QLineEdit(datetime.now().strftime("%Y-%m-%d")),
            "expiracao": QLineEdit(""),
            "status": QLineEdit("ativo"),
            "telas": QLineEdit("clientes,config"),
            "criado_por": QLineEdit("admin")
        }

        for campo, input_widget in self.campos.items():
            layout.addWidget(QLabel(campo.capitalize()))
            layout.addWidget(input_widget)

        self.btn_cadastrar = QPushButton("Cadastrar novo cliente")
        self.btn_cadastrar.clicked.connect(self.cadastrar_cliente)

        layout.addWidget(self.btn_cadastrar)
        self.setLayout(layout)

    def cadastrar_cliente(self):
        dados = {campo: widget.text() for campo, widget in self.campos.items()}

        try:
            conn = sqlite3.connect("usuarios.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO usuarios 
                (nome, usuario, senha, email, data_criacao, expiracao, status, telas, criado_por) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, tuple(dados.values()))
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Sucesso", "Cliente cadastrado com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar: {e}")
