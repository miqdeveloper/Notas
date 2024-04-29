from operator import le
from turtle import mode
import pandas as pd
from tqdm import tqdm
import re
from yarg import get 

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
              "Supervisor",
              "Centro",
              "Conversão Alimentar"
            ]


file_execel = r'C:\PROGRAMAÇÃO PYTHON\AVIGRAND\ARQUIVOS_EXCEL\TABELA_1.csv'


def search_term(name, lines_n):
    
    int(lines_n)   

    df = pd.read_excel(file_execel)

    lines, col =df.shape 
    filter_arr = []

    for line in tqdm(range(lines), desc="Processando Linhas"):
        line_ = df.iloc[line].values
        if name in line_:            
            new_df = df.iloc[line+1: (line+lines_n)]
            new_df = filter_arr.append(pd.DataFrame(new_df))

    new_df = pd.concat(filter_arr, ignore_index=True)
    new_df.to_excel(r'C:\Users/anton/OneDrive/Área de Trabalho/AVIGRAND novo/BASE/BD_1.csv')
    
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
    df.to_csv(r'C:\Users/anton/OneDrive/Área de Trabalho/AVIGRAND novo/BASE/BD_1.csv', mode="w", index=False)
 
    
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
    arr_pedido = []
    arr_data_aloj = []
    arr_quant_alojado = []
    arr_peso_medio = []
    arr_area_aloj = []
    arr_data_abate = []
    arr_centro = []
    arr_supervisor = []
    arr_v_pinto = []
    arr_conv_alimentar_real = []
    arr_conv_alimentar_real_aj = []
    mod = []
    
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
        line_item = str(row[0])
        # print(line_item)
        
        new_str = re.sub(r"\[|\]", "", line_item)
                
        new_str = remove_chars(new_str)

        for item in arr_filter:
            if(item in new_str):            
                # Get_integrado e atributo
                if arr_filter[0] == item:
                    separate_str = remove_empty_spaces(new_str.split(",")) 
                    # print(separate_str)                   
                # Get chave
                    chave = separate_str[0]
                    key_arr.append(chave)
                # Get clifor        
                    clifor_ = find_numbers(separate_str[1])
                    clifor_arr.append(clifor_[0])               
                # Get name integrado
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
                # Get_DATA_ALOJAMENTO
                if arr_filter[3] == item:
                    separate_data_aloj = new_str.split(",")
                    data_alojamento = separate_data_aloj[1].replace("Data Alojamento ", "")
                    # print(data_alojamento)
                    arr_data_aloj.append(data_alojamento)
                # Get_linhagem 
                if arr_filter[4] == item:
                    separate_linhagem = new_str.split(",")
                    linhagem = remove_empty_spaces(separate_linhagem[1].split("Linhagem "))
                    # print(linhagem[0])
                    arr_linhagem.append(linhagem[0])
                # Get_quantidade_alojada                    
                if arr_filter[5] == item:
                    separate_quat_aloj = new_str.split(",")
                    quant_aloj = (remove_empty_spaces(separate_quat_aloj))
                    quant_aloj = quant_aloj[-1]
                    quant_aloj = quant_aloj.replace("Qtde Alojada ", "")
                    # print(quant_aloj)
                    arr_quant_alojado.append(quant_aloj)
                # Get_peso_medio_pinto
                if arr_filter[6] == item:                    
                    separate_peso_med_p = new_str.split(", ")
                    peso_med_p = separate_peso_med_p[1]
                    peso_med_p = peso_med_p.replace("Peso Méd Pintinho", "")
                    # print(peso_med_p)
                    arr_peso_medio.append(peso_med_p)
                # Get_area_aloj
                if arr_filter[7] == item:
                    separate_area_aloj = new_str.split(",")
                    area_aloj = separate_area_aloj[1].replace("Área Alojada", "")
                    # print(area_aloj)
                    arr_area_aloj.append(area_aloj)
                # Get DATA_ABATE
                if arr_filter[8] == item:
                    new_str = new_str.split(",", )
                    if find_dates(new_str[1]):
                        data_abate = new_str[1].replace("Data Abate ", "")
                        # print(data_abate)
                        arr_data_abate.append(data_abate)
                # Get_categoria
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
                # Get_TECNICO
                if arr_filter[10] == item:
                    separate_tcnico = new_str.split(", ")
                    separate_tcnico = remove_empty_spaces(separate_tcnico)
                    name_tcnico = separate_tcnico[-1].replace("Técnico ", "")
                    tecnico_arr.append(name_tcnico)
                # Get_TELEFONE
                if arr_filter[11] == item:
                    separate_tel = new_str.split(", ")
                    separate_tel = remove_empty_spaces(separate_tel)
                    telefone = separate_tel[-1].replace("Telefone", "").replace("Telefone ", "")
                    if not telefone:
                        telefone = "nan"                        
                    telefone_arr.append(telefone)
                # Get_EMAIL
                if arr_filter[12] == item:
                    separate_email = new_str.split(", ")
                    separate_email = remove_empty_spaces(separate_email)
                    email = separate_email[-1].replace("E-mail ", "").replace("E-mail", "")
                    if not email:
                        email = "nan"                
                    email_arr.append(email)
                # Get_TIPO_DE_VENTILACAO
                if arr_filter[13] == item:
                    separate_t_vent = new_str.split(", ")
                    separate_t_vent = remove_empty_spaces(separate_t_vent)
                    t_vent = separate_t_vent[-1].replace("Tipo Ventilação ", "").replace("Tipo Ventilação", "")
                    t_vent_arr.append(t_vent)
                    # print(t_vent)
                # Get_Kg/m2                
                if arr_filter[14] == item:
                    separate_kg_m2 = new_str.split(", ")
                    separate_kg_m2 = remove_empty_spaces(separate_kg_m2)
                    separate_kg_m2 = separate_kg_m2[-1].replace("Kg/m2", "").replace("Kg/m2 ", "")
                    if not separate_kg_m2:
                        separate_kg_m2 = "nan"                        
                    kgm2_arr.append(separate_kg_m2)
                # Get_MATERIAL
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
                # Get_QUANT_ABATIDA
                if arr_filter[17] == item:
                    separate_qabate = new_str.split(", ")
                    qabates_ = remove_empty_spaces(separate_qabate)
                    qabate_arr.append(qabates_[-1].replace("Qtde Abatida ", ""))
                # Get_MORTE_TOTAL
                if arr_filter[18] == item:
                    separate_mtotal = new_str.split(", ")
                    separate_mtotal = remove_empty_spaces(separate_mtotal)
                    m_total = separate_mtotal[-1].replace("Mort. Total ", "").replace("Mort. Total", "")
                    mort_total_arr.append(m_total)
                # Get_quant_mortes_arr
                if arr_filter[19] == item:
                    separate_qmortes = new_str.split(", ")
                    separate_qmortes = remove_empty_spaces(separate_qmortes)
                    separate_qmortes = separate_qmortes[-1].replace("Qtde Mortos ", "").replace("Qtde Mortos", "")
                    quant_mortes_arr.append(separate_qmortes)
                # Get_Qtde Eliminados 
                if arr_filter[20] == item:
                    separate_qmt_eliminados = new_str.split(", ")
                    separate_qmt_eliminados = remove_empty_spaces(separate_qmt_eliminados)
                    separate_qmt_eliminados = separate_qmt_eliminados[-1].replace("Qtde Eliminados ", "").replace("Qtde Eliminados", "")
                    if not separate_qmt_eliminados:
                        separate_qmt_eliminados = nan
                    quant_eliminados_arr.append(separate_qmt_eliminados)
                # Get_Idade Abate 
                if arr_filter[21] == item:
                    separate_idade_abate = new_str.split(", ")
                    separate_idade_abate = remove_empty_spaces(separate_idade_abate)
                    separate_idade_abate = separate_idade_abate[1].replace("Idade Abate ", "").replace("Idade Abate", "")
                    if not separate_idade_abate:
                        separate_idade_abate = nan
                    idade_abate_arr.append(separate_idade_abate)
                # Get_Aves Faltantes
                if arr_filter[22] == item:
                    separate_aves_falt = new_str.split(", ")
                    separate_aves_falt = remove_empty_spaces(separate_aves_falt)
                    separate_aves_falt = separate_aves_falt[-1].replace("Aves Faltantes ", "").replace("Aves Faltantes", "")
                    if not separate_aves_falt:
                        separate_aves_falt = nan
                    aves_faltantes_arr.append(separate_aves_falt)
                # Get_Peso Médio
                if arr_filter[23] == item:
                    separate_peso_m_f = new_str.split(", ")
                    separate_peso_m_f = remove_empty_spaces(separate_peso_m_f)          
                    if len(separate_peso_m_f) == 3:
                        separate_peso_m_f = separate_peso_m_f[1]
                        separate_peso_m_f = separate_peso_m_f.replace("Peso Médio ", "").replace("Peso Médio", "")     
                        if not separate_peso_m_f:
                            separate_peso_m_f = nan  
                        peso_medio_f_arr.append(separate_peso_m_f)
                # Get_GPD
                if arr_filter[24] == item:
                    separate_gpd = new_str.split(", ")
                    separate_gpd = remove_empty_spaces(separate_gpd)
                    gpd_ = separate_gpd[-1].replace("GPD ", "").replace("GPD", "")
                    if not gpd_:
                        gpd_ = nan
                    gpd_arr.append(gpd_)
                # Get_peso total
                if arr_filter[25] == item:
                    separate_p_total = new_str.split(", ")
                    separate_p_total = remove_empty_spaces(separate_p_total)
                    separate_p_total = separate_p_total[1].replace("Peso Total", "").replace("Peso Total ", "")
                    if not separate_p_total:
                        separate_p_total = nan
                    peso_total_arr.append(separate_p_total)
                # Get_CAAF
                if arr_filter[26] == item:
                    separate_caaf = new_str.split(", ")
                    separate_caaf = remove_empty_spaces(separate_caaf)
                    if (len(separate_caaf)) > 2:
                        caaf = separate_caaf[-1].replace("CAAF ", "").replace("CAAF", "")
                        if not caaf:
                            caaf = nan
                        caaf_arr.append(caaf)
                # Get_RAÇAO CONSUMIDA
                if arr_filter[27] == item:
                    separate_racao_c = new_str.split(", ")
                    separate_racao_c = remove_empty_spaces(separate_racao_c)
                    racao_c = separate_racao_c[-1].replace("Ração Consumida ", "").replace("Ração Consumida", "")
                    if not racao_c:
                        racao_c = nan
                    racao_c_arr.append(racao_c)
                # Get_VALOR KG FRANGO
                if arr_filter[28] == item:
                    separate_valor_f = new_str.split(", ")
                    separate_valor_f = remove_empty_spaces(separate_valor_f)
                    if len(separate_valor_f) == 2:
                        valor_f = (separate_valor_f[-1].replace("Valor do Frango Vivo por Kg em R$ ", "").replace("Valor do Frango Vivo por Kg em R$", ""))
                    if (len(separate_valor_f)) > 2:
                        valor_f = separate_valor_f[-1]
                    valor_f = converter_para_float(valor_f)
                    valor_kg_f_arr.append(valor_f)
                # Get_AVIARIO
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
                # Get_VALOR DA RAÇÃO
                if arr_filter[30] == item:
                    separate_kg_raca=new_str.split(", ")
                    separate_kg_raca = remove_empty_spaces(separate_kg_raca)
                    if len(separate_kg_raca) == 2:
                        val_kg = separate_kg_raca[-1].replace("Valor da Ração por Kg em R$ ", "").replace("Valor da Ração por Kg em R$", "")
                    if len(separate_kg_raca) > 2:
                        val_kg = separate_kg_raca[-1]
                    val_kg = converter_para_float(val_kg)
                    valor_kg_racao_arr.append(val_kg)
                # Get_PREÇO DO PINTO
                if arr_filter[31] == item:
                    separate_v_pinto = new_str.split(", ")
                    v_pinto_s = remove_empty_spaces(separate_v_pinto)
                    v_pinto_ = v_pinto_s[-1]
                    v_pinto_ = v_pinto_.replace("Valor do Pinto em R$ ", "").replace("Valor do Pinto em R$", "")
                    #print(separate_v_pinto)
                    arr_v_pinto.append(v_pinto_) 
                # Get_sUPERVISOR
                if arr_filter[32] == item:
                    separate_supervisor = new_str.split(", ")
                    supervisor_s = remove_empty_spaces(separate_supervisor)
                    supervisor_ = supervisor_s[-1]
                    supervisor_ = supervisor_.replace("Supervisor ", "").replace("Supervisor", "")
                    #print(supervisor_)
                    arr_supervisor.append(supervisor_)  
                # Get_CENTRO 
                if arr_filter[33] == item:
                    separate_centro = new_str.split(", ")
                    centro_s = remove_empty_spaces(separate_centro)
                    centro_ = centro_s[1]
                    centro_ = centro_.replace("Centro ", "").replace("Centro", "").replace("INTEGR. AVES DOURADOS", "")
                    #print(centro_)
                    arr_centro.append(centro_)                                                                                                                                    
                # Get_CONVERSAO ALIMENTAR
                if arr_filter[34] == item:
                    #print(new_str)
                    separate_conv_alimentar_real = new_str.split(", ")
                    conv_alimentar_real_s = remove_empty_spaces(separate_conv_alimentar_real)
                    conv_alimentar_real_ = conv_alimentar_real_s[1]
                    conv_alimentar_real_ = conv_alimentar_real_.replace("Conversão Alimentar ", "").replace("Conversão Alimentar", "")
                  # print(conv_alimentar_real_s)
                    arr_conv_alimentar_real.append(conv_alimentar_real_)
                    

# arr_conv_alimentar

    # #grava os dados para a nova tabela
    arr_pedido = list(dict.fromkeys(mod))
    
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
    new_dataFrame["PESO_MEDIO" ] = peso_medio_f_arr
    new_dataFrame["GPD" ] = gpd_arr
    new_dataFrame["PESO_TOTAL" ] = peso_total_arr
    new_dataFrame["CAAF"] = caaf_arr
    new_dataFrame["RACAO_CONSUMIDA"] = racao_c_arr
    new_dataFrame["VALOR_KG_FRANGO"] = valor_kg_f_arr
    new_dataFrame["VALOR_KG_RACAO"] = valor_kg_racao_arr  
    new_dataFrame["R$_PRECO_PINTO"] = arr_v_pinto
    new_dataFrame["SUPERVISOR"] = arr_supervisor
    new_dataFrame["CENTRO"] = arr_centro                       
    new_dataFrame["CONVERSAO_ALIMENTAR_REAL"] = arr_conv_alimentar_real 

    new_dataFrame.to_csv(r'C:\Users/anton/OneDrive/Área de Trabalho/AVIGRAND novo/BASE/BD_1.csv', mode="w", index=False)

    print("Filtragem Completa")
    print("Arquivo filter_tabela.csv salvo na pasta ArquivosCSV!"+"\n")

create_table_csv(arr_filter)

separate_()

## Integrado
## Município
## Tipo Ventilação
## Linhagem
## Técnico
## Telefone
## E-mail
## Data Alojamento
## Data Abate
## Categoria
## Kg/m2
# Qtde Alojada
## Qtde Abatida
## GPD
## Centro
## Supervisor
## Valor do Frango Vivo por Kg em R$
## Valor da Ração por Kg em R$
# Valor do Pinto em R$

# Endereço
# Área Alojada
# Instalações No

# Pintos Chegados Mortos
# Material
# Peso Méd Pintinho
# Peso Médio
# Peso Total
# Ração Consumida




# Percentual Basico
# CAAF
# Aves/m2

# Mort. Total
# Aves Faltantes
# Qtde Mortos
# Qtde Eliminados
# Mortos Transporte

# Imposto FUNRURAL
# Imposto SENAR
# Renda Líquida do Lote
# Valor Líquido a Receber
# Idade de Abate
# Peso Médio
# Mortalidade
# Conversão Alimentar
# % Condenação
# % Calo de Pata A
# % Calo de Pata B
# % Calo de Pata C
# % Arranhaduras
# % Papo Cheio
# % Condenação
# Peso Alojado
# Aves Consumida
# Aj Escala Produção
# Aj Sazonalidade
# Aj Sexo e Peso
# Aj Genética
# Aj Idade
# Remuneração Básica (RB)
# Aj Mortalidade
# Aj Conv Alimentar
# Aj Meritocracia (MT)
# Aj Calo Pata A
# Aj Calo Pata B
# Aj Calo Pata C
# Aj Arranhadurras
# Aj Papo Cheio
# Aj Condenações
# Aj Acerto Peso
# Aj Qualidade (QT)
# Aj Estrutural
# Aj Procedimento
# Aj Processos/Procedimentos (PP)
# Resultado Lote
# Renda Bruta / Ave
# Renda Bruta/Ton
# Renda Bruta / m2
# Renda Bruta / m2
# Renda Bruta / m2
# Conta Corrente Produtor
# Conta Corrente Vinculada
# Renda Líquida/Ave
# Renda Líquida / Ton