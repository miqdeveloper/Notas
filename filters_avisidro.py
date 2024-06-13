import pandas as pd
import re, ast

file_execel = "ArquivosCSV/file_csv_avisidro.csv"

# df_2 = pd.read_csv(file_execel, encoding="utf-8", index_col=0)   
df = pd.read_csv(file_execel, encoding="utf-8")
new_dataFrame= pd.DataFrame()


def remove_last_space(s):
    return re.sub(r' +$', ' ', s).strip()

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

hma_arr = []
aa_arr = []
sexo_arr = []
linhagem_arr = []
ajs_lnhg_arr = []
psc_arr = []
cap_arr = []
car_arr = []
cra_arr = []
dp_arr = []
pf_arr = []
vrac_arr = []
pbp_arr = []
ac_arr = []
acd_arr = []
acp_arr = []
acl_arr = []
rbl_arr = []
vrb_arr = []


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
            # print(separe_id)
            
            if "Integrado" in str(new_str):
                integrado_f = separe_id+", "+remove_last_space(find_letters(str(new_str))[1])
                # integrado_f = separe_id+", "+find_letters(str(new_str))[1]
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
            
        if "Área Alojada" in str(new_str):
            arl_s = new_str[1].replace("Área Alojada ", "").replace("Área Alojada", "")
            aa_arr.append(arl_s)
            
        if "Sexo" in str(new_str):
            sexo_s = new_str[1].replace(" Idade Abate ", ", ").replace(" Idade Abate", ",")
            sexo_s = sexo_s.split(", ")[0].replace("Sexo", "").replace("Sexo ", "").replace(" ", "")
            sexo_arr.append(sexo_s)
            
        if "Linhagem" in str(new_str):
            lnh_s = new_str[1].replace("Tipo Produto", ", ").split(",")[0]
            lnh_s = lnh_s.replace("Linhagem ", "").replace("Linhagem", "")
            linhagem_arr.append(lnh_s)
            
            
        if "Ajs Lnhg" in str(new_str):
            ajs_s = new_str[1].replace("Ajs Peso Pinto", ",").split(", ")[0]
            ajs_s = ajs_s.replace("Ajs Lnhg. ", "").replace("Ajs Lnhg.", "")
            ajs_s = converter_para_float(ajs_s)
            ajs_lnhg_arr.append(ajs_s)
            
        if "Prev Semanal de Conv." in str(new_str):
            prv_sema_f = new_str[1].replace("No Aves Condenadas", ",").split(", ")[0].replace("Prev Semanal de Conv. ", "")
            psc_arr.append(prv_sema_f)
            
        if "Conv. Ajustada Prev" in str(new_str):            
            cavp_ = new_str
            cavp_ = (cavp_[1].replace("No Aves Condenadas Parcial", ", ").split(", ")[0].replace("Conv. Ajustada Prev", "").replace(" ", ""))
            cap_arr.append(cavp_)
            
        if "Conv. Alimentar Real" in str(new_str):
            car_f = new_str[1].replace("Pc Condenações - Previsto ", ", ").split(", ")[0].replace("Conv. Alimentar Real", "").replace(" ", "")
            car_arr.append(car_f)
        
        
        if "Conv. Real Ajustada" in str(new_str):
            cra_f =new_str[1].replace("Pc Condenações - Real", ", ").split(", ")[0].replace("Conv. Real Ajustada", "").replace(" ", "")
            cra_arr.append(cra_f)
            
        if "Difça (PrevXReal)" in str(new_str):
            dp_f = (new_str[1].replace("Difça Cond (Prev-Real)", ", ").split(", ")[0].replace("Difça (PrevXReal)", "").replace(" ", ""))
            dp_arr.append(dp_f)
            
        if "PF - Preço do Kg do Frango" in str(new_str):
            pf_f = new_str[1].replace("PF - Preço do Kg do Frango", "").replace(" ", "")
            pf_arr.append(pf_f)
            
        if "VRac - Vlr das Rações" in str(new_str):
            vrac_f = new_str[1].replace("% Kg R$ R$/Cab", "").replace("VRac - Vlr das Rações", "").replace(" ", "")
            vrac_arr.append(vrac_f)
            
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass
        if "" in str(new_str):
            pass

    
    id_uni_f = list(dict.fromkeys(map(str, id_uni)))
    integrado_arr_f = list(dict.fromkeys(map(str, integrado_arr)))
    integrado_arr_f = [f.split(", ")[1] for f in integrado_arr_f]
    # print(len(id_uni_f))
    # print(len(integrado_arr_f))
    
    new_dataFrame["CHAVE"] = id_uni_f
    new_dataFrame["INTEGRADO"] = integrado_arr_f
    new_dataFrame["ENDEREÇO"] = endereco_arr
    new_dataFrame["MUNICIPIO"] = municipio_arr
    new_dataFrame["CPF/CGC"] = cgc_arr
    new_dataFrame["LOTE"] = lote_arr
    new_dataFrame["DATA_MEDIA_ALOJTO"] = dtma_arr
    new_dataFrame["HORA_MEDIA_ALOJTO"] = hma_arr
    new_dataFrame["AREA_ALOJADA"] = aa_arr
    new_dataFrame["SEXO"] = sexo_arr
    new_dataFrame["LINHAGEM"] = linhagem_arr
    new_dataFrame["AJS_LNHG"] = ajs_lnhg_arr
    new_dataFrame["PREV_SEMANAL_DE_CONV"] = psc_arr
    new_dataFrame["CONV_AJUSTADA_PREV"] = cap_arr
    new_dataFrame["CONV_ALIMENTAR_REAL"] = car_arr
    new_dataFrame["CONV_REAL_AJUSTADA"] = cra_arr
    new_dataFrame["DIFCA_PREVXREAL"] = dp_arr
    new_dataFrame["PF_PRECO_DO_KG_DO_FRANGO"] = pf_arr
    new_dataFrame["VRAC_VLR_DAS_RACOES"] = vrac_arr
    # new_dataFrame["PERCENTUAL_BASICO_DE_PARTILHA"] = pbp_arr
    # new_dataFrame["AVALIACAO_CONVERSAO"] = ac_arr
    # new_dataFrame["AVALIACAO_CONDENACAO"] = acd_arr
    # new_dataFrame["AVALIACAO_CALO_DE_PATAS"] = acp_arr
    # new_dataFrame["AVALIACAO_CHECK_LIST"] = acl_arr
    # new_dataFrame["RESULTADO_BRUTO_DO_LOTE"] = rbl_arr
    # new_dataFrame["VALOR_RENDA_BRUTA"] = vrb_arr

    # print(df_2)
    
    new_dataFrame.to_csv("ArquivosCSV/avisidro_tabela.csv", mode="w", index=False)
main()