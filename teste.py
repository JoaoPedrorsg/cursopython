import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da página
url = 'https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/'

# Fazendo a requisição HTTP
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Usando BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrando todas as tabelas na página
    tables = soup.find_all('table')

    # Verificando se encontrou tabelas
    if tables:
        # Usando Pandas para ler a tabela de interesse
        df = pd.read_html(str(tables[0]))[0]
        print(df)
    else:
        print("Nenhuma tabela encontrada na página.")
else:
    print("Erro ao acessar a página.")
