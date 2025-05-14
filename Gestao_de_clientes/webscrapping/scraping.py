import requests
from bs4 import BeautifulSoup
import sqlite3

# Configurações
url_login = 'https://cms.xcsdx.online/'  # URL de login
url_data = 'https://cms.xcsdx.online/gerenciador/usuario-iptv'  # URL para scraping
username = 'vinirabelo'
password = '25071123'

# Iniciar uma sessão
session = requests.Session()

# Realizar o login
login_payload = {
    'username': username,
    'password': password
}

# Enviar a requisição de login
session.post(url_login, data=login_payload)

# Acessar a página de dados
response = session.get(url_data)

# Analisar o conteúdo da página
soup = BeautifulSoup(response.text, 'html.parser')

# Extrair dados (exemplo: nomes de usuários)
usuarios = []
for row in soup.select('table tbody tr'):
    cols = row.find_all('td')
    if cols:
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

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()

# Criar tabela se não existir
c.execute('''
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
''')

# Inserir dados no banco de dados
for usuario in usuarios:
    c.execute('''
        INSERT INTO usuarios (nome, usuario, senha, email, data_criacao, expiracao, status, telas, criado_por)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (usuario['nome'], usuario['usuario'], usuario['senha'], usuario['email'], usuario['data_criacao'], usuario['expiracao'], usuario['status'], usuario['telas'], usuario['criado_por']))

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Dados extraídos e armazenados com sucesso!")