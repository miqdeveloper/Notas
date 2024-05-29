import pandas as pd
import re

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

def main():
    for index, row in df.iterrows():
        line_item = str(row.iloc[0])
        # print(line_item)
        
        new_str = re.sub(r"\[|\]", "", line_item)
        new_str = remove_empty_spaces(remove_chars(new_str).split(", "))
        len_newStr = len(new_str)
        
        if len_newStr == 1:
            pass
        if "Integrado" in new_str[0]:
            # print(new_str)
            pass
        if "Difça Calo Pata (Prev-Real)" in str(new_str):
            n_c = len(new_str)
            if n_c == 3:
                print(new_str[1:])
            pass

main()