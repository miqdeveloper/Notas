import pandas as pd
import re, ast

file_execel = "ArquivosCSV/file_csv.csv"
df_2 = pd.read_csv(file_execel, encoding="utf-8", index_col=0)   
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

def remove_chars_s_points(input_str):
    chars_to_remove = ["[", "\"", "'", "nan", "]"]
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
municipio_arr = []
cgc_arr = []
lote_arr = []
dtma_arr = []
hma_arr = []

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
            # print(str(new_str))
                        
            separe_id=remove_empty_spaces(remove_chars(str(df.loc[index+2][0])).split(", "))[0]
            
            if "Integrado" in new_str[1]: 
                integrado_f = separe_id+", "+find_letters(new_str[1])[1]
                # print(integrado_f)
                integrado_arr.append(integrado_f)

        if "Endereço" in str(new_str):
            endereco_f = (new_str[1].replace(" Técnico ", ", ").replace("Endereço ", ""))
            endereco_f = endereco_f.split(", ")[0]
            
            endereco_arr.append(endereco_f)
            n_c = len(new_str)
            
        if "Municipio" in str(new_str):
            muni_separate = (new_str[1]).replace("Dist", ",").split(", ")
            muni_f = muni_separate[0].replace("Municipio ", "").replace(" ", "")
            municipio_arr.append(muni_f)
            
        if "CPF/CGC" in str(new_str):
            cgc_f = find_numbers(new_str[1])[0].replace(" ", "")
            cgc_arr.append(cgc_f)
            
        if "Lote" and "Qtde Alojada" in str(new_str):
            lote_separate = new_str[1].replace("Qtde Alojada", ",").replace("Qtde Alojada ", ",").split(", ")
            lote_s_f = lote_separate[0].replace("Lote", "").replace("Lote ", "").replace(" ", "")
            lote_arr.append(lote_s_f)
            pass
        
        if "Data Média Alojto" in str(new_str):
            dtma_f = new_str[1].replace("Peso Médio Alojado", ",").split(", ")[0].replace("Data Média Alojto ", "").replace("Data Média Alojto", "")
            dtma_arr.append(dtma_f)
            
        if "Hora Média Alojto" in str(new_str):
            hma_f = remove_chars_s_points(line_item).replace("Hora média Abate:", ",").split(", ")[1].replace("Hora Média Alojto:", "").replace(" ", "")
            
            hma_arr.append(hma_f)
            pass
    
    id_uni_f = list(dict.fromkeys(id_uni))
    integrado_arr_f = list(dict.fromkeys(integrado_arr))
    integrado_arr_f = [f.split(", ")[1] for f in integrado_arr_f ]
    
    new_dataFrame["CHAVE"] = id_uni_f
    new_dataFrame["INTEGRADO"] = integrado_arr_f
    new_dataFrame["ENDEREÇO"] = endereco_arr
    new_dataFrame["MUNICIPIO"] = municipio_arr
    new_dataFrame["CPF/CGC"] = cgc_arr
    new_dataFrame["LOTE"] = lote_arr
    new_dataFrame["DATA_MEDIA_ALOJTO"] = dtma_arr
    new_dataFrame["HORA_MEDIA_ALOJTO"] = hma_arr
    # print(df_2)
    
    new_dataFrame.to_csv("ArquivosCSV/avisidro_tabela.csv", mode="w", index=False)
main()