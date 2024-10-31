import functions as f
import copia as c
import time as t

if f.downloadxmlmundnat():
    print('Mundo Natural baixado com sucesso!')
else:
    print('Erro ao baixar o download do Mundo Natural')


'''t.sleep(1)
f.downloadxmlflavia()
t.sleep(1)
c.copyfiles()'''