# python ou py -m venv env
# .\env\Scripts\activate
# deactivate
# pip install os
# pip install pyxlsb
# pip install tabula-py
# pip install pandas
# pip install numpy
# pip install PyPDF2
# pip install tqdm
# pip uninstall tabula-py
# pip uninstall tabula
# sudo pip uninstall tabula-py
# sudo pip uninstall tabula
from os import *
from tabula import *
from tabula import read_pdf_with_template
import pandas as pd
import numpy as np
import PyPDF2 as pypdf
import time
from tqdm import tqdm

t1 = time.time()
cols = []
tabelas = {}
files = [
        r'C:\PROGRAMAÇÃO PYTHON\AVISIDRO\PDF_AVISIDRO',
        r'C:\PROGRAMAÇÃO PYTHON\AVISIDRO\ARQUIVOS_EXCEL',
        r'C:\PROGRAMAÇÃO PYTHON\AVISIDRO\MODELOS_PDF'
        ]

chaves = [
#        "ALOJAMENTO",
#        "DESEMPENHO DO LOTE",
#        "CÁLCULO DA PARTILHA DO INTEGRADO",
#        "VALORES",
#        "MOVIMENTAÇÃO (PINTOS/MATRIZES)",
#        "MOVIMENTAÇÃO (PINTOS/MATRIZES)",
#        "MOVIMENTAÇÃO (PINTOS/MATRIZES)",
#        "INFORMAÇÕES DO LOTE",
#        "MOVIMENTAÇÃO DE RAÇÃO",
#        "RETIRADA DO FRANGO PARA ABATE",
#        "HISTÓRICO DOS ÚLTIMOS LOTES",
#        "INFORMAÇÕES GERAIS",
#        "DADOS DO LOTE",
#        "RESULTADOS DO LOTE",
#        "COMPLEMENTO DE RENDA",
#        "INDICADORES TÉCNICOS DO LOTE",
#        "CONDENAÇÕES DE CAUSAS AGROPECUÁRIA",
#        "PESO SEMANAL",
#        "ORGEM DO LOTE",
#        "ABATES",
#        "MOVIMENTAÇÃO DE RAÇÕES",
#        "HISTÓRICO DOS PEDIDOS ANTERIORES",
#        "OBSERVAÇÔES",
#        "FINANCIAMENTO"
]

for dir_ in files:
    if not path.exists(dir_):
        system(f"mkdir {dir_}")
        # print(system)


def reader_pages(Nome_pdf):
    # for arquivo_pdf in listdir(files[0]):
    pdf = pypdf.PdfReader(f"{files[0]}/{Nome_pdf}")
    return int(len(pdf.pages))


def remover_dois_pontos(frase):
    frase_sem_dois_pontos = frase.replace(':', ': ')
    return frase_sem_dois_pontos
       
def limpar_linhas(df, delimitadores):
    for delimitador in delimitadores:
        df = df[~df.apply(lambda row: row.astype(str).str.contains(delimitador).any(), axis=1)]
    return df

def manipule_array(arr):
    global colum
    char_l = []

    chave_atual = None
    qtd_it_arr = len(arr)

    for col in range(qtd_it_arr):

        df = pd.DataFrame(arr[col])
        df = limpar_linhas(df, delimitadores=
                                            [
                                            'ALOJAMENTO ABATE',
                                            'DESEMPENHO DO LOTE',
                                            'CÁLCULO DA PARTILHA DO INTEGRADO',
                                            'INFORMAÇÕES DO LOTE',
                                            'MOVIMENTAÇÃO DE RAÇÃO',
                                            'RETIRADA DO FRANGO PARA ABATE',
                                            'CONDENAÇÕES DO SIF',
                                            'HISTÓRICO DOS ÚLTIMOS LOTES',
                                            'VALORES'
                                            ])
        
        df.insert(0, f"CHAVE", f"{name_file}")
        lines, coluns = df.shape
        colum = df.columns[1]
        colum = str(colum).replace(":", "")
        if colum in chaves:
            tabelas[colum] = []
            colum = colum
            cols.append(colum)
        for line in range(0, lines):

            line_t = list(df.iloc[line].values)
            char_l = str(line_t[1]).replace(":", "")

            if char_l in chaves:
                chave_atual = char_l
                tabelas[char_l] = []
                cols.append(chave_atual)
            cols.append(line_t)
 
    df = pd.DataFrame(cols)
    df.to_csv(r'C:\PROGRAMAÇÃO PYTHON\AVISIDRO\ARQUIVOS_EXCEL\TABELA_1.csv', index=False, encoding='utf-8', errors='ignore')
    return


def main():
    global name_file

    # Loop para converter cada PDF em um DataFrame
    try:
        for arquivo in tqdm(listdir(files[0]), desc="PROCESSANDO ARQUIVOS"):

            if arquivo.endswith(".pdf"):
                pdf_num_pages = reader_pages(arquivo)
                nome_arquivo = path.splitext(arquivo)[0]
                name_file = nome_arquivo
                    
                if pdf_num_pages == 2:
                    template_json = "T2.tabula-template.json"
                if pdf_num_pages == 3:
                    template_json = "T3.tabula-template.json"
#                if pdf_num_pages == 4:
#                    template_json = "T4.tabula-template.json"                 
#                if pdf_num_pages == 5:
#                    template_json = "T5.tabula-template.json"    

                dfs = read_pdf_with_template(
                    path.join(files[0], arquivo), f"{files[2]}/{template_json}", stream=True)
                manipule_array(dfs)
               # print(dfs)
    except Exception as err:
        print("Erro :",  err)


main()
t2 = time.time() - t1
print("Tempo de exec: ", t2)
# print(reader_pages())
