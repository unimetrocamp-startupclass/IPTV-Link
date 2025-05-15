from PyQt6.QtWidgets import QApplication
import sys
from cadastro_widget import CadastroWindow

app = QApplication(sys.argv)
janela = CadastroWindow()
janela.show()
sys.exit(app.exec())
