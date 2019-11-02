# -*- coding: utf-8 -*-
''''
Este codigo e' uma evolucao do anterior agora pegando todos os comentarios das paginas, sem as respostas dos comentarios
'''

import simplejson as json
import urllib
import math

#arquivo onde o resultado sera armazenado
arquivoResultado = open('resultado-v2.txt','w')

url = "http://api.nytimes.com/svc/community/v3/user-content/url.json?api-key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&url=http://www.nytimes.com/2015/10/11/fashion/the-original-conscious-uncouplers.html"

#le a pagina. O retorno e' um json
conteudoJSON = urllib.urlopen(url).read()

#Cria o parser do json retornado
parser = json.loads(conteudoJSON.strip())

#numero total de comentarios (sem incluir as respostas)
totalComentarios = parser['results']['totalParentCommentsFound']

#O NYT retorna no maximo 25 comentarios por resposta. Esse calculo serve para saber quantas requisicoes serao necessarias. 
numRequisicoes = int(math.ceil(totalComentarios/25.0)) 



#Agora que ja sabemos o numero de requisicoes que devemos fazer, criamos um laco de acordo com esse numero
for req in range(0,numRequisicoes):
    
    url = "http://api.nytimes.com/svc/community/v3/user-content/url.json?api-key=31df9489228447933edb81c5e170296e:12:72976163&url=http://www.nytimes.com/2015/10/11/fashion/the-original-conscious-uncouplers.html&offset="+str(req*25)
    
    conteudoJSON = urllib.urlopen(url).read()
    parser = json.loads(conteudoJSON.strip())
    
    #numero total de comentarios retornados 
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
      
      