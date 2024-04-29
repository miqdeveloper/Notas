import time
import win32com.client
import messagebox

def ATUALIZAR_ARQUIVO_EXCEL(file_path):
    try:
        # Inicie o Excel
        File = win32com.client.Dispatch("Excel.Application")
        # Torne-o visível/invisível
        # File.Visible = 1  # if 0, it processes in the background
        # Abra o arquivo
        Workbook = File.Workbooks.open(file_path)
        # Calculate all sheets in the workbook
        Workbook.Application.CalculateFullRebuild()
        # Aguarde o Excel a Atualização        
        time.sleep(10)  # pausa por 10 segundos     
        # Salve a pasta de trabalho
        Workbook.Save()
        # Exibir uma mensagem indicando a conclusão bem-sucedida
        print("O arquivo foi atualizado com sucesso!")
        #messagebox.showinfo("Operação concluída", "O arquivo foi atualizado com sucesso!")
        # Fechar planilha
        Workbook.Close()
        File.Quit()
    except Exception as e:
        # Exibir uma mensagem de erro em caso de exceção
        error_message = f"Um erro ocorreu: {str(e)}"
        print(error_message)
        #messagebox.showerror("Erro", error_message)

# Lista de caminhos de arquivos
CAMINHOS_DE_ARQUIVOS = [
    r'C:\Users\anton\OneDrive\Área de Trabalho\AVICAR_novo\BD_ABATE.xlsx',
    r'C:\Users\anton\OneDrive\Área de Trabalho\AVICAR_novo\BD_ALOJAMENTO.xlsx',
    r'C:\Users\anton\OneDrive\Área de Trabalho\AVICAR_novo\BD_CONDENA.xlsx',
    r'C:\Users\anton\OneDrive\Área de Trabalho\AVICAR_novo\BD_RAÇÃO.xlsx'
]

# Itere pelos caminhos dos arquivos e chame a função para cada um deles
for CAMINHO in CAMINHOS_DE_ARQUIVOS:
    ATUALIZAR_ARQUIVO_EXCEL(CAMINHO)