from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

def Clica(nome, ano, mes):
    link_site = 'https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx' #Link do site de acesso

    options = Options()
    options.add_argument('--headless') #Opção pra deixar o browser oculto em quanto o código roda

    navegador = webdriver.Chrome(options=options) #CASO HAJA PROBLEMA NO CÓDIGO, RETIRE AS OPTIONS
    navegador.get(link_site) #Utilizado para abrir o browser no respectivo site

    idMes = 'cphBody_lkMes'+mes #ID do botão de cada respectivo mês indicado 
    idAno = 'cphBody_lkAno'+ano #ID do botão de cada respectivo ano indicado
    idSite = 'cphBody_btn'+nome #ID do botão de cada respectivo tema indicado   

    click1 = navegador.find_element('id', idSite)
    click1.click() #Click no botão do tema

    click2 = navegador.find_element('id', idAno)
    click2.click()#Click no botão do ano

    click3 = navegador.find_element('id', idMes)
    click3.click()#Click no botão do mês

    clickDownload = navegador.find_element('id', 'cphBody_ExportarBOLink')
    clickDownload.click()#Click no botão de Download

    sleep(8)#time para aguardar tudo acontecer, sem quebrar a execução no meio
     


#GUIA DOS NOMES DOS TEMAS, ANO, MES
    #OS ANOS PRECISAM SER INDICADO APENAS COM OS DOIS ULTIMOS DIGITOS EX:22, 23 
    #OS MESES REPRENTADO POR SEUS RESPECTIVOS NÚMEROS EX: JANEIRO = 1, MAIO = 5 ETC
    #OS NOMES TEM QUE SER INDICADO DA SEGUINTE FORMA:
        #TAXA DE HOMICÍDIO = TaxaHomicidio
        #HOMICÍDIO DOLOSO = Homicidio
        #FEMINICÍDIO = Feminicidio
        #LATROCÍNIO = Latrocinio
        #LESÃO CORPORAL SEGUIDA DE MORTE = LesaoMorte
        #REGISTRO DE ÓBITOS - IML = IML2022
        #MORTE DECORRENTE DE INTERVENÇÃO POLICIAL = MortePolicial2022
        #MORTE SUSPEITA = MorteSuspeita
        #FURTO DE VEÍCULO = FurtoVeiculo
        #ROUBO DE VEÍCULO = RouboVeiculo
        #FURTO DE CELULAR = FurtoCelular
        #ROUBO DE CELULAR = RouboCelular
        #SP DADOS CRIMINAIS = DadosCriminais2022
