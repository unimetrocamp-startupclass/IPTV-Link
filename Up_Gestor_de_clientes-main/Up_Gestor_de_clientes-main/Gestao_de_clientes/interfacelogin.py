from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

import sys

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Usuário:")
        self.username_input = QLineEdit()
        
        self.label2 = QLabel("Senha:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.verificar_login)

        layout.addWidget(self.label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.label2)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def verificar_login(self):
        usuario = self.username_input.text()
        senha = self.password_input.text()

        # Validação básica (depois podemos conectar ao banco ou arquivo)
        if usuario == "admin" and senha == "1234":
            self.ir_para_tela_principal()
        else:
            self.label.setText("Login inválido!")

    def ir_para_tela_principal(self):
        from main_window import MainWindow  # Importação atrasada para evitar erro circular
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Fecha a tela de login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())