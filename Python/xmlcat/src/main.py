import functions as f
import copia as c
import time as t

f.downloadxmlmundnat()
t.sleep(1)
f.downloadxmlflavia()
t.sleep(1)
c.copyfiles()