import pandas as pd
import re, ast

file_execel = "ArquivosCSV/file_csv.csv"
df = pd.read_csv(file_execel, encoding="utf-8")    
new_dataFrame= pd.DataFrame()
    
def find_dates(text):
    date_pattern = r"\b(0[1-9]|1[0-9]|2[0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{2})\b"
    return re.findall(date_pattern, text)

def remove_empty_spaces(lst):
    return list(filter(lambda item: item.strip() != '', lst))

def find_numbers(input_str):
    pattern = r'\b\d+\b'  # Padrão para números
    result = re.findall(pattern, input_str)
    return result

def find_letters(input_str):
    pattern = r'\b[A-Za-z\s]+\b'  # Padrão para letras
    result = re.findall(pattern, input_str)
    return result

def remove_chars(input_str):
    chars_to_remove = ["[", "\"", "'", "nan", "]", ":"]
    for char in chars_to_remove:
        input_str = input_str.replace(char, "")
    return input_str

def converter_para_float(numero_str):
    numero_str = numero_str.replace(',', '.')
    return float(numero_str)
            
    #ITERA SOBRE O NOVO DATA FRAME FILTRADO

def find_id_ifem(id_):
    id_ = ast.literal_eval(id_)
    id_ = id_[0]    
    padrao = r'\d+-\d+'
    id_f = re.match(padrao, str(id_))
    return id_f

integrado_arr = []
id_uni = []
endereco_arr = []

def main():
    for index, row in df.iterrows():
        line_item = str(row.iloc[0])
       
        
        new_str = re.sub(r"\[|\]", "", line_item)
        new_str = remove_empty_spaces(remove_chars(new_str).split(", "))
        # print(new_str)
        len_newStr = len(new_str)

        if find_id_ifem(str(new_str)):
            id_uni.append(new_str[0])
            
        if "Integrado" in str(new_str):
                        
            separe_id=remove_empty_spaces(remove_chars(str(df.loc[index+2][0])).split(", "))[0]
            if "Integrado" in new_str[0]: 
                integrado_f = separe_id+", "+find_letters(new_str[0])[1]
                
                integrado_arr.append(integrado_f)

        if "Endereço" in str(new_str):
            endereco_f = (new_str[1].replace(" Técnico ", ", ").replace("Endereço ", ""))
            endereco_f = endereco_f.split(", ")[0]
            endereco_arr.append(endereco_f)
            n_c = len(new_str)
        if "Municipio" in str(new_str):
            print(new_str)
            pass
    
    id_uni_f = list(dict.fromkeys(id_uni))
    integrado_arr_f = list(dict.fromkeys(integrado_arr))
    integrado_arr_f = [f.split(", ")[1] for f in integrado_arr_f ]
    
    new_dataFrame["CHAVE"] = id_uni_f
    new_dataFrame["INTEGRADO"] = integrado_arr_f
    new_dataFrame["ENDEREÇO"] = endereco_arr
    
    
    new_dataFrame.to_csv("ArquivosCSV/avisidro_tabela.csv", mode="w", index=False)
main()