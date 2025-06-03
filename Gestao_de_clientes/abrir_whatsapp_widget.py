# abrir_whatsapp_widget.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
import subprocess

class AbrirWhatsAppWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Clique abaixo para abrir o WhatsApp Web no navegador com depuração remota.")
        layout.addWidget(self.label)

        self.btn_abrir = QPushButton("💬 Abrir WhatsApp Web")
        self.btn_abrir.clicked.connect(self.abrir_whatsapp)
        layout.addWidget(self.btn_abrir)

        self.setLayout(layout)

    def abrir_whatsapp(self):
        try:
            comando = (
                r'"C:\Program Files\Google\Chrome\Application\chrome.exe" '
                '--remote-debugging-port=9222 '
                '--user-data-dir="C:\\chrome_wpp" '
                'https://web.whatsapp.com/'
            )
            subprocess.Popen(comando, shell=True)
            QMessageBox.information(self, "Sucesso", "💬 WhatsApp Web aberto! Faça login, se necessário.")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao abrir o WhatsApp: {e}")
