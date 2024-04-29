from os import *
from tabula import *
from tabula import read_pdf_with_template
import pandas as pd
import numpy as np 
import pypdf, time
from tqdm import tqdm


t1 = time.time()
cols = []
tabelas = {}
files = ["Notas", "ArquivosExcel", "TemplateTabula"]

chaves = [
   "INFORMAÇÕES GERAIS",
   "DADOS DO LOTE",
   "RESULTADOS DO LOTE",
   "COMPLEMENTO DE RENDA",
   "INDICADORES TÉCNICOS DO LOTE",
   "CONDENAÇÕES DE CAUSAS AGROPECUÁRIA",
   "PESO SEMANAL",
   "ORGEM DO LOTE",
   "ABATES",
   "MOVIMENTAÇÃO DE RAÇÕES",
   "HISTÓRICO DOS PEDIDOS ANTERIORES",
   "OBSERVAÇÔES",
   "FINANCIAMENTO"
   
]

for dir_ in files:
   if not path.exists(dir_):
      system(f"mkdir {dir_}")
         
def reader_pages(Nome_pdf):
   # for arquivo_pdf in listdir(files[0]):
   pdf = pypdf.PdfReader(f"{files[0]}/{Nome_pdf}")
   return int(len(pdf.pages))

def remover_dois_pontos(frase):
   frase_sem_dois_pontos = frase.replace(':', '')
   return frase_sem_dois_pontos

def manipule_array(arr):
   global colum
   char_l = []
   
   chave_atual = None
   qtd_it_arr = len(arr)
   
   for col in range(qtd_it_arr):
      
      df = pd.DataFrame(arr[col])
      df.insert(0, f"CHAVE", f"{name_file}")
      lines, coluns = df.shape
      colum = df.columns[1]
      colum = str(colum).replace(":", "")
      # print(df[colum].values)
      if colum in chaves:            
         tabelas[colum] = []
         # print(tabelas[colum])
         colum = colum
         # COLUNA EXTRAIDA 
         cols.append(colum)
         # print(colum)
      for line in range(0, lines):
         
         line_t = list(df.iloc[line].values)
         char_l=str(line_t[1]).replace(":", "")
         
         if char_l in chaves:
            chave_atual = char_l
            tabelas[char_l] = []
            # CASO A LINHA SEJA UMA COLUNA 
            cols.append(chave_atual)
            # print(chave_atual)         
         cols.append(line_t)
         # print(line_t)
         
   
   return 

def main():
   global name_file
   # Loop para converter cada PDF em um DataFrame
   try:
      for arquivo in tqdm(listdir(files[0]), desc="Processando arquivos"):
         
         if arquivo.endswith(".pdf"):
            pdf_num_pages = reader_pages(arquivo)
            nome_arquivo = path.splitext(arquivo)[0]
            name_file = nome_arquivo

            if pdf_num_pages == 3:
               templateJson = "T3.tabula-template.json"
            if pdf_num_pages == 4:
               templateJson = "T4.tabula-template.json"                 
            if pdf_num_pages == 5:
               templateJson = "T5.tabula-template.json"
            manipule_array(dfs)
            dfs = read_pdf_with_template(path.join(files[0], arquivo), f"{files[2]}/{templateJson}", stream=True)
            df = pd.DataFrame(cols)
            df.to_excel("file_execel.xlsx")
   print("Completo!")
   except Exception as err:
      print("Erro :",  err)

main()
t2 = time.time() - t1
print("Tempo de exec: ", t2)
# print(reader_pages())