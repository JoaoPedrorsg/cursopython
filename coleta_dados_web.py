import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisisao = requests.get(url)
extracao = BeautifulSoup(requisisao.text, 'html.parser')

#print(extracao.text.strip())

# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.name.strip()
#     print('Titulo: ', titulo)
#
# for linha_texto in extracao.find_all('p'):
#     paragrafos = linha_texto.text.strip()
#     print('Paragrafos: ', paragrafro)

contar_titulos = 0
contar_paragrafos = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulos += 1
    elif linha_texto.name == 'p':
        contar_paragrafos += 1

print('Total de Titulos: ', contar_titulos)
print('Total de Paragrafos: ', contar_paragrafos)
