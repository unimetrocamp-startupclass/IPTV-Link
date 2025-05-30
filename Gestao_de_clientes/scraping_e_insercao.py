from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import sqlite3

def raspar_e_inserir():
    # Conecta ao Chrome já aberto com login
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)

    driver.get("https://cms.xcsdx.online/gerenciador/usuario-iptv")
    time.sleep(3)

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

    # Salva como JSON para registro
    with open("usuarios_extraidos.json", "w", encoding="utf-8") as f:
        json.dump(usuarios, f, ensure_ascii=False, indent=4)

    # Conecta ao banco SQLite
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # Cria a tabela com chave primária
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        nome TEXT,
        usuario TEXT PRIMARY KEY,
        senha TEXT,
        email TEXT,
        data_criacao TEXT,
        expiracao TEXT,
        status TEXT,
        telas TEXT,
        criado_por TEXT
    )
    """)

    # Inserção ou atualização
    for u in usuarios:
        cursor.execute("""
            INSERT INTO usuarios (
                nome, usuario, senha, email,
                data_criacao, expiracao, status,
                telas, criado_por
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(usuario) DO UPDATE SET
                nome=excluded.nome,
                senha=excluded.senha,
                email=excluded.email,
                data_criacao=excluded.data_criacao,
                expiracao=excluded.expiracao,
                status=excluded.status,
                telas=excluded.telas,
                criado_por=excluded.criado_por
        """, (
            u['nome'], u['usuario'], u['senha'], u['email'],
            u['data_criacao'], u['expiracao'], u['status'],
            u['telas'], u['criado_por']
        ))

    conn.commit()
    conn.close()
    print(f"[✓] {len(usuarios)} usuários inseridos/atualizados no banco com sucesso!")

if __name__ == "__main__":
    raspar_e_inserir()
