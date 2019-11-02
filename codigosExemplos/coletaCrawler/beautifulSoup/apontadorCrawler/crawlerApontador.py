import requests
from bs4 import BeautifulSoup


#url da busca por bares em BH. Ja com o atributo page
url = "http://www.apontador.com.br/local/search.html?q=bares&loc=Belo%20Horizonte%2C%20MG&page=1"

#retorna o conteudo da pagina
req = requests.get(url)

#transforma o conteudo da pagina em um objeto BeautifulSoup
conteudoGeral = BeautifulSoup(req.content,'html.parser')


#identifica todos os estabelecimentos. Eles estao disponibilizados com a tag article e possuem um atributo 'class' do tipo 'poi card'
estabelecimentosInfos = conteudoGeral.find_all("article", {"class":"poi card"})

#percorre cada estabelecimento da lista retornada
for estab in estabelecimentosInfos:
  print(estab.get('data-place-lat'))
  print(estab.get('data-place-long'))
  
  #tratamento de excesao. Caso algum estabelecimento nao possua a classe "poi address" ignora o estabelecimento
  try:
    #identifica o endereco do estabelecimento
    adressBruto = estab.find_all("p", {"class":"poi address"})
    print(adressBruto[0].text)
  except:
    continue
  
  #identifica o nome do estabelecimento
  estab.find_all("h3", {"class":"poi name"})
  