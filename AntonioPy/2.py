%%time

import os
import openpyxl
from PyPDF2 import PdfReader
from tqdm import tqdm

# Diretório contendo os arquivos PDF
diretorio_pdf = r'C:\Users\anton\OneDrive\Área de Trabalho\AVIGRAND novo\PDF_TESTE'

# Criando um arquivo Excel e uma planilha
excel_file = openpyxl.Workbook()
sheet = excel_file.active

# Adicionando cabeçalhos, incluindo a nova coluna para o nome do arquivo
headers = ["Arquivo", "Dados"]
sheet.append(headers)

# Iterando sobre os arquivos no diretório PDF
for nome_arquivo in tqdm(os.listdir(diretorio_pdf), desc="Processando arquivos", unit="arquivo"):
    if nome_arquivo.endswith(".pdf"):
        caminho_arquivo = os.path.join(diretorio_pdf, nome_arquivo)

        # Abrindo um arquivo PDF existente
        with open(caminho_arquivo, "rb") as input_pdf:
            # Criando um objeto PdfReader
            pdf_reader = PdfReader(input_pdf)

            # Obtendo o número de páginas do arquivo PDF
            num_pages = len(pdf_reader.pages)

 #           for page_number in range(1):
            for page_number in range(num_pages):                
#                page = pdf_reader.pages[2] #FAZER EXTRAÇÃO SOMENTE NA PAGINA 3
                page = pdf_reader.pages[page_number]                
                text = page.extract_text()
             
                
                linhas_filtradas = [linha.replace("", "").strip()
                                    for linha in text.split('\n')
                                   
                                    if ("" in linha  )] 

                # Adicionando as linhas filtradas à planilha
                for linha in linhas_filtradas:
                    # Substituindo o texto desejado
                    linha = linha.replace("", "").replace("", "").replace("", "")

                    # Verificando se a linha não ficou vazia após a substituição
                    if linha.strip():
                        # Separando os dados por tabulação
                        dados = [nome_arquivo] + linha.split('\t')

                        # Adicionando os dados à planilha
                        sheet.append(dados)

# Salvando o arquivo Excel
excel_file.save(r'C:\Users\anton\OneDrive\Área de Trabalho\AVIGRAND novo\BASE\TAB_07_SUJO.xlsx')