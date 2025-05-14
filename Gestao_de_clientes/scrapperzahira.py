import pandas as pd
from urllib.parse import quote

def extrair_tabelas_wikipedia(titulo_artigo):
    # Codifica o título para formato URL-safe
    titulo_formatado = quote(titulo_artigo.replace(" ", "_"))
    url = f"https://pt.wikipedia.org/wiki/{titulo_formatado}"

    # Lê as tabelas da página
    tabelas = pd.read_html(url)

    # Mostra quantas tabelas foram encontradas
    print(f'{len(tabelas)} tabela(s) encontrada(s) na página "{titulo_artigo}":\n')

    # Exibe as 3 primeiras linhas de cada tabela
    for i, tabela in enumerate(tabelas):
        print(f'Tabela {i+1}:\n')
        print(tabela.head())
        print("\n" + "-"*50 + "\n")

# Teste
extrair_tabelas_wikipedia("Lista de estados do Brasil por população")
