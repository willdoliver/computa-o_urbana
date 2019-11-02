

import requests
from bs4 import BeautifulSoup


##pagina do produto
url = "https://www.bringit.com.br/fonte-bringit-notebook-bringit-seletor-de-voltagem.html"

##retorna o conteudo da pagina
req = requests.get(url)

##transforma o conteudo da pagina em um objeto BeautifulSoup
soup = BeautifulSoup(req.content,'html.parser')

nomeBruto = soup.find("div",{"class":"product-name"})


print nomeBruto.text





