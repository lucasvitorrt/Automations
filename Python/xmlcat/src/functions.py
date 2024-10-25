from numpy import imag
import pyautogui as pa
import os
import time as t
import datetime as dt

path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
site = r'http://nfe.sefaz.go.gov.br/nfeweb/sites/nfe/consulta-publica/principal'

daysago = 1
today = dt.date.today().strftime('%d/%m/%Y')
day = (dt.date.today() - dt.timedelta(days=daysago)).strftime('%d/%m/%Y')

def clickonimg(img : str):
    local = pa.locateOnScreen('Automations\\python\\xmlcat\\imgs\\' + img)
    x, y = pa.center(local)
    pa.click(x, y, duration=0.2)

def locationimg(img : str):
    try:
        pa.locateOnScreen('Automations\\python\\xmlcat\\imgs\\' + img)
    except:
        return 0
    return 1

def verifycertificate(certificate : str):
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
            

def searchdownload():
    clickonimg('pesquisar.png')
    t.sleep(3)
    pa.click()
    t.sleep(3)
    clickonimg('baixar2.png')
    t.sleep(3)
    #clickonimg('ok.png')

def insertdate():
    pa.click(256, 256, duration=0.3)
    pa.write(day)
    t.sleep(0.7)
    pa.press('TAB')
    pa.write(today)
    t.sleep(0.7)

def downloadxmlmundnat():
    os.startfile(path)
    t.sleep(1)
    pa.click(872, 42, duration=0.3)
    pa.write(site)
    t.sleep(1)
    pa.press('ENTER')
    t.sleep(1)
    clickonimg('acessocert.png')
    t.sleep(1)
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
    os.startfile(path)
    t.sleep(1)
    pa.click(872, 42, duration=0.3)
    pa.write(site)
    t.sleep(1)
    pa.press('ENTER')
    t.sleep(1)
    clickonimg('acessocert.png')
    t.sleep(1)
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





