import json
from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton,
    QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt


class ConfigWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configurações")
        self.setStyleSheet("background-color: #f0f0f0;")
        self.setFixedSize(500, 300)

        main_layout = QHBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card = QFrame()
        card.setFixedSize(350, 220)
        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(10, 10, 10, 10)

        # Aqui colocamos fundo amarelo TEMPORÁRIO no QLabel para ver se aparece
        self.label = QLabel("Alteraração de Senha")
        self.label.setStyleSheet("""
            font-size: 16px;
            color: black;
            padding: 5px;
        """)

        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha.setPlaceholderText("Digite a nova senha")
        self.input_senha.setStyleSheet("""
            QLineEdit {
                padding: 3px;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 14px;
            }
        """)

        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.clicked.connect(self.salvar_senha)
        self.btn_salvar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 3px;
                border: none;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.mensagem = QLabel("")
        self.mensagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mensagem.setStyleSheet("font-size: 2px; font-weight: bold;")

        layout.addWidget(self.label)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.btn_salvar)
        layout.addWidget(self.mensagem)

        card.setLayout(layout)
        main_layout.addWidget(card)
        self.setLayout(main_layout)

    def salvar_senha(self):
        nova_senha = self.input_senha.text().strip()
        if not nova_senha:
            self.mensagem.setText("A senha não pode estar vazia.")
            self.mensagem.setStyleSheet("color: red; font-weight: bold;")
            return

        try:
            with open("config.json", "r") as f:
                dados = json.load(f)
        except FileNotFoundError:
            dados = {}

        dados["senha"] = nova_senha

        with open("config.json", "w") as f:
            json.dump(dados, f)

        self.mensagem.setText("Senha atualizada com sucesso!")
        self.mensagem.setStyleSheet("color: green; font-size: 4px;")
