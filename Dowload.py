from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


#options = Options()
#options.add_argument('--headless')

def Clica(link, nome):
    link_site = link

    navegador = webdriver.Chrome()
    navegador.get(link_site)

    idSite = 'cphBody_btn'+nome    
    print(idSite)

    click1 = navegador.find_element('id', idSite)
    click1.click()



Clica('https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx', 'FurtoVeiculo')
