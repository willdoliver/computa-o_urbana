from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

#options = webdriver.ChromeOptions()
#options.binary_location = "/home/thiago/Dropbox/utfpr/disciplinas/computacaoSocialUrbana/aulas/2-coleta/codigos1/coletaCrawler/selenium/chromedriver"
driver = webdriver.Chrome()


driver.get("https://www.w3schools.com/xml/ajax_intro.asp")  

#Clica no botao da pagina para ver o conteudo     
botaolist = driver.find_elements_by_xpath('//*[@id="demo"]/button')
botaolist[0].click()

wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="demo"]/h1')))

# get the page source
page_source = driver.page_source    

#fecha o driver, mas quando estivermos coletando varias paginas podemos manter ativo pra nao precisar abrir o browser novamente
#driver.close()
    
soup = BeautifulSoup(page_source, "lxml") #grab the content with beautifulsoup for parsing
    
content= soup.find("div",{"id":"demo"}) 
print content

