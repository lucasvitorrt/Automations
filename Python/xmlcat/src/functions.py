from numpy import imag
import pyautogui as pa
import os
import time as t
import datetime as dt

local = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' #Local do navegador(baseado no edge)
ende = r'http://nfe.sefaz.go.gov.br/nfeweb/sites/nfe/consulta-publica/principal' #site de dowload dos xmls

daysago = 1 #quantidade de dias atrás para pesquisa
today = dt.date.today().strftime('%d/%m/%Y')
day = (dt.date.today() - dt.timedelta(days=daysago)).strftime('%d/%m/%Y')

def opensite(site, path): #função para abrir o site de download.
    os.startfile(path)
    t.sleep(1)
    pa.click(872, 42, duration=0.3) #clique na barra de endereços
    pa.write(site) #insere o site 
    t.sleep(1)
    pa.press('ENTER')
    t.sleep(1)
    clickonimg('acessocert.png')
    t.sleep(1)

def clickonimg(img : str): #função para clicar em uma imagem.png que esteja na tela
    local = pa.locateOnScreen('Automations\\python\\xmlcat\\imgs\\' + img)
    x, y = pa.center(local)
    pa.click(x, y, duration=0.1)

def locationimg(img : str): #função que retorna 1 casa haja uma imagem na tela, 0 caso não.
    try:
        pa.locateOnScreen('Automations\\python\\xmlcat\\imgs\\' + img)
    except:
        return 0
    return 1

def verifycertificate(certificate : str): #função que verifica se há um certificado instalado.
    while True:
        ex = 0
        try:
            clickonimg(certificate)
        except:
            ex = 1
        if ex:
            if locationimg('finalcerts.png'):
                print('Certificado não encontrado!!')
                break
            else:
                try:
                    clickonimg('movdow.png')
                except:
                    pa.click()
                ex = 0
        else:
            t.sleep(0.2)
            pa.press('ENTER')
            break
            

def searchdownload(): #função de busca dos xml e downloads
    clickonimg('pesquisar.png')
    t.sleep(3)
    pa.click()
    t.sleep(3)
    clickonimg('baixar2.png')
    t.sleep(3)
    #clickonimg('ok.png')

def insertdate(): #função para inserção de data no seu respectivo campo.
    pa.click(256, 256, duration=0.3)
    pa.write(day)
    t.sleep(0.7)
    pa.press('TAB')
    pa.write(today)
    t.sleep(0.7)

def downloadxmlmundnat(): #função para dowload dos xmls de catalão.
    opensite(ende, local)
    verifycertificate('mundonat.png')
    t.sleep(0.5)
    pa.click(545, 209, duration=0.3)
    t.sleep(1)
    clickonimg('mundonatcnpj.png')
    t.sleep(1)
    insertdate()
    searchdownload()
    t.sleep(1)
    pa.click(1341, 14, duration=0.3)

def downloadxmlflavia():
    opensite(ende, local)
    verifycertificate('flavia.png')
    t.sleep(1)
    insertdate()
    searchdownload()
    t.sleep(1)
    clickonimg('novaconsulta.png')
    t.sleep(4)
    pa.click(545, 209, duration=0.3)
    t.sleep(1)
    clickonimg('flaviacnpj.png')
    t.sleep(1)
    insertdate()
    searchdownload()
    t.sleep(1)
    pa.click(1341, 14, duration=0.3)





