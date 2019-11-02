# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://www.apontador.com.br/local/search.html?q=bares&loc=Belo%20Horizonte%2C%20MG&page="

saida = open("locais.txt",'w')

for i in range(1,4):
  url = url+str(i)
  
  #retorna o conteudo da pagina
  req = requests.get(url)

  #transforma o conteudo da pagina em um objeto BeautifulSoup
  conteudoGeral = BeautifulSoup(req.content,'html.parser')


  #identifica todos os estabelecimentos. Eles estao disponibilizados com a tag article e possuem um atributo 'class' do tipo 'poi card'
  estabelecimentosInfos = conteudoGeral.find_all("article", {"class":"poi card"})
  
  
  #percorre cada estabelecimento da lista retornada
  for estab in estabelecimentosInfos:
    latitude = estab.get('data-place-lat')
    longitude = estab.get('data-place-long')
    address = ""
    
    #tratamento de excesao. Caso algum estabelecimento nao possua a classe "poi address" ignora o estabelecimento
    try:
      #identifica o endereco do estabelecimento
      addressBruto = estab.find_all("p", {"class":"poi address"})
      address = addressBruto[0].text
      
    except:
      print('Erro :(')
      continue
    
    addressEncode = address.encode('utf-8').replace('\n','')
    
    #identifica o nome do estabelecimento
    nome = estab.find_all("h3", {"class":"poi name"})[0].text
    nomeEncode = nome.encode('utf-8').replace('\n','')
    
    saida.write(nomeEncode+'\t'+str(latitude)+'\t'+str(longitude)+'\t'+addressEncode+'\n')


