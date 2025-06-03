import json
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("⬆️ UP Gestores - Login")
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial;
            }
        """)
        self.setup_ui()
        self.showMaximized()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(100, 100, 100, 20)

        # Título
        titulo_label = QLabel("⬆️ UP Gestores")
        titulo_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
        titulo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(titulo_label)

        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        center_layout = QHBoxLayout()
        center_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        login_card = QFrame()
        login_card.setFixedSize(350, 300)
        login_card.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                padding: 25px;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.25);
            }
        """)

        form_layout = QVBoxLayout()

        self.label = QLabel("Usuário:")
        self.label.setStyleSheet("font-size: 14px;")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Usuario")  # <-- Placeholder aqui

        self.label2 = QLabel("Senha:")
        self.label2.setStyleSheet("font-size: 14px;")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Digite sua senha")  # <-- Placeholder aqui

        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.verificar_login)

        self.username_input.setStyleSheet(self.input_style())
        self.password_input.setStyleSheet(self.input_style())
        self.login_button.setStyleSheet(self.button_style())

        form_layout.addWidget(self.label)
        form_layout.addWidget(self.username_input)
        form_layout.addWidget(self.label2)
        form_layout.addWidget(self.password_input)
        form_layout.addStretch()
        form_layout.addWidget(self.login_button)

        login_card.setLayout(form_layout)
        center_layout.addWidget(login_card)
        main_layout.addLayout(center_layout)

        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        version_layout = QHBoxLayout()
        version_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        versao_label = QLabel("v1.0")
        versao_label.setStyleSheet("color: gray; font-size: 12px; padding-right: 10px;")
        version_layout.addWidget(versao_label)
        main_layout.addLayout(version_layout)

        self.setLayout(main_layout)

    def input_style(self):
        return """
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 14px;
            }
        """

    def button_style(self):
        return """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px;
                border: none;
                border-radius: 8px;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """

    def verificar_login(self):
        usuario_nome = self.username_input.text()
        senha_digitada = self.password_input.text()

        try:
            with open("config.json", "r") as f:
                dados = json.load(f)
                senha_salva = dados.get("senha", "1234")
        except (FileNotFoundError, json.JSONDecodeError):
            senha_salva = "1234"

        if senha_digitada == senha_salva:
            self.ir_para_tela_principal(usuario_nome)
        else:
            self.label.setText("Senha incorreta!")
            self.label.setStyleSheet("color: red; font-weight: bold;")

    def ir_para_tela_principal(self, usuario_nome):
        try:
            from main_window import MainWindow
            self.main_window = MainWindow(usuario_nome=usuario_nome)
            self.main_window.show()
            self.close()
        except Exception as e:
            print(f"Erro ao abrir a janela principal: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
