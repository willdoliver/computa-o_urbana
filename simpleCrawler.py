import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


url = 'https://www.bringit.com.br/fonte-bringit-notebook-bringit-seletor-de-voltagem.html'

# Requisicao da pagina
req = requests.get(url)

# Todo o conteudo da pagina
soup = BeautifulSoup(req.content, 'html.parser')

productName = soup.find("div", {"class":"product-name"})
price = soup.find("span", {"class":"price"})

print(productName.text.strip())
print(price.text.strip())

# Using Selenium to get the shipping value
driver = webdriver.Chrome('/home/willdoliver/Downloads/chromedriver')
#driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver,3)

# insert the zip+code in the field
zip_code = driver.find_element_by_id('estimate_postcode')
zip_code.send_keys(83302100)

# Click on the button to calculate shippment
button = driver.find_elements_by_xpath('//*[@id="primary-col-product-page"]/div[3]/div[3]/div/div/button')
button[0].click()

# Wait calc response
time.sleep(3)

# Find the fiels with the values
shipping = driver.find_element_by_id('shipping-estimate-results')
shipping_value = shipping.find_element_by_tag_name('tbody')

soup2 = BeautifulSoup(shipping_value, 'lxml')
price2 = soup2.find("div", {"class":"block-content"})

print(price2)