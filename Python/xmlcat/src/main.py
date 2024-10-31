import functions as f
import copia as c
import time as t

if f.downloadxmlmundnat():
    print('XML Mundo Natural baixado com sucesso!')
else:
    print('Erro ao baixar o XML do Mundo Natural')

t.sleep(1)

if f.downloadxmlflavia():
    print('XML Flavia baixado com sucesso!')
else:
    print('Erro ao baixar o XML da Flavia')

t.sleep(1)

c.copyfiles()