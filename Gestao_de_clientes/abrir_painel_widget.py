# abrir_painel_widget.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
import subprocess

class AbrirPainelWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Clique abaixo para abrir o painel no navegador com depuração remota.")
        layout.addWidget(self.label)

        self.btn_abrir = QPushButton("🌐 Abrir Painel no Chrome")
        self.btn_abrir.clicked.connect(self.abrir_painel)
        layout.addWidget(self.btn_abrir)

        self.setLayout(layout)

    def abrir_painel(self):
        try:
            comando = (
                r'"C:\Program Files\Google\Chrome\Application\chrome.exe" '
                '--remote-debugging-port=9222 '
                '--user-data-dir="C:\\selenium-profile" '
                'https://cms.xcsdx.online/'
            )
            subprocess.Popen(comando, shell=True)
            QMessageBox.information(self, "Sucesso", "🌐 Painel aberto! Faça login e depois vá para 'Raspar Dados'.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir o painel: {e}")
