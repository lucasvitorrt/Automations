import pyautogui as pa
import time as t
import datetime as dt
import os
import sys

def resource_path(relative_path):
    #Retorna o caminho absoluto para um recurso, independente se está em execução ou empacotado.
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

local = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' #Local do navegador(baseado no edge)
ende = r'http://nfe.sefaz.go.gov.br/nfeweb/sites/nfe/consulta-publica/principal' #site de dowload dos xmls

today = dt.date.today().strftime('%d/%m/%Y')

def aguardeimg(img : str, time : int): # espera uma imagem(img) na tela por x(time) tentaivas de 1 seg, caso apareça retorna 1.
    t.sleep(1)
    while locationimg(img) != 1:
        t.sleep(1)
        time -= 1
        if time == 0:
            return 0
    else:
        return 1

def opensite(site, path): #função para abrir o site de download.
    os.startfile(path)
    #t.sleep(1)
    if aguardeimg('edgeaberto.png', 10):
        pa.click(872, 42, duration=0.3) #clique na barra de endereços
        pa.write(site) #insere o site 
        t.sleep(1)
        pa.press('ENTER')
        t.sleep(1)
        if aguardeimg('acessocert.png', 10): #espera a imagem por 10s, se achar clica nela!
            clickonimg('acessocert.png')
            t.sleep(1)
            return 1
        else:
            print('Erro ao acessar por certificado digital!')
            return 0
        #return 1
    else:
        print('Navegador não foi aberto corretamente!')
        return 0

#descomentar as funções abaixo para testar o app, a que está descomentada é usada para gerar o exe
'''def clickonimg(img : str): #função para clicar em uma imagem.png que esteja na tela
    local = pa.locateOnScreen(resource_path('Automations\\python\\xmlcat\\imgs\\' + img))
    x, y = pa.center(local)
    pa.click(x, y, duration=0.2)

def clickonimgembaixo(img : str): #função para clicar em uma imagem.png que esteja na tela
    local = pa.locateOnScreen(resource_path('Automations\\python\\xmlcat\\imgs\\' + img))
    x = local.left + local.width // 2  # Coordenada X permanece no centro
    y = local.top + local.height - 1   # Coordenada Y na parte inferior da imagem
    pa.click(x, y, duration=0.2)    
 
def clickonimgemdireta(img : str): #função para clicar em uma imagem.png que esteja na tela
    local = pa.locateOnScreen(resource_path('Automations\\python\\xmlcat\\imgs\\' + img))
    x = local.left + local.width - 5  # Move para o canto direito da imagem
    y = local.top + local.height // 2  # Mantém o Y no meio vertical da imagem
    pa.click(x, y, duration=0.2) 
    
def locationimg(img : str): #função que retorna 1 caso haja uma imagem na tela, 0 caso não.
    try:
        pa.locateOnScreen(resource_path('Automations\\python\\xmlcat\\imgs\\' + img))
    except:
        return 0
    return 1'''
    

def clickonimg(img : str): #função para clicar em uma imagem.png que esteja na tela
    img_path = resource_path(img)
    local = pa.locateOnScreen(resource_path(img_path))
    x, y = pa.center(local)
    pa.click(x, y, duration=0.2)
    
def clickonimgembaixo(img : str): #função para clicar na parte de baixo em uma imagem.png que esteja na tela
    img_path = resource_path(img)
    local = pa.locateOnScreen(resource_path(img_path))
    x = local.left + local.width // 2  # Coordenada X permanece no centro
    y = local.top + local.height - 1   # Coordenada Y na parte inferior da imagem
    pa.click(x, y, duration=0.2)    
 
def clickonimgemdireta(img : str): #função para clicar na parte direira em uma imagem.png que esteja na tela
    img_path = resource_path(img)
    local = pa.locateOnScreen(resource_path(img_path))
    x = local.left + local.width - 5  # Move para o canto direito da imagem
    y = local.top + local.height // 2  # Mantém o Y no meio vertical da imagem
    pa.click(x, y, duration=0.2) 

def locationimg(img : str): #função que retorna 1 caso haja uma imagem na tela, 0 caso não.
    try:
        img_path = resource_path(img)  # Caminho direto da imagem na pasta raiz (src)
        pa.locateOnScreen(img_path)
    except:
        return 0
    return 1

def verifycertificate(certificate : str): #função que verifica se há um certificado instalado.
    if aguardeimg('selecionarumcertificado.png', 10):
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
                t.sleep(0.1)
                pa.press('ENTER')
                break
    else:
        print('Não foi possivel abrir a janela de seleção de certificado!')   
   
def aguarde(): #verifica se a imagem do arguarde ainda está na tela
    time = 0
    t.sleep(1.5)
    while locationimg('aguarde.png'):
        t.sleep(1)
        time += 1
        if time == 20:
            return 0
    else:
        return 1

def aguarda_navegador():
    time = 0
    while locationimg('aguardenavegador2.png') != 1:
        t.sleep(1)
        time += 1
        if time == 20:
            return 0
    else:
        return 1

def searchdownload(): #função de busca dos xml e downloads
    clickonimg('pesquisar.png')
    if aguarde():
        t.sleep(1)
        if aguarda_navegador():
            clickonimg('baixar.png')
            if aguarde():
                if locationimg('semresult.png'):
                    print('Não há xml para essa empresa.')    
                else:
                    clickonimg('baixar2.png')
                    if aguardeimg('concluido.png', 120):
                        return 1
                    else:
                        return 0
            else:
                print('Aguardou tempo demais!')
                return 0    
        else:
            return 0
        
    else:
        print('Aguardou tempo demais!')
        return 0

def insertdate(daysago): #função para inserção de data no seu respectivo campo.
    day = (dt.date.today() - dt.timedelta(days=daysago)).strftime('%d/%m/%Y')
    clickonimgembaixo('periodo.png')
    t.sleep(0.5)
    pa.write(day)
    t.sleep(0.5)
    pa.press('TAB')
    t.sleep(0.5)
    pa.write(today)
    t.sleep(0.5)

def downloadxmlmundnat(daysago): #função para dowload dos xmls de catalão.
    if opensite(ende, local):
        verifycertificate('mundonat.png')
        t.sleep(1)
        if aguarde():
            pa.click(545, 209, duration=0.3)
            t.sleep(1)
            clickonimg('mundonatcnpj.png')
            t.sleep(1)
            insertdate(daysago)
            if searchdownload():
                clickonimgemdireta('fecharjanela.png')
                t.sleep(1)
                if locationimg('continuarbaixando.png'):
                    if aguardeimg('baixado.png', 30):
                        clickonimg('continuarbaixando.png')
                        clickonimgemdireta('fecharjanela.png')
                        return 1
                    else:
                        print('falha no download!!')
                        t.sleep(1)
                        clickonimgemdireta('fecharjanela.png')
                        return 0
                else:
                    return 1
            else:
                print('Problema no Download Mundo Natural!')
                clickonimgemdireta('fecharjanela.png')
                return 0
        else:
            print('Problema no site!')
            return 0
    else:
        return 0

def downloadxmlflavia(daysago): 
    if opensite(ende, local):
        verifycertificate('flavia.png')
        t.sleep(1)
        if aguarde():
            t.sleep(1)
            insertdate(daysago)
            if searchdownload():
                t.sleep(1)
                clickonimg('novaconsulta.png')
                if aguarde():
                    pa.click(545, 209, duration=0.3)
                    t.sleep(1)
                    clickonimg('flaviacnpj.png')
                    t.sleep(1)
                    insertdate(daysago)
                    if searchdownload():
                        clickonimgemdireta('fecharjanela.png')
                        t.sleep(1)
                        if locationimg('continuarbaixando.png'):
                            if aguardeimg('baixado.png', 30):
                                clickonimg('continuarbaixando.png')
                                t.sleep(1.5)
                                clickonimgemdireta('fecharjanela.png')
                                return 1
                            else:
                                print('falha no download!!')
                                t.sleep(1.5)
                                clickonimgemdireta('fecharjanela.png')
                                return 0
                        else:
                            return 1
                    else: 
                        print('Problema no download Flavia!')
                        clickonimgemdireta('fecharjanela.png')
                else:
                    print('Problema na nova consulta da Flavia.')
                    return 0
            else:
                print('Problema no Download!')
                return 0
        else:
            print('Problema no site!')
            return 0
    else:
        return 0