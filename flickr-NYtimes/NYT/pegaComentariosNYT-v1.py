# -*- coding: utf-8 -*-
import simplejson as json
import urllib
import math

#arquivo onde o resultado sera armazenado
arquivoResultado = open('resultado-v1.txt','w')

url = "http://api.nytimes.com/svc/community/v3/user-content/url.json?api-key=xxxxxxxxxxxxxxxxxxxxxxxx&url=http://www.nytimes.com/2015/09/27/fashion/from-divorce-a-fractured-beauty.html"

#le a pagina. O retorno e' um json
conteudoJSON = urllib.urlopen(url).read()

#Cria o parser do json retornado
parser = json.loads(conteudoJSON.strip())

totalCommentsReturned = parser['results']['totalCommentsReturned']


for i in range(0,totalCommentsReturned):
      comentarioDetalhes = parser['results']['comments'][i]
      
      #detalhes do comentario
      comentarioID = comentarioDetalhes['commentID']
      comentarioConteudo = comentarioDetalhes['commentBody'].encode('utf_8')
      comentarioConteudoNoHTMLTags = comentarioConteudo.replace('<br/>',' ')
      
      comentarioRecomendacoes = comentarioDetalhes['recommendations']
      comentarioNumReplies = comentarioDetalhes['replyCount']
      
      arquivoResultado.write(str(comentarioID)+'\t'+comentarioConteudoNoHTMLTags+'\t'+str(comentarioRecomendacoes)+'\t'+str(comentarioNumReplies)+'\n')