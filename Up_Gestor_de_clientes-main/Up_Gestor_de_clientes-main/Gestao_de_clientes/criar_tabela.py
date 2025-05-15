import sqlite3

# Conecta (ou cria) o banco de dados
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Cria a tabela 'usuarios' se ela não existir
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

conn.commit()
conn.close()

print("Tabela 'usuarios' criada (ou já existia).")
