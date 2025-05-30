# raspar_dados_widget.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import QThread, pyqtSignal

class RaspagemThread(QThread):
    sucesso = pyqtSignal()
    erro = pyqtSignal(str)

    def run(self):
        try:
            from scraping_e_insercao import raspar_e_inserir
            raspar_e_inserir()
            self.sucesso.emit()
        except Exception as e:
            self.erro.emit(str(e))

class RasparDadosWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Raspar Dados")

        layout = QVBoxLayout()

        self.label = QLabel("Clique para raspar os dados do painel aberto e salvar no banco de dados.")
        layout.addWidget(self.label)

        self.btn_raspar = QPushButton("📥 Iniciar raspagem")
        self.btn_raspar.clicked.connect(self.executar_raspar_dados)
        layout.addWidget(self.btn_raspar)

        self.setLayout(layout)

    def executar_raspar_dados(self):
        self.thread = RaspagemThread()
        self.thread.sucesso.connect(lambda: QMessageBox.information(self, "Sucesso", "📥 Dados raspados e inseridos com sucesso!"))
        self.thread.erro.connect(lambda msg: QMessageBox.critical(self, "Erro", f"Erro durante a raspagem: {msg}"))
        self.thread.start()
