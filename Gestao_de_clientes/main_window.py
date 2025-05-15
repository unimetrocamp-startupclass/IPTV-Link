from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt
from cadastro_widget import CadastroWidget  # Agora é um widget, não uma janela
from clientes_widget import ClientesWidget


class MainWindow(QWidget):
    def __init__(self, usuario_nome="Usuário"):
        super().__init__()

        self.setWindowTitle("Gestor de Clientes")
        self.setGeometry(100, 100, 1000, 600)

        # Layout principal
        main_layout = QHBoxLayout()

        # 📌 MENU
        menu_frame = QFrame(self)
        menu_frame.setFixedWidth(200)
        menu_frame.setStyleSheet("background-color: #333; color: white;")
        menu_layout = QVBoxLayout()

        self.label_usuario = QLabel(f"Olá, {usuario_nome}!")
        self.label_usuario.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.label_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_cadastros = QPushButton("📋 Cadastrar")
        btn_clientes = QPushButton("👥 Clientes")
        btn_config = QPushButton("⚙️ Configurações")
        btn_logout = QPushButton("🚪 Sair")
        btn_logout.clicked.connect(self.sair)

        btn_cadastros.clicked.connect(self.abrir_cadastro)
        btn_clientes.clicked.connect(self.abrir_clientes)


        menu_layout.addWidget(self.label_usuario)
        menu_layout.addWidget(btn_cadastros)
        menu_layout.addWidget(btn_clientes)
        menu_layout.addWidget(btn_config)
        menu_layout.addStretch()
        menu_layout.addWidget(btn_logout)

        menu_frame.setLayout(menu_layout)

        # 📌 CONTEÚDO DINÂMICO
        self.content_frame = QFrame(self)
        self.content_frame.setStyleSheet("background-color: #f4f4f4;")
        self.content_layout = QVBoxLayout()
        self.label_conteudo = QLabel("Selecione uma opção no menu")
        self.label_conteudo.setStyleSheet("font-size: 18px;")
        self.label_conteudo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.content_layout.addWidget(self.label_conteudo)
        self.content_frame.setLayout(self.content_layout)

        # Adiciona ao layout principal
        main_layout.addWidget(menu_frame)
        main_layout.addWidget(self.content_frame)

        self.setLayout(main_layout)

    def sair(self):
        self.close()

    def abrir_cadastro(self):
        # Limpa o conteúdo atual
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Adiciona o novo widget de cadastro
        self.content_layout.addWidget(CadastroWidget())

    def abrir_clientes(self):
    # Limpa o conteúdo atual
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        # Adiciona a tabela de clientes
        self.content_layout.addWidget(ClientesWidget())

