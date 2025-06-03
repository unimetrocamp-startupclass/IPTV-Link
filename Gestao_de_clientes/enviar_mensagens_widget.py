from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QTextEdit
from PyQt6.QtCore import QTimer
import threading
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class EnviarMensagensWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.label = QLabel("Digite a mensagem que será enviada automaticamente pelo WhatsApp Web:")
        layout.addWidget(self.label)

        self.texto_mensagem = QTextEdit()
        self.texto_mensagem.setPlaceholderText("Ex: Olá! Esta é uma mensagem automática enviada pelo sistema 😊")
        layout.addWidget(self.texto_mensagem)

        self.btn_enviar = QPushButton("📨 Enviar Mensagens")
        self.btn_enviar.clicked.connect(self.executar_script_em_thread)
        layout.addWidget(self.btn_enviar)

        self.setLayout(layout)

    def executar_script_em_thread(self):
        mensagem = self.texto_mensagem.toPlainText().strip()
        if not mensagem:
            QMessageBox.warning(self, "Aviso", "Por favor, digite a mensagem antes de enviar.")
            return

        thread = threading.Thread(target=self.enviar_mensagens, args=(mensagem,))
        thread.start()

    def enviar_mensagens(self, mensagem):
        try:
            # Conecta ao navegador já aberto com depuração remota
            options = Options()
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver = webdriver.Chrome(options=options)

            # Conecta ao banco de dados
            con = sqlite3.connect('usuarios.db')
            cur = con.cursor()
            cur.execute("SELECT nome FROM usuarios WHERE nome IS NOT NULL")
            usuarios = cur.fetchall()

            for (telefone,) in usuarios:
                numero = f'+55{telefone}'
                try:
                    driver.get(f'https://web.whatsapp.com/send?phone={numero}&text={mensagem}')
                    time.sleep(6)

                    caixa = driver.find_element(By.XPATH, '//div[@data-tab="10"][@contenteditable="true"]')
                    caixa.send_keys(Keys.ENTER)

                    print(f"[✓] Mensagem enviada para {telefone}")
                    time.sleep(3)
                except Exception as e:
                    print(f"[X] Erro com {telefone}: {e}")

            driver.quit()

            QTimer.singleShot(0, lambda: QMessageBox.information(
                self, "Sucesso", "Mensagens enviadas com sucesso!"))

        except Exception as e:
            QTimer.singleShot(0, lambda: QMessageBox.critical(
                self, "Erro", f"Erro ao enviar mensagens: {e}"))
