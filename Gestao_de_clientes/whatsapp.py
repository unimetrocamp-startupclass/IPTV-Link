from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sqlite3
import time

# Conectar ao banco de dados
con = sqlite3.connect('usuarios.db')
cur = con.cursor()

# Buscar telefones (na coluna "nome")
cur.execute("SELECT nome FROM usuarios WHERE nome IS NOT NULL")
usuarios = cur.fetchall()

# Iniciar o navegador
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# Esperar login manual
input("Escaneie o QR Code no navegador e aperte Enter aqui quando estiver logado...")

# Enviar mensagem para cada número
for (telefone,) in usuarios:
    numero = f'+55{telefone}'  # garante que o número esteja no formato internacional
    mensagem = 'Olá! Esta é uma mensagem automática enviada pelo sistema 😊'
    
    try:
        driver.get(f'https://web.whatsapp.com/send?phone={numero}&text={mensagem}')
        time.sleep(5)  # tempo para carregar a conversa
        
        caixa_mensagem = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        caixa_mensagem.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para {telefone}")
        time.sleep(5)
    except Exception as e:
        print(f"Erro ao enviar para {telefone}: {e}")

driver.quit()
