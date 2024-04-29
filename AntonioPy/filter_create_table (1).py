import pandas as pd
from tqdm import tqdm
import re 
# 'ArquivosCSV/file_csv.csv'

file_execel = r'C:\PROGRAMAÇÃO PYTHON\AVIGRAND\ARQUIVOS_EXCEL\TABELA_1.csv'


def search_term(name, lines_n):
    
    int(lines_n)   
    
    # "TABELA_1.xlsx"
    df = pd.read_excel(file_execel)

    lines, col =df.shape 
    filter_arr = []

    for line in tqdm(range(lines), desc="Processando Linhas"):
        line_ = df.iloc[line].values
        if name in line_:            
            new_df = df.iloc[line+1: (line+lines_n)]
            new_df = filter_arr.append(pd.DataFrame(new_df))

    new_df = pd.concat(filter_arr, ignore_index=True)
    new_df.to_excel("filter_term.xlsx")
    
    print("Filtragem Completa")
    print("Arquivo filter_term.xlsx salvo!"+"\n")




def TABELA_1(termos_list):
    
    filter_arr_b = []
    key_arr = []
    name_arr = []
    clifor_arr = []
    
    # termos_list = []
    
    def remove_chars(input_str):
        chars_to_remove = ["[", "\"", "'", "nan", "]", ":"]
        for char in chars_to_remove:
            input_str = input_str.replace(char, "")
        return input_str
    
    def find_numbers(input_str):
        pattern = r'\b\d+\b'  # Padrão para números
        result = re.findall(pattern, input_str)
        return result
    
    def find_letters(input_str):
        pattern = r'\b[A-Za-z\s]+\b'  # Padrão para letras
        result = re.findall(pattern, input_str)
        return result

    df = pd.read_csv(file_execel)
    lines, col = df.shape 
    
    for line in tqdm(range(lines), desc="Processando Linhas"):
        for palavra_  in termos_list:
            line_ = df.iloc[line].values
            # print(line_[0])
            line_ = str(line_[0])
            
            if palavra_ in line_:
                filter_arr_b.append(line_)
            
    df = pd.DataFrame(filter_arr_b)
    
    new_dataFrame= pd.DataFrame()
    
     #ITERA SOBRE O NOVO DATA FRAME FILTRADO
    for index, row in df.iterrows():
        line_item = str(row[0])
        
    
        new_str = re.sub(r"\[|\]", "", line_item)
                
        new_str = remove_chars(new_str)
        # get chave primary
        chave = new_str.split(",")
        chave = chave[0]
        key_arr.append(chave)
        
        # get clifor data
        clifor_separate = find_numbers(new_str)
        clifor = clifor_separate[-1]
        clifor_arr.append(clifor)
        # new_str = new_str.split(",", )
        
        # get letters name 
        name_get = find_letters(new_str)
        name_integrado = name_get[-1]
        name_arr.append(name_integrado)
   
        print(chave, clifor, name_integrado)
        
    #grava os dados para a nova tabela
    new_dataFrame["CHAVE"] = key_arr
    new_dataFrame["CLIFOR"] =  clifor_arr
    new_dataFrame["INTEGRADO"] = name_arr
    new_dataFrame.to_csv(r'C:\Users/anton/OneDrive/Área de Trabalho/AVIGRAND novo/BASE/BD_1.csv', mode="w")
    # df.to_excel("filter_line.xlsx")
    

    print("Filtragem Completa")
    print("Arquivo create_table.csv salvo!"+"\n")

def TABELA_2(termos_list):
    
    filter_arr_b = []
    key_arr = []
    tecnico_arr = []
    municipio_arr = []
    
    # termos_list = []
    
    def remove_chars(input_str):
        chars_to_remove = ["[", "\"", "'", "nan", "]", ":"]
        for char in chars_to_remove:
            input_str = input_str.replace(char, "")
        return input_str
    
    def find_numbers(input_str):
        pattern = r'\b\d+\b'  # Padrão para números
        result = re.findall(pattern, input_str)
        return result
    
    def find_letters(input_str):
        pattern = r'\b[A-Za-z\s]+\b'  # Padrão para letras
        result = re.findall(pattern, input_str)
        return result

    df = pd.read_csv(file_execel)
    lines, col = df.shape 
    
    for line in tqdm(range(lines), desc="Processando Linhas"):
        for palavra_  in termos_list:
            line_ = df.iloc[line].values
            # print(line_[0])
            line_ = str(line_[0])
            
            if palavra_ in line_:
                filter_arr_b.append(line_)
            
    df = pd.DataFrame(filter_arr_b)
    
    new_dataFrame= pd.DataFrame()
    
     #ITERA SOBRE O NOVO DATA FRAME FILTRADO
    for index, row in df.iterrows():
        line_item = str(row[0])
        
    
        new_str = re.sub(r"\[|\]", "", line_item)
                
        new_str = remove_chars(new_str)
        # get chave primary
        chave = new_str.split(",")
        chave = chave[0]
        key_arr.append(chave)
        
        # get letters municipio      
        municipio_str = find_letters(new_str)
        municipio = municipio_str[0]
        municipio_arr.append(municipio)
        
        # get letters tecnico
        tecnico_str = find_letters(new_str)
        name_tecnico = tecnico_str[-1]
        tecnico_arr.append(name_tecnico)
   
        print(chave, municipio, name_tecnico)
        
    #grava os dados para a nova tabela
    new_dataFrame["CHAVE"] = key_arr
    new_dataFrame["MUNICIPIO"] =  municipio_arr
    new_dataFrame["TECNICO"] = tecnico_arr
    new_dataFrame.to_csv(r'C:\Users/anton/OneDrive/Área de Trabalho/AVIGRAND novo/BASE/BD_2.csv', mode="w")
    # df.to_excel("filter_line.xlsx")
    

    print("Filtragem Completa")
    print("Arquivo create_table.csv salvo!"+"\n")

def TABELA_3(termos_list):
    
    filter_arr_b = []
    key_arr = []
    endereco_arr = []
    supervisor_arr = []
    
    # termos_list = []
    
    def remove_chars(input_str):
        chars_to_remove = ["[", "\"", "'", "nan", "]", ":", "Supervisor"]
        for char in chars_to_remove:
            input_str = input_str.replace(char, "")
        return input_str
    
    def find_numbers(input_str):
        pattern = r'\b\d+\b'  # Padrão para números
        result = re.findall(pattern, input_str)
        return result
    
    def find_letters(input_str):
        pattern = r'\b[A-Za-z\s]+\b'  # Padrão para letras
        result = re.findall(pattern, input_str)
        return result

    df = pd.read_csv(file_execel)
    lines, col = df.shape 
    
    for line in tqdm(range(lines), desc="Processando Linhas"):
        for palavra_  in termos_list:
            line_ = df.iloc[line].values
            # print(line_[0])
            line_ = str(line_[0])
            
            if palavra_ in line_:
                filter_arr_b.append(line_)
            
    df = pd.DataFrame(filter_arr_b)
    
    new_dataFrame= pd.DataFrame()
    
     #ITERA SOBRE O NOVO DATA FRAME FILTRADO
    for index, row in df.iterrows():
        line_item = str(row[0])
        
    
        new_str = re.sub(r"\[|\]", "", line_item)
                
        new_str = remove_chars(new_str)
        # get chave primary
        chave = new_str.split(",")
        chave = chave[0]
        key_arr.append(chave)
        
        # get letters endereco     
        endereco_str = find_letters(new_str)
        endereco = endereco_str[0] # TEM QUE DAR UM GEITO DE TRAZER O ENDEREÇO INTEIRO ELE ESTA SE DIVIDINDO
        endereco_arr.append(endereco)
        
        # get letters supervisor
        supervisor_str = find_letters(new_str)
        name_supervisor = supervisor_str[-1]
        supervisor_arr.append(name_supervisor)
   
        print(chave, endereco, name_supervisor)
        
    #grava os dados para a nova tabela
    new_dataFrame["CHAVE"] = key_arr
    new_dataFrame["ENDERECO"] =  endereco_arr
    new_dataFrame["SUPERVISOR"] = supervisor_arr
    new_dataFrame.to_csv(r'C:\Users/anton/OneDrive/Área de Trabalho/AVIGRAND novo/BASE/BD_3.csv', mode="w")
    # df.to_excel("filter_line.xlsx")
    

    print("Filtragem Completa")
    print("Arquivo create_table.csv salvo!"+"\n")


#A funcao abaixo recebe 2 argumentos um string e um inteiro
# A string e a tabela que quer filtrar o inteiro significa a linha limite, ate que linha sera lido.

# search_term("ORGEM DO LOTE", 30, ["Pinto", "data", "Data", "10.0", "10,00"])


#A funcao recebe um argumento ARRAY
#A linha que sera filtrada com base no termo

# exemplo de uso:line_filter(["Pinto", "data", "Data", "10.0", "10,00"])

TABELA_1(["Integrado"])

TABELA_2(["Município"])

TABELA_3(["Endereço"])

# PALAVRA CHAVE
# Centro
# Integrado
# Município
# Endereço
# Área Alojada
# Instalações No
# Tipo Ventilação