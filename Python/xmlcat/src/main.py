import functions as f
import flet as ft
import time
import os
import shutil

download = os.path.expanduser('~\Downloads') # caminho pasta dowload
destino = 'C:/NFE/Importador - CATALAO/'  # caminho destino
tempo_atual = time.time() 
limite_tempo = tempo_atual - (1 * 60 * 60)  # apenas arquivos baixados na ultima hora


def main(page: ft.Page): # Configurando a janela do aplicativo
    page.title = "Baixa XML"
    page.window_width = 310
    page.window_height = 390
    
    def on_download_click(e):     # Função para o botão "Baixar"
        try:
            # Captura o valor digitado e converte para inteiro
            days = int(input_days.value)
            output.value = f"Iniciando download para {days} dias..."
            page.update()
            progress_bar.value = 0  # Resetando a barra de progresso
            page.update()

            if f.downloadxmlmundnat(days):
                ok_cat = 1
            else:
                err_cat = 1
            
            progress_bar.value = 4 / 10  # Atualiza a barra de progresso
            output.value = f"Baixando... {int(progress_bar.value * 100)}% concluído."
            page.update()
            
            time.sleep(1)

            if f.downloadxmlflavia(days):
                ok_flavia = 1
            else:
                err_flavia = 1

            progress_bar.value = 7 / 10  # Atualiza a barra de progresso
            output.value = f"Baixando... {int(progress_bar.value * 100)}% concluído."
            page.update()

            time.sleep(1)
            
            progress_bar.value = 10 / 10  # Atualiza a barra de progresso
            output.value = f"Baixando... {int(progress_bar.value * 100)}% concluído."
            page.update()

            if ok_cat:
                output.value += "\nXML Mundo Natural baixado com sucesso!"
            elif err_cat:
                output.value += "\nErro ao baixar o XML do Mundo Natural"
            elif ok_flavia:
                output.value += "\nXML Flavia baixado com sucesso!"
            elif err_flavia:
                output.value += "\nErro ao baixar o XML da Flavia"
            
            copyfiles()
            page.update()
        except ValueError:
            output.value = "Por favor, digite um número inteiro válido!"
            page.update()
    
   
    def on_cancel_click(e):  # Função para o botão "Cancelar"
        # Limpa o campo de entrada, o campo de saída e a barra de progresso
        input_days.value = ""
        output.value = "Operação cancelada."
        progress_bar.value = 0
        page.update()

    # Função personalizada para simular o print no output
    def custom_print(message):
        output.value += f"{message}\n"
        page.update()
    
    def copyfiles():
        for arquivo in os.listdir(download): 
            if arquivo.endswith('.zip'): 
                origem = os.path.join(download, arquivo)   
                if os.path.getmtime(origem) >= limite_tempo: # verifica a data de modificação do arquivo
                    destino_arquivo = os.path.join(destino, arquivo)
                    shutil.move(origem, destino_arquivo) 
                    #print(f'Copiado: {arquivo}') # informação dos arquivos copiados.
                    output.value += (f'Copiado: {arquivo}')
    
        
    app_title = ft.Text("Baixa XML", size=20, weight="bold") # Título do aplicativo
    
    # Campo para entrada de número de dias
    input_days = ft.TextField(label="Digite aqui a quantidade de dias", keyboard_type="number", text_size=12)

    # Botões de Baixar e Cancelar
    download_button = ft.ElevatedButton(text="Baixar", on_click=on_download_click)
    cancel_button = ft.ElevatedButton(text="Cancelar", on_click=on_cancel_click)
    
    progress_bar = ft.ProgressBar(width=300, value=0) # Barra de progresso

    # Campo de saída de texto
    output = ft.Text(
        value="",
        expand=True,
        size=12,
        width=300,
        height=150,  # Define uma altura fixa para o campo de output
        overflow="auto"  # Ativa a rolagem quando o conteúdo excede a altura
    )

    # Rodapé com o nome do desenvolvedor
    developer_footer = ft.Text("Desenvolvido por Lucas Vitor.", size=10, text_align="center")

    # Adicionando os componentes na página
    page.add(   
        ft.Column(
            [
                app_title,  # Título do aplicativo centralizado
                input_days,
                ft.Row([download_button, cancel_button]),  # Organiza os botões lado a lado
                progress_bar,  # Barra de progresso
                output,
                developer_footer  # Rodapé
            ],
            alignment="center",  # Centraliza os itens no eixo vertical
            horizontal_alignment="center"  # Centraliza os itens no eixo horizontal
        )
    )

ft.app(target=main) # Executa a aplicação