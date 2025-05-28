from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

# Configura o Selenium para se conectar ao Chrome já aberto
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Inicializa o WebDriver (usa o Chrome já aberto!)
driver = webdriver.Chrome(options=options)

# Acesse a URL desejada (já logado)
driver.get("https://cms.xcsdx.online/gerenciador/usuario-iptv")  # ou a página onde a tabela está

time.sleep(3)  # Espera a tabela carregar

# Encontra todas as linhas da tabela
rows = driver.find_elements("css selector", "table tbody tr")

usuarios = []
for row in rows:
    cols = row.find_elements("tag name", "td")
    if len(cols) >= 10:
        usuario = {
            'nome': cols[1].text.strip(),
            'usuario': cols[2].text.strip(),
            'senha': cols[3].text.strip(),
            'email': cols[4].text.strip(),
            'data_criacao': cols[5].text.strip(),
            'expiracao': cols[6].text.strip(),
            'status': cols[7].text.strip(),
            'telas': cols[8].text.strip(),
            'criado_por': cols[9].text.strip()
        }
        usuarios.append(usuario)

# Salva os dados em um arquivo JSON
with open("usuarios_extraidos.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, ensure_ascii=False, indent=4)

print(f"[✓] {len(usuarios)} usuários extraídos com sucesso!")
