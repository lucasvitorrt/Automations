import pyautogui as pa
import time as t
import os
''' é importante que tenha no disco local C:/bin/ dois arquivos, o da conexão e o txt com a senha "passgriffe"
'''

alerta = r'O Caminho "C:\bin\GRIFFE(198).rdp" Não Encontrado! Caso não exista, crie-o e adicione a conexão, com o mesmo nome, dentro da pasta!'
path = r'C:\bin\GRIFFE(198).rdp'
passgriffe = r'C:\bin\passgriffe.txt'

file = open(passgriffe, "r")
content = file.read()
file.close()

while True:
    try:
        os.startfile(path)
    except:
        pa.alert(text=alerta, title='CAMINHO NÃO ENCONTRADO', button='OK')
        break
    try:    
        t.sleep(4)
        pa.click(518, 359, duration=0.3)
        pa.write(content)
        t.sleep(0.8)
        pa.press('ENTER')
        t.sleep(2)
        pa.click(743, 543, duration=0.3)
        t.sleep(20)
        pa.click(927, 8, duration=0.3)
        #pa.alert(text='Processo concluido com sucesso', title='PROCESSO CONCLUÍDO', button='OK')
        break
    except:
        break
    