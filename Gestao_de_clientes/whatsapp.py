from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sqlite3
import time

# Conecta ao navegador já aberto
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=options)

# Conecta ao banco
con = sqlite3.connect('usuarios.db')
cur = con.cursor()
cur.execute("SELECT nome FROM usuarios WHERE nome IS NOT NULL")
usuarios = cur.fetchall()

# Envia mensagem
for (telefone,) in usuarios:
    numero = f'+55{telefone}'
    mensagem = 'Olá! Esta é uma mensagem automática enviada pelo sistema 😊'
    
    try:
        driver.get(f'https://web.whatsapp.com/send?phone={numero}&text={mensagem}')
        time.sleep(6)  # aguarda carregar a conversa

        # Envia com Enter
        caixa = driver.find_element(By.XPATH, '//div[@data-tab="10"][@contenteditable="true"]')
        caixa.send_keys(Keys.ENTER)

        print(f"[✓] Mensagem enviada para {telefone}")
        time.sleep(3)
    except Exception as e:
        print(f"[X] Erro com {telefone}: {e}")

driver.quit()
