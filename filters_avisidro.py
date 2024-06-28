
from os import remove
import pandas as pd
import re, ast
from tqdm import tqdm
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

pbp_percente_arr = []
pbp_kg_arr = []
pbp_real_arr = []
pcp_arr = []

avc_percente_arr = []
avc_kg_arr = []
avc_real_arr = []

acd_percent_arr = []
acd_kg_arr = []
acd_real_arr = []

acp_percent_arr = []
acp_kg_arr = []
acp_real_arr = []

acl_percent_arr = []
acl_kg_arr = []
acl_real_arr = []

rbl_percent_arr = []
rbl_kg_arr = []
rbl_real_arr = []


vrb_arr = []
vnf_arr = []
vtd_arr = []

dkm_arr =  []
adp_arr = []
qa_arr = []
dal_arr = []

qad_arr = []
qabt_arr = []

pma_arr = []
dtma_arr_d = []
prbd_arr = []
homa_arr = []
rcsmd_arr = []
pmrl_arr = []
tpo_arr = []
gpd_arr = []
pmpj_arr = []
ajs_pp_arr = []
iee_arr = []
iep_arr = []
pm_arr = []
avc_t_arr = []
pmr_pmp_arr = []
nacp_arr = []
npc_arr = []
pcp_arr = []
pcpp_arr = []
mrt_prv_arr = []
pcrl_arr  = []
pcpr_arr = []
mr_arr = []
dc_pr_arr = []
dc_pr_arr = []
dcp_pr_arr = []
dpxr_arr = []

def main():
    print("Filtrando aguarde...")
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
            # print(new_str)
            vrac_f = new_str[1].replace("% Kg R$ R$/Cab", "").replace("VRac - Vlr das Rações", "").replace(" ", "")
            vrac_arr.append(vrac_f)
            
        if "Percentual Básico de Partilha" in str(new_str):
            
            pbp_sep = remove_empty_spaces(list(new_str[1].replace("Percentual Básico de Partilha", "").split(" ")))
           
            # %
            pbp_percente_arr.append(pbp_sep[0])
            
            # kg
            pbp_kg_arr.append(pbp_sep[1])
            
            # $
            pbp_real_arr.append(pbp_sep[2])
            
        if "Avaliação Conversão" in str(new_str):
            avc_f = remove_empty_spaces(new_str[1].replace("Avaliação Conversão", "").split(" "))

            # %
            avc_percent_f=(avc_f[0])
            avc_percente_arr.append(avc_percent_f)
            
            # kg
            avc_kg_f=(avc_f[1])
            avc_kg_arr.append(avc_kg_f)
            
            # $
            avc_real_f=(avc_f[2])
            avc_real_arr.append(avc_real_f)
            
        if "Avaliação Condenação" in str(new_str):
            acd_s = remove_empty_spaces(new_str[1].replace("Avaliação Condenação", "").split(" "))
            
            # %           
            acd_percent_arr.append(acd_s[0])
            # kg
            acd_kg_arr.append(acd_s[1])
            # $
            acd_real_arr.append(acd_s[2])
            
        if "Avaliação Calo de Patas" in str(new_str):
            
            acp_sep = remove_empty_spaces(new_str[1].replace("Avaliação Calo de Patas", "").split(" "))
            
            # nc_ = (len(acp_sep))
            # if nc_ == 4:
            #     # print(acp_sep)
            #     pass
            # if nc_ == 3:
            #     print(acp_sep)
            #     pass
                           
            # %
            acp_percent_arr.append(acp_sep[0])
            # kg
            acp_kg_arr.append(acp_sep[1])
            # $
            acp_real_arr.append(acp_sep[2])           
            
        if "Avaliação Check-List" in str(new_str):
            acl_sep = (remove_empty_spaces(new_str[1].replace("Avaliação Check-List", "").split(" ")))
            nc_ = (len(acl_sep))
            if nc_ == 4:
                # %
                acl_percent = acl_sep[0]
                # KG
                acl_kg_f = acl_sep[1]
                #$
                acl_real_f = acl_sep[2]
                # print(acl_real_f)
                

                # print(acl_sep[1])
                # print(acl_[2])
                
            if nc_ == 5:
                # %
                acl_percent = acl_sep[1]
                # KG
                acl_kg_f = acl_sep[2]
                 # $
                acl_real_f = acl_sep[3]               
                
                
            acl_percent_arr.append(acl_percent)
            acl_kg_arr.append(acl_kg_f)
            acl_real_arr.append(acl_real_f)
            
            pass
        
        if "Resultado Bruto do Lote" in str(new_str):
            rbl_s = remove_empty_spaces(new_str[1].replace("Resultado Bruto do Lote", "").split(" "))
            
            #%
            # print(rbl_s[0])
            rbl_percent_arr.append(rbl_s[0])
            # rbl_percent_arr.append()
            
            #kg
            # print(rbl_s[1])
            rbl_kg_arr.append(rbl_s[1])
            
            #$
            # print(rbl_s[2])
            rbl_real_arr.append(rbl_s[2])
            
        if "Valor Renda Bruta" in str(new_str):
            vrb_s = remove_empty_spaces(new_str[1].replace("Valor Renda Bruta", "").split(" "))
            n_c = len(vrb_s)
            
            if n_c == 1:
                vrb_f = (vrb_s[0])
                
            if n_c == 2:
                vrb_f = (vrb_s[0])         
                
            vrb_arr.append(vrb_f)
            
        if "Valor NF" in str(new_str):
            vnf_s = remove_empty_spaces(new_str[1].replace("Valor NF", "").split(" "))
            
            n_c = len(vnf_s)
            
            if n_c == 1:
                vnf_f = vnf_s[0]
            if n_c == 2:
                vnf_f = vnf_s[0]
                        
            vnf_arr.append(vnf_f)
        
        if "Valor Total a Depositar" in str(new_str):
            vtd_s = remove_empty_spaces(new_str[1].replace("Valor Total a Depositar", "").split(" "))
            n_c = len(vtd_s)
            
            if n_c == 1:
                vtd_f = vtd_s[0]
                
            if n_c == 2:
                vtd_f = vtd_s[0]
                
            
            
            vtd_arr.append(vtd_f)

        if "Dist Km" in str(new_str):
            dk_s = remove_empty_spaces(new_str[1].replace("Dist Km", ", ").split(", ")[-1].split(" "))
            dkm_f = dk_s[0]
            dkm_arr.append(dkm_f)
            
        if "Área disp" in str(new_str):
            adp_f = (new_str[1].split("Área disp")[-1])
            adp_arr.append(adp_f)
            
        if "Qtde Alojada" in str(new_str):
            qa_s_f = (new_str[1].split("Data Acerto do Lote")[0].split("Qtde Alojada")[-1])
            qa_arr.append(qa_s_f)
            
        if "Data Acerto do Lote" in str(new_str):
            dal_s_f = (remove_empty_spaces(new_str[1].split("Data Acerto do Lote")[-1].split(" "))[0])
            dal_arr.append(dal_s_f)
        
        # "Qtde Abatida"
        if "Qtde Abatida" and "Data Acerto do Lote" in str(new_str):
            qabt_arr.append(new_str[2])
        
        
        if "Peso Médio Alojado" in str(new_str):
            pma_s_f = (new_str[1].split("Peso Médio Alojado")[-1].split("Data Média Abate")[0])
            pma_arr.append(pma_s_f)
            
            
        if "Data Média Abate" in str(new_str):
            dmab_s_f = (remove_empty_spaces(new_str[1].split("Peso Médio Alojado")[-1].split("Data Média Abate")[-1].split(" "))[0])
            
            dtma_arr_d.append(dmab_s_f)

        if "Peso Recebido" in str(new_str):
            n_c = len(new_str)
            if n_c == 2:
                prbd_s_f = remove_empty_spaces(new_str[1].split("Peso Recebido"))[-1]
                # print(prbd_s_f)                
            if n_c == 3:
                prbd_s_f = (new_str[-1])                
            if n_c == 4:
                pass
            
            prbd_arr.append(prbd_s_f)
            
        if "Hora média Abate" in str(new_str):
            n_c_ = len(new_str[1:])
            
            if n_c_ == 1:
                s_ = (remove_chars_s_points(line_item).split("Hora média Abate:")[-1].split(" "))
                hmabt_f = remove_empty_spaces(s_)
                hmabt_f =hmabt_f[0]
                
                
                
            if n_c_ == 2:
                s_d = remove_empty_spaces(remove_chars_s_points(line_item).split(", ")[1].split("Hora média Abate:")[-1].split(" "))
                hmabt_f = s_d[0]
                # homa_arr.append(hmabt_f)
                                
                pass
            if n_c_ == 3:
                # print(remove_chars_s_points(line_item))
                # hmabt_f = s_d[0])
                pass
            # if n_c_ == 4:
            #     pass
            # if n_c_ == 5:
            #     # print(line_item)
            #     pass
            homa_arr.append(hmabt_f)
            # print(hmabt_f)
            
        if "Ração Consumida" in str(new_str):
            
            nc_ = len(new_str)
            if nc_ == 2:
                rcsmd_s_f = (new_str[1].split("Ração Consumida")[-1].replace(" ", ""))
            if nc_ == 3:
                rcsmd_s_f = (new_str[-1].replace(" ", ""))
                
            # if nc_ == 4:
            #     # print(new_str)
            #     pass
            # rcsmd_s
            rcsmd_arr.append(rcsmd_s_f)
        
        if "Peso Médio Real" in str(new_str):
            nc_ = len(new_str)
            # if nc_ == 2:
            #     # print(new_str)
            #     pass
            if nc_ == 3:
                pmrl_s_f = (new_str[-1].replace(" ", ""))
                pass
            # if nc_ == 4:
            #     # print(new_str)
            #     pass
            pmrl_arr.append(pmrl_s_f)
            
            pass
        
        if "Tipo Produto" and "Linhagem" in str(new_str):
            
            tpo_s_f = (remove_empty_spaces(new_str[1].split("Tipo Produto")[1].split(" "))[0])
            tpo_arr.append(tpo_s_f)
            
        if "GPD" and "Linhagem" in str(new_str):
            gpd_s_f = (remove_empty_spaces(new_str[1].split("GPD")[1].split(" "))[0])
            gpd_arr.append(gpd_s_f)
        
        if "Peso Médio Projetado" in str(new_str):
            nc_ = len(new_str)
            if nc_ == 2:
                
                pass
            
            if nc_ == 3:
                pmpj_s_f = (new_str[-1])
                pmpj_arr.append(pmpj_s_f)
            
            if nc_ == 4:
                # print(new_str)
                pass
            pass
        if "Ajs Peso Pinto" in str(new_str):
            ajs_pp_s_f= (remove_empty_spaces(new_str[1].split("Ajs Peso Pinto")[-1].split(" "))[0])
            ajs_pp_arr.append(ajs_pp_s_f)
            
        if "IEE" in str(new_str):
            
            iee_s_f = remove_empty_spaces(new_str[1].split("IEE")[-1].split(" "))[0]
            iee_arr.append(iee_s_f)
            
        if "IEP" in str(new_str):
            iep_s_f = remove_empty_spaces((new_str[1].split("IEP"))[-1].split(" "))[0]
            iep_arr.append(iep_s_f)
            
        if "PM Real - PM Projetado" in str(new_str):
            pm_arr.append(new_str[-1])
            
        if "Aves Condenadas Total" in str(new_str):
           avc_t_s_f =  remove_empty_spaces(new_str[1].split("No Aves Condenadas Total"))[-1].replace(" ","")
           avc_t_arr.append(avc_t_s_f)
        
        if "PM Real - PM Projetado" in str(new_str):
            pmr_pmp = new_str[-1]
            # print(pmr_pmp)
            pmr_pmp_arr.append(pmr_pmp)
            
        if "No Aves Condenadas Parcial" in str(new_str):
            nacp_s_f = (remove_empty_spaces( new_str[1].split("No Aves Condenadas Parcial")[-1].split(" "))[0])
            nacp_arr.append(nacp_s_f)
            
            
        if "No de Patas Condenadas" in str(new_str):
            npc_s_f = (remove_empty_spaces(new_str[1].split("No de Patas Condenadas")[-1].split(" "))[0])
            npc_arr.append(npc_s_f)
            
        if "Pc Condenações - Previsto" in str(new_str):
            pcp_s_f = (remove_empty_spaces(new_str[1].split("Pc Condenações - Previsto")[1].split(" "))[0] )
            pcp_arr.append(pcp_s_f)
            
        if "Pc Calo de Pata - Previsto" in str(new_str):
            pcpp_s_f = (remove_empty_spaces(new_str[1].split("Pc Calo de Pata - Previsto")[1].split(" "))[0])
            pcpp_arr.append(pcpp_s_f)
            
        if "Mort. Prev" in str(new_str):
            mrt_prv_s_f =  (remove_empty_spaces(new_str[-1].split("Mort. Prev."))[0].replace(" ", ""))
            mrt_prv_arr.append(mrt_prv_s_f)
            
            
        if "Pc Condenações - Real" in str(new_str):
            pcrl_s_f = remove_empty_spaces(new_str[1].split("Pc Condenações - Real")[1].split(" "))[0]
            pcrl_arr.append(pcrl_s_f)
            
        if "Pc Calo de Pata - Real" in str(new_str):
            pcpr_s_f = remove_empty_spaces(new_str[1].split("Pc Calo de Pata - Real")[1].split(" "))[0]
            pcpr_arr.append(pcpr_s_f)
            
        
        if "Mort. Real" in str(new_str):
            n_c_ = len(new_str)
            # print(n_c_)
            if n_c_ == 3:
                mr_s_f = remove_empty_spaces(new_str[-1].split("Mort. Real"))[0].replace(" ", "")
                mr_arr.append(mr_s_f)
                # pass
            # elif n_c_ == 4:
            #     print(new_str)
            #     pass

        if "Difça Cond (Prev-Real)" in str(new_str):
            dc_pr_s_f = ( remove_empty_spaces(new_str[1].split("Difça Cond (Prev-Real)")[-1].split(" "))[0])
            dc_pr_arr.append(dc_pr_s_f)
        
        
        if "Difça Calo Pata (Prev-Real)" in str(new_str):
            dcp_s_f = remove_empty_spaces(new_str[1].split("Difça Calo Pata (Prev-Real)")[-1].split(" "))[0]
            dcp_pr_arr.append(dc_pr_s_f)
            
        if "Difça (PrevXReal)" in str(new_str):
            dpxr_s_f = remove_empty_spaces(new_str[1].split("Difça (PrevXReal)")[1].split(" "))[0]
            dpxr_arr.append(dpxr_s_f)
            pass

    id_uni_f = list(dict.fromkeys(map(str, id_uni)))
    integrado_arr_f = list(dict.fromkeys(map(str, integrado_arr)))
    integrado_arr_f = [f.split(", ")[1] for f in integrado_arr_f]
    # print(len(pmr_pmp_arr))
    
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
    
    new_dataFrame["PERCENTUAL_BASICO_DE_PARTILHA_%"] = pbp_percente_arr
    new_dataFrame["PERCENTUAL_BASICO_DE_PARTILHA_KG"] = pbp_kg_arr
    new_dataFrame["PERCENTUAL_BASICO_DE_PARTILHA_$"] = pbp_real_arr
    
    new_dataFrame["AVALIACAO_CONVERSAO_%"] = avc_percente_arr
    new_dataFrame["AVALIACAO_CONVERSAO_KG"] = avc_kg_arr
    new_dataFrame["AVALIACAO_CONVERSAO_$"] = avc_real_arr
    
    new_dataFrame["AVALIACAO_CONDENACAO_%"] = acd_percent_arr
    new_dataFrame["AVALIACAO_CONDENACAO_KG"] = acd_kg_arr
    new_dataFrame["AVALIACAO_CONDENACAO_$"] = acd_real_arr
    
    new_dataFrame["AVALIACAO_CALO_DE_PATAS_%"] = acp_percent_arr
    new_dataFrame["AVALIACAO_CALO_DE_PATAS_KG"] = acp_kg_arr
    new_dataFrame["AVALIACAO_CALO_DE_PATAS_$"] = acp_real_arr
    
    new_dataFrame["AVALIACAO_CHECK_LIST_%"] = acl_percent_arr
    new_dataFrame["AVALIACAO_CHECK_LIST_KG"] = acl_kg_arr
    new_dataFrame["AVALIACAO_CHECK_LIST_$"] = acl_real_arr
    
    new_dataFrame["RESULTADO_BRUTO_DO_LOTE_%"] = rbl_percent_arr
    new_dataFrame["RESULTADO_BRUTO_DO_LOTE_KG"] = rbl_kg_arr
    new_dataFrame["RESULTADO_BRUTO_DO_LOTE_$"] = rbl_real_arr
    
    new_dataFrame["VALOR_RENDA_BRUTA_CREDITO"] = vrb_arr
    new_dataFrame["VALOR_NF"] = vnf_arr
    new_dataFrame["VALOR_TOTAL_A_DEPOSITAR"] = vtd_arr
    new_dataFrame["DIST_KM"] = dkm_arr
    new_dataFrame["AREA_DISP"] = adp_arr
    new_dataFrame["QTDE_ALOJADA"] = qa_arr
    new_dataFrame["DATA_ACERTO_DO_LOTE"] = dal_arr
    new_dataFrame["QTDE_ABATIDA"] = qabt_arr
    new_dataFrame["PESO_MEDIO_ALOJADO"] = pma_arr
    new_dataFrame["DATA_MEDIA_ABATE"] = dtma_arr_d
    new_dataFrame["PESO_RECEBIDO"] = prbd_arr
    new_dataFrame['HORA_MEDIA_ABATE'] = homa_arr
    new_dataFrame['RACAO_CONSUMIDA'] = rcsmd_arr
    new_dataFrame['PESO_MEDIO_REAL'] = pmrl_arr
    new_dataFrame['TIPO_PRODUTO'] = tpo_arr
    new_dataFrame["GPD"] = gpd_arr
    new_dataFrame["PESO_MEDIO_PROJETADO"] = pmpj_arr
    new_dataFrame["AJS_PESO_PINTO"] = ajs_pp_arr
    new_dataFrame["IEE"] = iee_arr
    new_dataFrame["IEP"] = iep_arr
    new_dataFrame['PM_REAL_PM_PROJETADO'] = pm_arr
    new_dataFrame['AVES_CONDENADAS_TOTAL'] = avc_t_arr
    new_dataFrame["N_AVES_CONDENADAS_PARCIAL"] = nacp_arr
    new_dataFrame["N_PATAS_CONDENADAS"] = npc_arr
    new_dataFrame["PC_CODENACOES_PREVISTO"] = pcp_arr
    new_dataFrame["PC_CALO_DE_PATA_PREVISTO"] = pcpp_arr
    new_dataFrame["MORT_PREV"] = mrt_prv_arr
    new_dataFrame["PC_CODENACOES_REAL"] = pcrl_arr
    new_dataFrame["PC_CALO_DE_PATA_REAL"] = pcpr_arr
    new_dataFrame["MORT_REAL"] = mr_arr
    new_dataFrame["DIFCA_COND_PREV_REAL"] = dc_pr_arr    
    new_dataFrame["DIFCA_CALO_PATA_PREV_REAL"] = dcp_pr_arr    
    new_dataFrame["DIFCA_PREV_X_REAL"] = dpxr_arr
    
    
    
    
    
    

    # print(df_2)
    print("Slavando arquivo...")
    new_dataFrame.to_csv("ArquivosCSV/avisidro_tabela.csv", mode="w", index=False)
    input("Arquivo salvo com sucesso...")
main()