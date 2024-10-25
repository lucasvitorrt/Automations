import os
import shutil
import time

download = os.path.expanduser('~\Downloads') # caminho pasta dowload
destino = 'C:/NFE/Importador - CATALAO/'  # caminho destino
tempo_atual = time.time() 
limite_tempo = tempo_atual - (1 * 60 * 60)  # apenas arquivos baixados na ultima hora

def copyfiles():
    for arquivo in os.listdir(download): 

        if arquivo.endswith('.zip'): 
            origem = os.path.join(download, arquivo)
            
            if os.path.getmtime(origem) >= limite_tempo: # verifica a data de modificação do arquivo
                destino_arquivo = os.path.join(destino, arquivo)
                shutil.move(origem, destino_arquivo) 
                #print(f'Copiado: {arquivo}')
