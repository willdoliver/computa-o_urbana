import requests
from bs4 import BeautifulSoup

url = 'https://www.bringit.com.br/fonte-bringit-notebook-bringit-seletor-de-voltagem.html'

# Requisicao da pagina
req = requests.get(url)

# Todo o conteudo da pagina
soup = BeautifulSoup(req.content, 'html.parser')

nomeBruto = soup.find("div", {"class":"product-name"})
price = soup.find("span", {"class":"price"})

print(nomeBruto.text.strip())
print(price.text.strip())
