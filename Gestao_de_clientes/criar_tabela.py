import json
import sqlite3

# Caminho do arquivo JSON
with open("usuarios_extraidos.json", "r", encoding="utf-8") as f:
    usuarios = json.load(f)

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Criar a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nome TEXT,
    usuario TEXT,
    senha TEXT,
    email TEXT,
    data_criacao TEXT,
    expiracao TEXT,
    status TEXT,
    telas TEXT,
    criado_por TEXT
)
""")

# Inserir cada usuário no banco
for u in usuarios:
    cursor.execute("""
        INSERT INTO usuarios (
            nome, usuario, senha, email,
            data_criacao, expiracao, status,
            telas, criado_por
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        u['nome'], u['usuario'], u['senha'], u['email'],
        u['data_criacao'], u['expiracao'], u['status'],
        u['telas'], u['criado_por']
    ))

conn.commit()
conn.close()
print("[✓] Dados inseridos no banco com sucesso!")
