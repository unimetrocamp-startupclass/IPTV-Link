from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QFrame
)
from PyQt6.QtCore import Qt

from main_config import ConfigWindow
from cadastro_widget import CadastroWidget
from clientes_widget import ClientesWidget
from abrir_painel_widget import AbrirPainelWidget
from raspar_dados_widget import RasparDadosWidget
from enviar_mensagem_widget import EnviarMensagemWidget  # Novo widget

class MainWindow(QWidget):
    def __init__(self, usuario_nome="Usuário"):
        super().__init__()

        self.setWindowTitle("UP - Gestor de Clientes")
        self.setGeometry(100, 100, 1000, 600)
        self.showMaximized()

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
        btn_abrir_painel = QPushButton("🌐 Abrir Painel")
        btn_raspar_dados = QPushButton("📥 Raspar Dados")
        btn_mensagem = QPushButton("💬 Enviar Mensagem")  # Botão novo
        btn_logout = QPushButton("🚪 Sair")

        # Conectando botões às funções
        btn_cadastros.clicked.connect(self.abrir_cadastro)
        btn_clientes.clicked.connect(self.abrir_clientes)
        btn_config.clicked.connect(self.abrir_configuracoes)
        btn_abrir_painel.clicked.connect(self.abrir_painel)
        btn_raspar_dados.clicked.connect(self.executar_raspar_dados)
        btn_mensagem.clicked.connect(self.abrir_mensagem_widget)  # Novo método
        btn_logout.clicked.connect(self.sair)


        botao_estilo = """
            QPushButton {
                background-color: transparent;
                color: white;
                font-size: 14px;
                padding: 10px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #444;
            }
        """

        for botao in [btn_cadastros, btn_clientes, btn_config, btn_abrir_painel, btn_raspar_dados, btn_logout]:
            botao.setStyleSheet(botao_estilo)



        # Adiciona os botões ao menu
        menu_layout.addWidget(self.label_usuario)
        menu_layout.addWidget(btn_cadastros)
        menu_layout.addWidget(btn_clientes)
        menu_layout.addWidget(btn_config)
        menu_layout.addWidget(btn_abrir_painel)
        menu_layout.addWidget(btn_raspar_dados)
        menu_layout.addWidget(btn_mensagem)
        menu_layout.addStretch()
        menu_layout.addWidget(btn_logout)

        menu_frame.setLayout(menu_layout)

        # 📦 ÁREA DE CONTEÚDO PRINCIPAL
        self.content_frame = QFrame(self)
        self.content_frame.setStyleSheet("background-color: #f4f4f4;")
        self.content_layout = QVBoxLayout()
        self.label_conteudo = QLabel("Selecione uma opção no menu")
        self.label_conteudo.setStyleSheet("font-size: 18px;")
        self.label_conteudo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.content_layout.addWidget(self.label_conteudo)
        self.content_frame.setLayout(self.content_layout)

        # Layout principal
        main_layout.addWidget(menu_frame)
        main_layout.addWidget(self.content_frame)
        self.setLayout(main_layout)

    def limpar_conteudo(self):
        for i in reversed(range(self.content_layout.count())):
            widget = self.content_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def sair(self):
        self.close()

    def abrir_cadastro(self):
        self.limpar_conteudo()
        self.content_layout.addWidget(CadastroWidget())

    def abrir_clientes(self):
        self.limpar_conteudo()
        self.content_layout.addWidget(ClientesWidget())

    def abrir_configuracoes(self):
        self.limpar_conteudo()
        self.content_layout.addWidget(ConfigWindow())

    def abrir_painel(self):
        self.limpar_conteudo()
        self.content_layout.addWidget(AbrirPainelWidget())

    def executar_raspar_dados(self):
        self.limpar_conteudo()
        self.content_layout.addWidget(RasparDadosWidget())

    def abrir_mensagem_widget(self):  # Novo método
        self.limpar_conteudo()
        self.content_layout.addWidget(EnviarMensagemWidget())
