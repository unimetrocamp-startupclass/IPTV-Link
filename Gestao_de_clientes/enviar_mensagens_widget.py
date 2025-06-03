# enviar_mensagens_widget.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PyQt6.QtCore import QTimer
import subprocess
import threading
import os

class EnviarMensagensWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Clique abaixo para enviar mensagens automáticas pelo WhatsApp Web.")
        layout.addWidget(self.label)

        self.btn_enviar = QPushButton("📨 Enviar Mensagens")
        self.btn_enviar.clicked.connect(self.executar_script_em_thread)
        layout.addWidget(self.btn_enviar)

        self.setLayout(layout)

    def executar_script_em_thread(self):
        thread = threading.Thread(target=self.executar_script)
        thread.start()

    def executar_script(self):
        try:
            caminho_script = os.path.abspath("enviar_mensagens.py")
            subprocess.run([
                "python", 
                "C:\\Users\\pedro\\Downloads\\Nova pasta (4)\\Up_Gestor_de_clientes-main\\Gestao_de_clientes\\enviar_mensagens.py"
            ], check=True)

            QTimer.singleShot(0, lambda: QMessageBox.information(
                self, "Sucesso", "Mensagens enviadas com sucesso!"))

        except subprocess.CalledProcessError as e:
            QTimer.singleShot(0, lambda: QMessageBox.critical(
                self, "Erro", f"Ocorreu um erro ao enviar mensagens:\n{e}"))
