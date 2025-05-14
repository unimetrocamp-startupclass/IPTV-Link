from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, usuario_nome="Usuário"):
        super().__init__()

        self.setWindowTitle("Gestor de Clientes")
        self.setGeometry(100, 100, 1000, 600)

        # Layout principal (horizontal: menu + conteúdo)
        main_layout = QHBoxLayout()

        # 📌 MENU LATERAL
        menu_frame = QFrame(self)
        menu_frame.setFixedWidth(200)
        menu_frame.setStyleSheet("background-color: #333; color: white;")

        menu_layout = QVBoxLayout()

        self.label_usuario = QLabel(f"Olá, {usuario_nome}!")
        self.label_usuario.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.label_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_cadastros = QPushButton("📋 Cadastros")
        btn_clientes = QPushButton("👥 Clientes")
        btn_config = QPushButton("⚙️ Configurações")
        btn_logout = QPushButton("🚪 Sair")
        btn_logout.clicked.connect(self.sair)

        # Adiciona widgets ao menu
        menu_layout.addWidget(self.label_usuario)
        menu_layout.addWidget(btn_cadastros)
        menu_layout.addWidget(btn_clientes)
        menu_layout.addWidget(btn_config)
        menu_layout.addStretch()  # Empurra os botões para cima
        menu_layout.addWidget(btn_logout)

        menu_frame.setLayout(menu_layout)

        # 📌 ÁREA PRINCIPAL DE CONTEÚDO
        content_frame = QFrame(self)
        content_frame.setStyleSheet("background-color: #f4f4f4;")
        content_layout = QVBoxLayout()

        self.label_conteudo = QLabel("Selecione uma opção no menu")
        self.label_conteudo.setStyleSheet("font-size: 18px;")
        self.label_conteudo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        content_layout.addWidget(self.label_conteudo)
        content_frame.setLayout(content_layout)

        # 📌 Adiciona menu e conteúdo ao layout principal
        main_layout.addWidget(menu_frame)
        main_layout.addWidget(content_frame)

        self.setLayout(main_layout)

    def sair(self):
        self.close()  # Fecha a tela principal
