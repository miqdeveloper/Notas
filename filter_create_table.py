from hmac import new
from math import nan
from os import remove
from tkinter import W
from traceback import print_tb
import pandas as pd
from tqdm import tqdm
import re

# 'ArquivosCSV/file_csv.csv'
arr_filter = ["Integrado", 
              "Pedido", 
              "Município", 
              "Data Alojamento", 
              "Linhagem", 
              "Qtde Alojada",
              "Peso Méd Pintinho", 
              "Área Alojada", 
              "Data Abate", 
              "Categoria",
              "Técnico",
              "Telefone",
              "E-mail",
              "Tipo Ventilação",
              "Kg/m2",
              "Material",
              "Aves/m2",
              "Qtde Abatida",
              "Mort. Tota",
              "Qtde Mortos",
              "Qtde Eliminados",
              "Idade Abate",
              "Aves Faltantes",
              "Peso Médio",
              "GPD",
              "Peso Total",
              "CAAF",
              "Ração Consumida",
              "Valor do Frango Vivo por Kg em R$",
              "Instalações No",
              "Valor da Ração por Kg em R$",
              "Valor do Pinto em R$",
              "Percentual Basico",
              "Aj Escala Produção",
              "Aj Sazonalidade",
              "Aj Sexo e Peso",
              "Aj Idade",
              "Aj Mortalidade",
              "Aj Conv Alimentar",
              "Aj Meritocracia",
              "Aj Calo Pata A",
              "Aj Condenações",
              "Aj Qualidade",
            ]

file_execel = 'TABELA_1.csv'
# file_execel = 'ArquivosCSV/file_csv.csv'

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

def create_table_csv(termos_list):
    filter_arr_b = []
        
    # termos_list = []
    

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
    df.to_csv("ArquivosCSV/extract_terms_table.csv", mode="w", index=False)
    
def separate_():

    key_arr = []
    name_arr = []
    clifor_arr = []
    arr_municipio = []
    tecnico_arr = []
    telefone_arr = []
    
    email_arr = []
    t_vent_arr = []
    arr_categoria = []
    arr_linhagem =  []
    kgm2_arr = []
    material_arr = []
    ave_m2_arr = []
    
    qabate_arr = []
    mort_total_arr = []
    quant_mortes_arr = []
    quant_eliminados_arr = []
    idade_abate_arr = []
    aves_faltantes_arr = []
    peso_medio_f_arr = []
    gpd_arr = []
    peso_total_arr = []
    caaf_arr = []
    racao_c_arr = []
    valor_kg_f_arr = []
    aviario_arr = []
    valor_kg_racao_arr = []
    valor_pinto_real_arr = []
    percentual_basico_arr = []
    carne_base_arr = []
    real_base_arr = []
    arr_pedido = []
    
    
    arr_data_aloj = []
    
    arr_quant_alojado = []
    arr_peso_medio = []
    arr_area_aloj = []
    arr_data_abate = []
    
    aj_porcent_arr = []
    aj_kg_arr = []
    aj_real_arr = []

    aj_sazonalidade_percent_arr = []
    aj_sazonalidade_kg_arr = []
    aj_sazonalidade_real_arr = []
    
    aj_sex_pes_percent_arr = []
    aj_sex_pes_kg_arr = []
    aj_sex_pes_real_arr = []
    
        
    aj_idade_percent_arr = []
    aj_idade_kg_arr = []
    aj_idade_real_arr = []
    
    aj_mortalidade_percent_arr = []
    aj_mortalidade_kg_arr = []
    aj_mortalidade_real_arr = []
    
    aj_conv_alimentar_percent_arr = []
    aj_conv_alimentar_kg_arr = []
    aj_conv_alimentar_real_arr = []
    
    aj_meritocracia_mt_percent_arr = []
    aj_meritocracia_mt_kg_arr = []
    aj_meritocracia_mt_real_arr = []
    
    aj_calo_pata_a_percent_arr = []
    aj_calo_pata_a_kg_arr = []
    aj_calo_pata_a_real_arr = []
    
    condenacoes_percent_arr = []
    condenacoes_kg_arr = []
    codenacoes_real_arr = []
    
    aj_qualidade_percent_arr = []
    aj_qualidade_kg_arr = []
    aj_qualidade_real_arr = []
    
    mod = []
    mod_2 = []
    
    df = pd.read_csv(file_execel)
    
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
    for index, row in df.iterrows():
        line_item = str(row.iloc[0])
        # print(line_item)
        # print(line_item)
        
        new_str = re.sub(r"\[|\]", "", line_item)
                
        new_str = remove_chars(new_str)

        for item in arr_filter:
            if(item in new_str):
                    #get_integrado e atributo
                if arr_filter[0] == item:
                    separate_str = remove_empty_spaces(new_str.split(","))                    
                    # get clifor
                    chave = separate_str[0]
                    key_arr.append(chave)
                    
                    clifor_ = find_numbers(separate_str[1])
                    clifor_arr.append(clifor_[0])
                    
                    # get name integrado
                    name_integrado = find_letters(separate_str[-1].replace("Integrado ", ""))
                    if name_integrado:
                        name_arr.append(name_integrado[0])
                        
                # Get_PEDIDO/LOTE                
                if arr_filter[1] == item:
                    get_pedido = remove_empty_spaces(new_str.split(","))
                    n_pedido =find_numbers(get_pedido[1])                              
                    if (find_numbers(get_pedido[1])):
                        get_p = get_pedido[1].replace("Pedido ", "")
                        lote_ = remove_empty_spaces(get_p.split(" "))
                        lote_ = lote_[0].replace("Vlr", "")                        
                        if lote_:
                            mod.append(lote_)
     
                # Get_municipio
                if  arr_filter[2] == item:
                    separate_mun = new_str.split(",")
                    municipio = (separate_mun[1].replace("Município ", ""))
                    # print(municipio)
                    arr_municipio.append(municipio)
                    
                # GET_DATA_ALOJAMENTO
                if arr_filter[3] == item:
                    separate_data_aloj = new_str.split(",")
                    data_alojamento = separate_data_aloj[1].replace("Data Alojamento ", "")
                    # print(data_alojamento)
                    arr_data_aloj.append(data_alojamento)
                
                # GET_linhagem 
                if arr_filter[4] == item:
                    separate_linhagem = new_str.split(",")
                    linhagem = remove_empty_spaces(separate_linhagem[1].split("Linhagem "))
                    # print(linhagem[0])
                    arr_linhagem.append(linhagem[0])
                
                # GET_quantidade_alojada                    
                if arr_filter[5] == item:
                    separate_quat_aloj = new_str.split(",")
                    quant_aloj = (remove_empty_spaces(separate_quat_aloj))
                    quant_aloj = quant_aloj[-1]
                    quant_aloj = quant_aloj.replace("Qtde Alojada ", "")
                    # print(quant_aloj)
                    arr_quant_alojado.append(quant_aloj)
                
                #get_peso_medio_pinto
                if arr_filter[6] == item:                    
                    separate_peso_med_p = new_str.split(", ")
                    peso_med_p = separate_peso_med_p[1]
                    peso_med_p = peso_med_p.replace("Peso Méd Pintinho", "")
                    # print(peso_med_p)
                    arr_peso_medio.append(peso_med_p)
                
                # get_area_aloj
                if arr_filter[7] == item:
                    separate_area_aloj = new_str.split(",")
                    area_aloj = separate_area_aloj[1].replace("Área Alojada", "")
                    # print(area_aloj)
                    arr_area_aloj.append(area_aloj)

                # get DATA_ABATE
                if arr_filter[8] == item:
                    new_str = new_str.split(",", )
                    if find_dates(new_str[1]):
                        data_abate = new_str[1].replace("Data Abate ", "")
                        # print(data_abate)
                        arr_data_abate.append(data_abate)
                    
                #Get_categoria
                if arr_filter[9] == item:
                    separate_categoria = new_str.split(", ")
                    categoria_s = remove_empty_spaces(separate_categoria)
                    categoria_ = categoria_s[-1]
                    categoria_ = categoria_.replace("Categoria ", "").replace("Categoria", "")
                    if not categoria_:
                        # print(categoria_)
                        categoria_ = nan
                        
                    # print(categoria_)
                    arr_categoria.append(categoria_)
                    
                # GET_TECNICO
                if arr_filter[10] == item:
                    separate_tcnico = new_str.split(", ")
                    separate_tcnico = remove_empty_spaces(separate_tcnico)
                    name_tcnico = separate_tcnico[-1].replace("Técnico ", "")
                    tecnico_arr.append(name_tcnico)
                    
                # GET_TELEFONE
                if arr_filter[11] == item:
                    separate_tel = new_str.split(", ")
                    separate_tel = remove_empty_spaces(separate_tel)
                    telefone = separate_tel[-1].replace("Telefone", "").replace("Telefone ", "")
                    if not telefone:
                        telefone = "nan"                        
                    telefone_arr.append(telefone)
                    
                # GET_EMAIL
                if arr_filter[12] == item:
                    separate_email = new_str.split(", ")
                    separate_email = remove_empty_spaces(separate_email)
                    email = separate_email[-1].replace("E-mail ", "").replace("E-mail", "")
                    if not email:
                        email = "nan"                
                    email_arr.append(email)
                    
                # GET_TIPO_DE_VENTILACAO
                if arr_filter[13] == item:
                    separate_t_vent = new_str.split(", ")
                    separate_t_vent = remove_empty_spaces(separate_t_vent)
                    t_vent = separate_t_vent[-1].replace("Tipo Ventilação ", "").replace("Tipo Ventilação", "")
                    t_vent_arr.append(t_vent)
                    # print(t_vent)
                    
                # GET_Kg/m2                
                if arr_filter[14] == item:
                    separate_kg_m2 = new_str.split(", ")
                    separate_kg_m2 = remove_empty_spaces(separate_kg_m2)
                    separate_kg_m2 = separate_kg_m2[-1].replace("Kg/m2", "").replace("Kg/m2 ", "")
                    if not separate_kg_m2:
                        separate_kg_m2 = "nan"                        
                    kgm2_arr.append(separate_kg_m2)
                    
                # GET_MATERIAL
                if arr_filter[15] == item:
                    separate_material = new_str.split(", ")
                    separate_material = remove_empty_spaces(separate_material)
                    get_m = separate_material[1].split(" ")
                    if item in get_m[0]:
                        material = separate_material[1].replace("Material ", "")
                        material_arr.append(material)
                # GET_ave/m2
                if arr_filter[16] == item:
                    separate_avem2 = new_str.split(", ")
                    separate_avem2 = remove_empty_spaces(separate_avem2)
                    get_avem2 = separate_avem2[-1].replace("Aves/m2", "").replace("Aves/m2 ", "").replace(" ", "")
                    ave_m2_arr.append(get_avem2)
                # GET_QUANT_ABATIDA
                if arr_filter[17] == item:
                    separate_qabate = new_str.split(", ")
                    qabates_ = remove_empty_spaces(separate_qabate)
                    qabate_arr.append(qabates_[-1].replace("Qtde Abatida ", ""))
                
                # GET_MORTE_TOTAL
                if arr_filter[18] == item:
                    separate_mtotal = new_str.split(", ")
                    separate_mtotal = remove_empty_spaces(separate_mtotal)
                    m_total = separate_mtotal[-1].replace("Mort. Total ", "").replace("Mort. Total", "")
                    mort_total_arr.append(m_total)
                
                # GET_quant_mortes_arr
                if arr_filter[19] == item:
                    separate_qmortes = new_str.split(", ")
                    separate_qmortes = remove_empty_spaces(separate_qmortes)
                    separate_qmortes = separate_qmortes[-1].replace("Qtde Mortos ", "").replace("Qtde Mortos", "")
                    quant_mortes_arr.append(separate_qmortes)
                    
                # GET_Qtde Eliminados 
                if arr_filter[20] == item:
                    separate_qmt_eliminados = new_str.split(", ")
                    separate_qmt_eliminados = remove_empty_spaces(separate_qmt_eliminados)
                    separate_qmt_eliminados = separate_qmt_eliminados[-1].replace("Qtde Eliminados ", "").replace("Qtde Eliminados", "")
                    if not separate_qmt_eliminados:
                        separate_qmt_eliminados = nan
                    quant_eliminados_arr.append(separate_qmt_eliminados)
                    
                # GET_Idade Abate 
                if arr_filter[21] == item:
                    separate_idade_abate = new_str.split(", ")
                    separate_idade_abate = remove_empty_spaces(separate_idade_abate)
                    separate_idade_abate = separate_idade_abate[1].replace("Idade Abate ", "").replace("Idade Abate", "")
                    if not separate_idade_abate:
                        separate_idade_abate = nan
                        
                    idade_abate_arr.append(separate_idade_abate)
                
                #GET_Aves Faltantes
                if arr_filter[22] == item:
                    separate_aves_falt = new_str.split(", ")
                    separate_aves_falt = remove_empty_spaces(separate_aves_falt)
                    separate_aves_falt = separate_aves_falt[-1].replace("Aves Faltantes ", "").replace("Aves Faltantes", "")
                    if not separate_aves_falt:
                        separate_aves_falt = nan
                    aves_faltantes_arr.append(separate_aves_falt)
                    
                #GET_Peso Médio
                if arr_filter[23] == item:
                    separate_peso_m_f = new_str.split(", ")
                    separate_peso_m_f = remove_empty_spaces(separate_peso_m_f)
                    
                    if len(separate_peso_m_f) == 3:
                        separate_peso_m_f = separate_peso_m_f[1]
                        separate_peso_m_f = separate_peso_m_f.replace("Peso Médio ", "").replace("Peso Médio", "")
                        
                        if not separate_peso_m_f:
                            separate_peso_m_f = nan
                            
                        peso_medio_f_arr.append(separate_peso_m_f)
                
                # GET_GPD
                if arr_filter[24] == item:
                    separate_gpd = new_str.split(", ")
                    separate_gpd = remove_empty_spaces(separate_gpd)
                    gpd_ = separate_gpd[-1].replace("GPD ", "").replace("GPD", "")
                    if not gpd_:
                        gpd_ = nan
                    gpd_arr.append(gpd_)
                    
                # GET_peso total
                if arr_filter[25] == item:
                    separate_p_total = new_str.split(", ")
                    separate_p_total = remove_empty_spaces(separate_p_total)
                    separate_p_total = separate_p_total[1].replace("Peso Total", "").replace("Peso Total ", "")
                    if not separate_p_total:
                        separate_p_total = nan
                    peso_total_arr.append(separate_p_total)
                
                # GET_CAAF
                if arr_filter[26] == item:
                    separate_caaf = new_str.split(", ")
                    separate_caaf = remove_empty_spaces(separate_caaf)
                    if (len(separate_caaf)) > 2:
                        caaf = separate_caaf[-1].replace("CAAF ", "").replace("CAAF", "")
                        if not caaf:
                            caaf = nan
                        caaf_arr.append(caaf)
                
                # GET_Ração Consumida
                if arr_filter[27] == item:
                    separate_racao_c = new_str.split(", ")
                    separate_racao_c = remove_empty_spaces(separate_racao_c)
                    racao_c = separate_racao_c[-1].replace("Ração Consumida ", "").replace("Ração Consumida", "")
                    if not racao_c:
                        racao_c = nan
                    racao_c_arr.append(racao_c)
                
                # GET_Valor do Frango Vivo por Kg em R$
                if arr_filter[28] == item:
                    separate_valor_f = new_str.split(", ")
                    separate_valor_f = remove_empty_spaces(separate_valor_f)
                    if len(separate_valor_f) == 2:
                        valor_f = (separate_valor_f[-1].replace("Valor do Frango Vivo por Kg em R$ ", "").replace("Valor do Frango Vivo por Kg em R$", ""))
                    if (len(separate_valor_f)) > 2:
                        valor_f = separate_valor_f[-1]
                    valor_f = converter_para_float(valor_f)
                    valor_kg_f_arr.append(valor_f)
                    
                
                # GET_aviario_instalacoes
                if arr_filter[29] == item:
                    separate_av = new_str.split(", ")
                    separate_av = remove_empty_spaces(separate_av)
                    f = list(find_numbers(separate_av[2]))
                    inst_ = separate_av[1].replace("Instalações No ", "").replace("Instalações No", "")
                    if not f:
                        f = ""
                        inst_ = inst_
                    if f:
                        f=f[0]
                        inst_ = inst_ +","+f
                        
                    aviario_arr.append(inst_)
                
                # GET_Valor da Ração por Kg em R$:
                if arr_filter[30] == item:
                    separate_kg_raca=new_str.split(", ")
                    separate_kg_raca = remove_empty_spaces(separate_kg_raca)
                    if len(separate_kg_raca) == 2:
                        val_kg = separate_kg_raca[-1].replace("Valor da Ração por Kg em R$ ", "").replace("Valor da Ração por Kg em R$", "")
                    if len(separate_kg_raca) > 2:
                        val_kg = separate_kg_raca[-1]
                    val_kg = converter_para_float(val_kg)
                    valor_kg_racao_arr.append(val_kg)
                    
                # GET_VALOR_REAL_pinto
                if arr_filter[31] == item:
                    separate_pinto=new_str.split(", ")
                    separate_pinto=remove_empty_spaces(separate_pinto)
                    if len(separate_pinto) > 2:
                        val_pinto= converter_para_float(separate_pinto[-1])
                    elif len(separate_pinto) == 2:
                        val_pinto = converter_para_float(separate_pinto[-1].replace("Valor do Pinto em R$ ", "").replace("Valor do Pinto em R$", ""))
                    
                    valor_pinto_real_arr.append(val_pinto)
                
                # GET_percentual_basico AND Kg
                if arr_filter[32] == item:                    
                    separate_percentual=new_str.split(", ")
                    separate_percentual = remove_empty_spaces(separate_percentual)
                    
                    percent_basic = separate_percentual[1].replace("Percentual Basico ", "").replace("Percentual Basico", "")
                    porcetage_percent = separate_percentual[2]
                    mod_2.append(separate_percentual)
                    
                    if not percent_basic:
                       percent_basic = separate_percentual[2].split(" ")
                       percent_basic = percent_basic[0]
                   
                    percent_basic = converter_para_float(percent_basic)
                  
                    percentual_basico_arr.append(percent_basic)
                
                # GET_AJ_%_Kg_R$
                if arr_filter[33] == item:
                    aj_separate = new_str.split(", ")
                    aj_separate = remove_empty_spaces(aj_separate)
                    
                    # aj_porcent_arr.append(aj_separate)
                    
                    if len(aj_separate) == 3:
                        
                        # %_percent_aj
                        aj_percent = aj_separate[1]
                        percent_aj = aj_percent.replace("Aj Escala Produção ", "").replace("Aj Escala Produção", "")

                        # aj_kg
                        kg_aj_separate = aj_separate[-1].split(" ")
                                               
                        if len(kg_aj_separate) ==2:
                            kg_aj_final = kg_aj_separate[0]
                        if len(kg_aj_separate) == 3:
                            kg_aj_final = kg_aj_separate[1]
                            # print(kg_aj_separate)
                        
                        # aj_R$
                        aj_real_separate = aj_separate[-1].split(" ")
                        aj_real_final = aj_real_separate[-1]
                        
                        
                        if not percent_aj:
                            percent_aj = aj_separate[-1].split(" ")
                            percent_aj = percent_aj[0]
                        
                        percent_aj = converter_para_float(percent_aj)
                        aj_porcent_arr.append(percent_aj)
                        
                        kg_aj_final = converter_para_float(kg_aj_final)
                        aj_kg_arr.append(kg_aj_final)
                        
                        aj_real_arr.append(aj_real_final)

                    if len(aj_separate) == 4:
                        # print(len(aj_real_separate))
                        kg_aj_separate = aj_separate[-1].split(" ")
                        
                        kg_aj_final = kg_aj_separate[0]
                        aj_real_final = aj_separate[-1].split(" ")[-1]
                        aj_real_arr.append(aj_real_final)
                        
                        # print(aj_real_final)
                        aj_porcent_arr.append(aj_separate[2])
                        
                        aj_kg_arr.append(kg_aj_final)

                # GET_AJ_SAZONALIDADE_%_Kg_R$
                if arr_filter[34] == item:
                    aj_sazonalidade_separate = new_str.split(", ")
                    aj_sazonalidade_separate = remove_empty_spaces(aj_sazonalidade_separate)
                    n_c_ = len(aj_sazonalidade_separate)
                    
                    if n_c_ == 3:
                        
                        # GET_AJ_SAZONALIDADE_%
                        porcetage_aj_saz = (aj_sazonalidade_separate[1].replace("Aj Sazonalidade ","").replace("Aj Sazonalidade",""))
                        
                        # GET_AJ_SAZONALIDADE_KG
                        aj_saz_kg_separate = aj_sazonalidade_separate                        
                        aj_saz_kg_separate = aj_saz_kg_separate[-1].split(" ")
                        
                        # GET_AJ_SAZONALIDADE_R$
                        aj_saz_real_separate = aj_sazonalidade_separate
                        aj_saz_real_f = (aj_saz_real_separate[-1].split(" ")[-1])
                
                        if len(aj_saz_kg_separate) == 2:
                            aj_saz_kg_f = aj_saz_kg_separate[0]
            
                        if len(aj_saz_kg_separate) == 3:
                            aj_saz_kg_f = aj_saz_kg_separate[1] 

                        if not porcetage_aj_saz:
                            porcetage_aj_saz = aj_sazonalidade_separate[-1].split(" ")
                            porcetage_aj_saz = porcetage_aj_saz[0]
                        
                        # GET_AJ_SAZONALIDADE_R$
                        aj_sazonalidade_real_arr.append(aj_saz_real_f)
                        
                        aj_sazonalidade_kg_arr.append(aj_saz_kg_f)
                        
                        aj_sazonalidade_percent_arr.append(porcetage_aj_saz)
                        
                        
                    elif n_c_ == 4:
                        
                        # GET_AJ_SAZONALIDADE_%
                        porcetage_aj_saz = (aj_sazonalidade_separate[1].replace("Aj Sazonalidade ","").replace("Aj Sazonalidade",""))
                        
                        # GET_AJ_SAZONALIDADE_KG
                        aj_saz_kg_separate = aj_sazonalidade_separate
                        aj_saz_kg_f = aj_saz_kg_separate[2]
                        
                        # GET_AJ_SAZONALIDADE_R$
                        aj_saz_real_separate = aj_sazonalidade_separate
                        aj_saz_real_f = aj_saz_real_separate[-1]
                        
                        if " " in aj_saz_real_f:
                            aj_saz_real_f = aj_saz_real_f.split(" ")[-1]
                            
                        if not aj_saz_kg_f:
                            aj_saz_kg_f = nan                        
                        
                        if not porcetage_aj_saz:
                            porcetage_aj_saz = aj_sazonalidade_separate[2]
                            
                        # GET_AJ_SAZONALIDADE_R$
                        aj_sazonalidade_real_arr.append(aj_saz_real_f)
                        
                        # GET_AJ_SAZONALIDADE_KG
                        aj_sazonalidade_kg_arr.append(aj_saz_kg_f)
                        
                        # GET_AJ_SAZONALIDADE_%
                        aj_sazonalidade_percent_arr.append(porcetage_aj_saz)
                
                # GET_Aj Sexo e Peso
                if arr_filter[35] == item:
                    
                    aj_sex_pes_separate = new_str.split(", ")
                    aj_sex_pes_separate = remove_empty_spaces(aj_sex_pes_separate)
                    
                    n_c_ = len(aj_sex_pes_separate)
                    
                    if (n_c_ == 3):
                        
                        # GET_Aj Sexo e Peso_%                        
                        aj_sex_pes_f = aj_sex_pes_separate[1].replace("Aj Sexo e Peso ", "").replace("Aj Sexo e Peso", "")
                        if not aj_sex_pes_f:
                            aj_sex_pes_f = aj_sex_pes_separate[-1].split(" ")[0]
                            
                        aj_sex_pes_percent_arr.append(aj_sex_pes_f)
                        
                        # GET_Aj Sexo e Peso_kg
                        aj_sex_pes_kg_separate = aj_sex_pes_separate[-1]
                        
                        if " " in  aj_sex_pes_kg_separate:
                            
                            if len(aj_sex_pes_kg_separate.split(" ")) == 2:
                                aj_sex_pes_kg_f = aj_sex_pes_kg_separate.split(" ")[0]

                            if len(aj_sex_pes_kg_separate.split(" ")) == 3:
                                aj_sex_pes_kg_f = (aj_sex_pes_kg_separate.split(" ")[1])
                                
                        aj_sex_pes_kg_arr.append(aj_sex_pes_kg_f)
                        
                        
                        # GET_Aj Sexo e Peso_$
                        aj_sex_pes_real_separate = aj_sex_pes_separate[-1]
                
                        if " " in  aj_sex_pes_real_separate:
                            
                            if len(aj_sex_pes_real_separate.split(" ")) == 2:
                                aj_sex_pes_real_f = aj_sex_pes_real_separate.split(" ")[1]
                                
                                # print(aj_sex_pes_real_f)

                            if len(aj_sex_pes_real_separate.split(" ")) == 3:
                                aj_sex_pes_real_f = (aj_sex_pes_kg_separate.split(" ")[-1])
                            
                        aj_sex_pes_real_arr.append(aj_sex_pes_real_f)
                                                    
                    if (n_c_ == 4):
                        
                        # GET_Aj Sexo e Peso_%
                        aj_sex_pes_f = aj_sex_pes_separate[2]                                                    
                        aj_sex_pes_percent_arr.append(aj_sex_pes_f)
                        
                        # GET_Aj Sexo e Peso_kg
                        aj_sex_pes_kg_f =  aj_sex_pes_separate[2]
                        aj_sex_pes_kg_arr.append(aj_sex_pes_kg_f)
                        
                        # GET_Aj Sexo e Peso_$
                        aj_sex_pes_real_f =  aj_sex_pes_separate[3]
                        # print(aj_sex_pes_real_f)                        
                        aj_sex_pes_real_arr.append(aj_sex_pes_real_f)

                        
                    if n_c_ == 5:
                        
                        # GET_Aj Sexo e Peso_%
                        aj_sex_pes_f = aj_sex_pes_separate[2]
                        aj_sex_pes_percent_arr.append(aj_sex_pes_f)
                        
                        # GET_Aj Sexo e Peso_kg
                        aj_sex_pes_kg_f = aj_sex_pes_separate[3]  
                        aj_sex_pes_kg_arr.append(aj_sex_pes_kg_f)
                        
                        # GET_Aj Sexo e Peso_$
                        aj_sex_pes_real_f =  aj_sex_pes_separate[4]
                        aj_sex_pes_real_arr.append(aj_sex_pes_real_f)
                        # print(aj_sex_pes_separate)
                        
                    pass
                

                if arr_filter[36] == item:
                
                    aj_idade_separate = new_str.split(", ")
                    aj_idade_separate = remove_empty_spaces(aj_idade_separate)

                    n_c_ = len(aj_idade_separate)
                    
                    if n_c_ == 3:
                        
                        # GET_Aj Idade_%
                        aj_idade_percent_f = aj_idade_separate[1].replace("Aj Idade ", "").replace("Aj Idade", "")
                        
                        if not aj_idade_percent_f:
                            aj_idade_percent_f = aj_idade_separate[-1].split(" ")[0]                        
                        aj_idade_percent_arr.append(aj_idade_percent_f)
                        
                        # GET_Aj Idade_Kg
                        aj_idade_kg_f = aj_idade_separate[-1].split(" ")
                        
                        if len(aj_idade_kg_f) == 2:
                            aj_idade_kg_f = aj_idade_kg_f[0]
                            aj_idade_real_f = aj_idade_separate[-1].split(" ")[-1]

                        if len(aj_idade_kg_f) == 3:
                            aj_idade_kg_f = aj_idade_kg_f[1]
                            
                        aj_idade_kg_arr.append(aj_idade_kg_f)
                        
                        # GET_Aj Idade_$                        
                        aj_idade_real_separate = aj_idade_separate[-1]
                        n_c_ = len(aj_idade_real_separate.split(" "))

                        if n_c_  == 2:
                            aj_idade_real_f = aj_idade_real_separate.split(" ")[1]
                            pass
                        if n_c_  == 3:
                            aj_idade_real_f = aj_idade_real_separate.split(" ")[-1]
                            pass
                        aj_idade_real_arr.append(aj_idade_real_f)
                        
                    
                    if n_c_ == 4:
                        
                        # GET_Aj Idade_%
                        aj_idade_percent_f = aj_idade_separate[1].replace("Aj Idade ", "").replace("Aj Idade", "")
                        aj_idade_percent_arr.append(aj_idade_percent_f)
                        
                        # GET_Aj Idade_Kg
                        aj_idade_kg_f = aj_idade_separate
                        aj_idade_kg_f = aj_idade_kg_f[2]
                        aj_idade_kg_arr.append(aj_idade_kg_f)
                        
                        # GET_Aj Idade_$
                        aj_idade_real_f = aj_idade_separate[2]
                        aj_idade_real_arr.append(aj_idade_real_f)
                        # print(aj_idade_real_f)
                        
                        pass
                    
                    if n_c_ == 5:
                        
                        # GET_Aj Idade_%
                        aj_idade_percent_f = (aj_idade_separate[2])
                        aj_idade_percent_arr.append(aj_idade_percent_f)
                        
                        # GET_Aj Idade_Kg
                        aj_idade_kg_f = aj_idade_separate
                        aj_idade_kg_f= aj_idade_kg_f[3]
                        aj_idade_kg_arr.append(aj_idade_percent_f)
                        
                        # GET_Aj Idade_$
                        aj_idade_real_f = aj_idade_separate[-1]
                        aj_idade_real_arr.append(aj_idade_real_f)
                
                # GET_Aj_Mortalidade
                
                if arr_filter[37] == item:
                    aj_mortalidade_separate = new_str.split(", ")
                    aj_mortalidade_separate = remove_empty_spaces(aj_mortalidade_separate)
                    
                    n_c_ = len(aj_mortalidade_separate)
                    # print(n_c_)
                    
                    if n_c_ == 3:
                        
                        # Aj_Mortalidade_%
                        aj_mortalidade_f = aj_mortalidade_separate[1].replace("Aj Mortalidade ", "").replace("Aj Mortalidade", "")
                        
                        if not aj_mortalidade_f:
                            aj_mortalidade_f = aj_mortalidade_separate[2].split(" ")[0]
                        
                        aj_mortalidade_percent_arr.append(aj_mortalidade_f)
                        
                        # Aj_Mortalidade_kg
                        aj_mortalidade_kg_f = aj_mortalidade_separate[-1].split(" ")
                        
                        n_c_ = len(aj_mortalidade_kg_f)
                        
                        if n_c_ == 2:
                            aj_mortalidade_kg_f = aj_mortalidade_kg_f[0]
                        if n_c_ == 3:
                            aj_mortalidade_kg_f = aj_mortalidade_kg_f[1]
                        
                        aj_mortalidade_kg_arr.append(aj_mortalidade_kg_f)
                        
                        # Aj_Mortalidade_real
                        aj_mortalidade_real_f = aj_mortalidade_separate[-1].split(" ")[-1]                        
                        aj_mortalidade_real_arr.append(aj_mortalidade_real_f)

                    if n_c_ == 4:
                        # Aj_Mortalidade_%
                        aj_mortalidade_f = aj_mortalidade_separate[1].replace("Aj Mortalidade ", "").replace("Aj Mortalidade", "")
                        aj_mortalidade_percent_arr.append(aj_mortalidade_f)
                        
                         # Aj_Mortalidade_kg
                        aj_mortalidade_kg_f = aj_mortalidade_separate[2]
                        aj_mortalidade_kg_arr.append(aj_mortalidade_kg_f)
                        
                        # Aj_Mortalidade_real
                        aj_mortalidade_real_f = aj_mortalidade_separate[-1]
                        aj_mortalidade_real_arr.append(aj_mortalidade_real_f)

                        
                    if n_c_ == 5:
                        # Aj_Mortalidade_%
                        aj_mortalidade_f = aj_mortalidade_separate[2]
                        aj_mortalidade_percent_arr.append(aj_mortalidade_f)
                        
                        # Aj_Mortalidade_kg
                        aj_mortalidade_kg_f = aj_mortalidade_separate[3]
                        aj_mortalidade_kg_arr.append(aj_mortalidade_kg_f)
                        
                        # Aj_Mortalidade_real
                        aj_mortalidade_real_f = aj_mortalidade_separate[-1]
                        aj_mortalidade_real_arr.append(aj_mortalidade_real_f)
                
                # GET_Aj_Conv_Alimentar
                if arr_filter[38] == item:
                    # GET_Aj_Conv_Alimentar
                    aj_conv_alimentar_separate = remove_empty_spaces(new_str.split(", "))
                    n_c_ = len(aj_conv_alimentar_separate)
                    
                    
                    if n_c_ == 3:
                        
                        # GET_Aj_Conv_Alimentar_%                        
                        aj_conv_alimentar_f = aj_conv_alimentar_separate[1].replace("Aj Conv Alimentar", "").replace("Aj Conv Alimentar ", "")
                        
                        if not aj_conv_alimentar_f:
                            aj_conv_alimentar_f = aj_conv_alimentar_separate[-1].split(" ")[0]
                        
                        aj_conv_alimentar_percent_arr.append(aj_conv_alimentar_f)
                        
                        # GET_Aj_Conv_Alimentar_KG                        
                        aj_conv_alimentar_kg_f = aj_conv_alimentar_separate[-1].split(" ")
                        n_c_ = len(aj_conv_alimentar_kg_f)
                        
                        if n_c_ == 2:
                            aj_conv_alimentar_kg_f = aj_conv_alimentar_kg_f[0]                            
                        if n_c_ == 3:
                            aj_conv_alimentar_kg_f = aj_conv_alimentar_kg_f[1]
                            
                        aj_conv_alimentar_kg_arr.append(aj_conv_alimentar_kg_f)

                        # GET_Aj_Conv_Alimentar_$
                        aj_conv_alimentar_real_f = aj_conv_alimentar_separate[-1].split(" ")[-1]
                        aj_conv_alimentar_real_arr.append(aj_conv_alimentar_real_f)

                    if n_c_ == 4:
                        # GET_Aj_Conv_Alimentar_%
                        aj_conv_alimentar_f = aj_conv_alimentar_separate[1].replace("Aj Conv Alimentar", "").replace("Aj Conv Alimentar ", "")
                        aj_conv_alimentar_percent_arr.append(aj_conv_alimentar_f)
                        
                        # GET_Aj_Conv_Alimentar_KG
                        aj_conv_alimentar_kg_f = aj_conv_alimentar_separate[2]
                        aj_conv_alimentar_kg_arr.append(aj_conv_alimentar_kg_f)
                        
                        # GET_Aj_Conv_Alimentar_$
                        aj_conv_alimentar_real_f = aj_conv_alimentar_separate[-1]
                        aj_conv_alimentar_real_arr.append(aj_conv_alimentar_real_f)
                    
                    if n_c_ == 5:
                         # GET_Aj_Conv_Alimentar_%
                        aj_conv_alimentar_f = aj_conv_alimentar_separate[2]                       
                        aj_conv_alimentar_percent_arr.append(aj_conv_alimentar_f)
                        
                        # GET_Aj_Conv_Alimentar_KG
                        aj_conv_alimentar_kg_f = aj_conv_alimentar_separate[3]                        
                        aj_conv_alimentar_kg_arr.append(aj_conv_alimentar_kg_f)
                        
                        # GET_Aj_Conv_Alimentar_$
                        aj_conv_alimentar_real_f = aj_conv_alimentar_separate[-1]
                        aj_conv_alimentar_real_arr.append(aj_conv_alimentar_real_f)
                
                # GET_Aj Meritocracia (MT)
                if arr_filter[39] == item:
                    aj_meritocracia_mt_separate = new_str.split(", ")

                    # Extract the percentage value (%_Aj_Meritocracia_MT)
                    aj_meritocracia_mt_separate = remove_empty_spaces(aj_meritocracia_mt_separate)
                    n_c_ = len(aj_meritocracia_mt_separate)
                    
                    if n_c_ == 3:
                        
                        # GET_Aj Meritocracia_%
                        aj_meritocracia_mt_percent = aj_meritocracia_mt_separate[-1].split(" ")[0]
                        aj_meritocracia_mt_percent_arr.append(aj_meritocracia_mt_percent)
                        
                        # GET_Aj Meritocracia_kg
                        aj_meritocracia_mt_kg = aj_meritocracia_mt_separate[-1].split(" ")[1]
                        aj_meritocracia_mt_kg_arr.append(aj_meritocracia_mt_kg)
                        
                        aj_meritocracia_mt_real = aj_meritocracia_mt_separate[-1].split(" ")[2]
                        aj_meritocracia_mt_real_arr.append(aj_meritocracia_mt_real)
                        
                    if n_c_ == 4:
                        aj_meritocracia_mt_percent = aj_meritocracia_mt_separate[1].replace("Aj Meritocracia (MT) ", "").replace("Aj Meritocracia (MT)", "")
                        aj_meritocracia_mt_percent_arr.append(aj_meritocracia_mt_percent)
                        
                        # GET_Aj Meritocracia_kg
                        aj_meritocracia_mt_kg = aj_meritocracia_mt_separate[2]
                        aj_meritocracia_mt_kg_arr.append(aj_meritocracia_mt_kg)

                        aj_meritocracia_mt_real = aj_meritocracia_mt_separate[-1]
                        aj_meritocracia_mt_real_arr.append(aj_meritocracia_mt_real)
                        
                    if n_c_ == 5:
                        aj_meritocracia_mt_percent = aj_meritocracia_mt_separate[2]
                        aj_meritocracia_mt_percent_arr.append(aj_meritocracia_mt_percent)
                        
                        aj_meritocracia_mt_kg = aj_meritocracia_mt_separate[3]
                        aj_meritocracia_mt_kg_arr.append(aj_meritocracia_mt_kg)
                        
                        aj_meritocracia_mt_real = aj_meritocracia_mt_separate[-1]                        
                        aj_meritocracia_mt_real_arr.append(aj_meritocracia_mt_real)
                        
                
                # GET_Aj Calo Pata A
                if arr_filter[40] == item:
                    aj_calo_pata_separate = remove_empty_spaces(new_str.split(", "))
                    n_c_ = len(aj_calo_pata_separate)
                    
                    if n_c_ == 3:
                        # GET_Aj Calo Pata A_%
                        aj_calo_pata_percent = aj_calo_pata_separate[1].replace("Aj Calo Pata A ", "").replace("Aj Calo Pata A", "")
                        if not aj_calo_pata_percent:
                            aj_calo_pata_percent = aj_calo_pata_separate[-1].split(" ")[0]
                        
                        aj_calo_pata_a_percent_arr.append(aj_calo_pata_percent)
                        
                        
                        # GET_Aj Calo Pata A_KG
                        aj_calo_pata_kg = aj_calo_pata_separate[-1].split(" ")
                        if len(aj_calo_pata_kg) == 2:
                            aj_calo_pata_kg_f =  aj_calo_pata_kg[0]

                        if len(aj_calo_pata_kg) == 3:
                            aj_calo_pata_kg_f =  aj_calo_pata_kg[1]
                            
                        aj_calo_pata_a_kg_arr.append(aj_calo_pata_kg_f)
                        
                        # GET_Aj Calo Pata A_$
                        aj_calo_pata_real_f = aj_calo_pata_separate[-1].split(" ")[-1]
                        aj_calo_pata_a_real_arr.append(aj_calo_pata_real_f)
                      
                    if n_c_ == 4:
                        aj_calo_pata_percent = aj_calo_pata_separate[1].replace("Aj Calo Pata A ", "").replace("Aj Calo Pata A", "")
                        aj_calo_pata_a_percent_arr.append(aj_calo_pata_percent)
                        
                        aj_calo_pata_kg_f = aj_calo_pata_separate[2]
                        aj_calo_pata_a_kg_arr.append(aj_calo_pata_kg_f)
                        
                        aj_calo_pata_real_f = aj_calo_pata_separate[-1]
                        aj_calo_pata_a_real_arr.append(aj_calo_pata_real_f)
                        pass
                    if n_c_ == 5:
                        aj_calo_pata_percent = aj_calo_pata_separate[2]
                        aj_calo_pata_a_percent_arr.append(aj_calo_pata_percent)
                        
                        aj_calo_pata_kg_f = aj_calo_pata_separate[3]
                        aj_calo_pata_a_kg_arr.append(aj_calo_pata_kg_f)

                        aj_calo_pata_real_f = aj_calo_pata_separate[-1]
                        aj_calo_pata_a_real_arr.append(aj_calo_pata_real_f)
                        pass
                    
                    pass        
                
                # GET_ AJ_CONDENACOES
                if arr_filter[41] == item:
                    
                    aj_condenacoes_separate = remove_empty_spaces(new_str.split(", "))
                    n_c_ = len(aj_condenacoes_separate)
                    
                    if  n_c_ == 3:
                        # GET_ AJ_CONDENACOES_%
                        aj_condenacoes_percent_f = aj_condenacoes_separate[1].replace("Aj Condenações ","").replace("Aj Condenações","")
                        if not aj_condenacoes_percent_f:
                            aj_condenacoes_percent_f  = aj_condenacoes_separate[-1].split(" ")[0]                        
                        condenacoes_percent_arr.append(aj_condenacoes_percent_f)
                        
                        # GET_ AJ_CONDENACOES_KG
                        aj_condenacoes_kg_separate = aj_condenacoes_separate[-1].split(" ")
                        
                        if len(aj_condenacoes_kg_separate) == 2:
                            aj_condenacoes_kg_f = aj_condenacoes_kg_separate[0]                            
                            
                        if len(aj_condenacoes_kg_separate) == 3:
                            aj_condenacoes_kg_f = aj_condenacoes_kg_separate[1]
                        condenacoes_kg_arr.append(aj_condenacoes_kg_f)

                        # GET_ AJ_CONDENACOES_$
                        aj_condenacoes_real_separate = aj_condenacoes_separate[-1].split(" ")
                        if len(aj_condenacoes_real_separate) == 2:
                            aj_condenacoes_real_f = aj_condenacoes_real_separate[-1]
                        if len(aj_condenacoes_real_separate) == 3:
                            aj_condenacoes_real_f = aj_condenacoes_real_separate[-1]
                        
                        codenacoes_real_arr.append(aj_condenacoes_real_f)
                                          
                    if  n_c_ == 4:
                        
                        # GET_ AJ_CONDENACOES_%
                        aj_condenacoes_percent_f = aj_condenacoes_separate[1].replace("Aj Condenações ","").replace("Aj Condenações","")
                        if not aj_condenacoes_percent_f:
                            aj_condenacoes_percent_f  = aj_condenacoes_separate[2]                            
                        condenacoes_percent_arr.append(aj_condenacoes_percent_f)
                        
                        # GET_ AJ_CONDENACOES_KG
                        aj_condenacoes_kg_f_ = aj_condenacoes_separate[-1]                        
                        if " " not in aj_condenacoes_kg_f_:
                            aj_condenacoes_kg_f = aj_condenacoes_separate[2]                            
                        if " " in aj_condenacoes_kg_f_: 
                            aj_condenacoes_kg_f = aj_condenacoes_kg_f_[0]                            
                        condenacoes_kg_arr.append(aj_condenacoes_kg_f)
                        
                        # GET_ AJ_CONDENACOES_$
                        aj_condenacoes_real_separate = aj_condenacoes_separate[-1]
                        if " " in aj_condenacoes_real_separate:
                            aj_condenacoes_real_f = aj_condenacoes_separate[-1].split(" ")[-1]
                        else:
                            aj_condenacoes_real_f = aj_condenacoes_separate[-1]
                        
                        codenacoes_real_arr.append(aj_condenacoes_real_f)
                        
                    if  n_c_ == 5:
                        
                        # GET_ AJ_CONDENACOES_% 
                        aj_condenacoes_percent_f = aj_condenacoes_separate[2]
                        condenacoes_percent_arr.append(aj_condenacoes_percent_f)
                        
                        # GET_ AJ_CONDENACOES_KG
                        aj_condenacoes_kg_f = aj_condenacoes_separate[3]
                        condenacoes_kg_arr.append(aj_condenacoes_kg_f)
                        
                        # GET_ AJ_CONDENACOES_$
                        aj_condenacoes_real_separate = aj_condenacoes_separate[-1]
                        codenacoes_real_arr.append(aj_condenacoes_real_f)
                
                if arr_filter[42] == item:
                    print(new_str)
                    
                    pass        
    # A partir do GET_percentual_basico pega Get_Kg_carne e pega $R_Base
    for eval_ in mod_2:
        if len(eval_) == 3:
            carne_final = eval_[2].split(" ")[1]
            real_base = eval_[2].split(" ")[-1]
            real_base_arr.append(real_base)
            # print(real_base)
            
            carne_base_arr.append(carne_final)
            
        if len(eval_) == 4:
            carne_base_arr.append(eval_[2])
            real_base = eval_[-1]
            real_base_arr.append(real_base)
            
        if len(eval_) == 5:
            carne_base_arr.append(eval_[3])
            real_base = eval_[-1]
            real_base_arr.append(real_base)
            
    # for value in aj_porcent_arr:
        # print(value)
    print(len(codenacoes_real_arr))                
    # print(len(valor_kg_f_arr))
    print(len(arr_filter))
    # #grava os dados para a nova tabela
    arr_pedido = list(dict.fromkeys(mod))
    # print(len(tecnico_arr), len(key_arr))
    new_dataFrame["CHAVE"] = key_arr
    new_dataFrame["CLIFOR"] =  clifor_arr
    new_dataFrame["INTEGRADO"] = name_arr
    new_dataFrame["MUNICIPIO"] = arr_municipio
    new_dataFrame["TECNICO"] = tecnico_arr
    new_dataFrame["AREA_ALOJ"] = arr_area_aloj
    new_dataFrame["TELEFONE"] = telefone_arr
    new_dataFrame["AVIARIO"] = aviario_arr
    new_dataFrame["EMAIL"] = email_arr
    new_dataFrame["T_VENTILACAO"] = t_vent_arr
    new_dataFrame["TIPO_PRODUTO"] = arr_categoria
    new_dataFrame["LINHAGEM"] = arr_linhagem
    new_dataFrame["KG_M2"] = kgm2_arr
    new_dataFrame["MATERIAL_GENETICO"] = material_arr
    new_dataFrame["AVE_M2"] = ave_m2_arr
    new_dataFrame["QUANT_ALOJADO"] = arr_quant_alojado
    new_dataFrame["DATA_ALOJ"] = arr_data_aloj
    new_dataFrame["QUANT_ABATE"] = qabate_arr
    new_dataFrame["MORTE_TOTAL"] = mort_total_arr
    new_dataFrame["QUANTIDADE_MORTOS"] = quant_mortes_arr
    new_dataFrame["QUANTIDADE_ELIMINADOS"] = quant_eliminados_arr
    new_dataFrame["DATA_ABATE"] = arr_data_abate
    new_dataFrame["IDADE_ABATE"] = idade_abate_arr
    new_dataFrame["PM_PINTO"] = arr_peso_medio
    new_dataFrame["AVES_FALTANTES"] = aves_faltantes_arr
    new_dataFrame["PESO_MEDIO"] = peso_medio_f_arr
    new_dataFrame["GPD"]=gpd_arr
    new_dataFrame["PESO_TOTAL"] = peso_total_arr
    new_dataFrame["CAAF"] = caaf_arr
    new_dataFrame["RACAO_CONSUMIDA"] = racao_c_arr
    new_dataFrame["VALOR_KG_FRANGO"] = valor_kg_f_arr
    new_dataFrame["VALOR_KG_RACAO"] = valor_kg_racao_arr
    new_dataFrame["VALOR_DO_PINTO"] = valor_pinto_real_arr
    new_dataFrame["PERCENTUAL_BASICO"] = percentual_basico_arr
    new_dataFrame["KG_CARNE_BASE"] = carne_base_arr
    new_dataFrame["R$_BASE"] = real_base_arr
    
    new_dataFrame['%_AJ_ESCALA_PROD'] = aj_porcent_arr
    new_dataFrame['KG_AJ_ESCALA_PROD'] = aj_kg_arr
    new_dataFrame["R$_AJ_ESCALA_PROD"] = aj_real_arr
    
    new_dataFrame["%_SAZONALIDADE"] = aj_sazonalidade_percent_arr    
    new_dataFrame["KG_SAZONALIDADE"] = aj_sazonalidade_kg_arr
    new_dataFrame["R$_SAZONALIDADE"] = aj_sazonalidade_real_arr
    
    new_dataFrame["%_AJ_SEXO_PESO"] = aj_sex_pes_percent_arr
    new_dataFrame["KG_AJ_SEXO_PESO"] = aj_sex_pes_kg_arr
    new_dataFrame["R$_AJ_SEXO_PESO"] = aj_sex_pes_real_arr
    
    new_dataFrame["%_AJ_IDADE"] = aj_idade_percent_arr
    new_dataFrame["KG_AJ_IDADE"] = aj_idade_kg_arr 
    new_dataFrame["R$_AJ_IDADE"] =  aj_idade_real_arr
    
    new_dataFrame["%_AJ_MORTALIDADE"] =  aj_mortalidade_percent_arr
    new_dataFrame["KG_AJ_MORTALIDADE"] =  aj_mortalidade_kg_arr
    new_dataFrame["R$_AJ_MORTALIDADE"] =  aj_mortalidade_real_arr

    new_dataFrame["%_CONV_ALIMENTAR"] =  aj_conv_alimentar_percent_arr
    new_dataFrame["KG_CONV_ALIMENTAR"] =  aj_conv_alimentar_kg_arr
    new_dataFrame["R$_CONV_ALIMENTAR"] =  aj_conv_alimentar_real_arr
    
    # new_dataFrame["LOTE"] = arr_pedido

    new_dataFrame["%_AJ_MERITOCRACIA_MT"] = aj_meritocracia_mt_percent_arr
    new_dataFrame["KG_AJ_MERITOCRACIA_MT"] = aj_meritocracia_mt_kg_arr
    new_dataFrame["R$_AJ_MERITOCRACIA_MT"] = aj_meritocracia_mt_real_arr

    new_dataFrame["%_AJ_CALO_PATA_A"] = aj_calo_pata_a_percent_arr
    new_dataFrame["KG_AJ_CALO_PATA_A"] = aj_calo_pata_a_kg_arr
    new_dataFrame["R$_AJ_CALO_PATA_A"] = aj_calo_pata_a_real_arr

    new_dataFrame["%_CONDENACOES"] = condenacoes_percent_arr
    new_dataFrame["KG_CONDENACOES"] = condenacoes_kg_arr
    new_dataFrame["R$_CONDENACOES"] = codenacoes_real_arr

    new_dataFrame["%_AJ_QUALIDADE_QT"] = aj_qualidade_percent_arr
    # new_dataFrame["KG_AJ_QUALIDADE_QT"] = aj_qualidade_qt_kg_arr
    # new_dataFrame["R$_AJ_QUALIDADE_QT"] = aj_qualidade_qt_rs_arr

    # new_dataFrame["%_AJ_ESTRUTURAL"] = aj_estrutural_percent_arr
    # new_dataFrame["KG_AJ_ESTRUTURAL"] = aj_estrutural_kg_arr
    # new_dataFrame["R$_AJ_ESTRUTURAL"] = aj_estrutural_rs_arr


    new_dataFrame.to_csv("ArquivosCSV/filter_tabela.csv", mode="w", index=False)

    print("Filtragem Completa")
    print("Arquivo filter_tabela.csv salvo na pasta ArquivosCSV!"+"\n")

#A funcao abaixo recebe 2 argumentos um string e um inteiro
# A string e a tabela que quer filtrar o inteiro significa a linha limite, ate que linha sera lido.

# search_term("ORGEM DO LOTE", 30, ["Pinto", "data", "Data", "10.0", "10,00"])


#A funcao recebe um argumento ARRAY
#A linha que sera filtrada com base no termo

# exemplo de uso:line_filter(["Pinto", "data", "Data", "10.0", "10,00"])

# create_table_csv(arr_filter)

separate_()