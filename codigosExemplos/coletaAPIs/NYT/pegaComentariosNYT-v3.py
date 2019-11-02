# -*- coding: utf-8 -*-
''''
Pega todos os comentarios incluindo as respostas
'''

import simplejson as json
import urllib
import math
import time

def pegaReplies(arquivoResultado,listReplies):
  
  for reply in listReplies:
    #Detalhes das respostas do comentario	
    replyID = reply['commentID']
    replyConteudo = reply['commentBody'].encode('utf_8')
    replyConteudoNoHTMLTags = replyConteudo.replace('<br/>',' ')
	  
    replyRecomendacoes = reply['recommendations']
    replyNumReplies = reply['replyCount']
    respostaDe = reply['parentID']
    
    listRepliesReplies = reply['replies']
    
    #imprime em arquivo o conteudo recuperado
    arquivoResultado.write(str(replyID)+'\t'+replyConteudoNoHTMLTags+'\t'+str(replyRecomendacoes)+'\t'+str(replyNumReplies)+'\t'+str(respostaDe)+'\n')
    
    #verifica se a lista de resposta nao e' vazia
    if len(listRepliesReplies) !=0:
      #chama a funcao que recupera os comentarios
      pegaReplies(arquivoResultado,listRepliesReplies)

    

      
def main():
  #arquivo onde o resultado sera armazenado
  arquivoResultado = open('resultado-v3.txt','w')

  url = "http://api.nytimes.com/svc/community/v3/user-content/url.json?api-key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&url=http://www.nytimes.com/2015/10/11/fashion/the-original-conscious-uncouplers.html"

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
	
	respostaDe = '-'
	
	#imprime em arquivo o conteudo recuperado
	arquivoResultado.write(str(comentarioID)+'\t'+comentarioConteudoNoHTMLTags+'\t'+str(comentarioRecomendacoes)+'\t'+str(comentarioNumReplies)+'\t'+respostaDe+'\n')
	
	listReplies = comentarioDetalhes['replies']
	
	#verifica se a lista de resposta nao e' vazia (API esta'retornando no maximo 3 comentarios)
	if len(listReplies) !=0:
	   #chama a funcao que recupera os comentarios
	   pegaReplies(arquivoResultado,listReplies)
      
      
      #commando para fazer o programa dormir, no caso por 4 segundos
      #time.sleep( 4 )

      
if __name__ == '__main__':
	main()       