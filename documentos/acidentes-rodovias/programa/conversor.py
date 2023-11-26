from datetime import datetime
import os
import pandas as pd
import sqlite3
import pandas as pd

class Trecho:    
    def __init__(self,id, descricao):
        self.id = id
        self.descricao = descricao


class TipoAcidente:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
        

def gravar_arquivo_layout_novo(nome_arquivo, dados):
    path_demo_novo = 'C:/mvp/puc-rio-mvp-sprint-04-sistemas-inteligentes/documentos/acidentes-rodovias/novo_layout'
    path_arq_novo = f'{path_demo_novo}/{nome_arquivo}'

    # exclui o arquivo se existir
    if os.path.exists(path_arq_novo):
        os.remove(path_arq_novo)

    # grava todo o conteudo
    with open(path_arq_novo, 'w') as f:
        f.writelines(dados)

def valor_numerico(valor):
    if (str(valor) == 'nan' or str(valor)==''):
        return "0"
    
    return valor

def classificar_tipo_acidente(ilesos,leve, moderado, grave, mortos):
    if (str(mortos).strip()!='' and str(mortos).strip()!= '0'):
        return 3
    elif (str(grave).strip()!='' and str(grave).strip()!='0'):
        return 2
    elif (str(moderado).strip()!='' and str(moderado).strip() !='0'):
        return 2
    elif (str(leve).strip() !='' and str(leve).strip()!= '0'):
        return 1
    elif (str(ilesos).strip() !='' and str(ilesos)):
        return 1
    else:
        return 1

def layout_customizado(dados, icon):
    
    total_linhas = len(dados)
    retorno = []
    linha = ''
    i = 1
                 
    for dado in dados:      
        info = dado.split(';')
        if (str(info[10]).strip() !='' and str(info[10]).strip() != '0' ):

            codigo_classificacao = classificar_tipo_acidente(info[18], info[19], info[20], info[21], info[22].removesuffix('\n'))

            linha = ''
            linha = str(info[0])
            linha = linha + ';' + str(info[1])      
            linha = linha + ';' + str(info[2])       
            linha = linha + ';' + str(info[3])       
            linha = linha + ';' + str(info[4])       
            linha = linha + ';' + str(info[5])       
            linha = linha + ';' + str(info[6])       
            linha = linha + ';' + str(info[7])                      
            linha = linha + ';' + str(info[10])  
            linha = linha + ';' + str(info[18])      
            linha = linha + ';' + str(info[19])      
            linha = linha + ';' + str(info[20])      
            linha = linha + ';' + str(info[21])      
            linha = linha + ';' + str(info[22]).removesuffix('\n')
            linha = linha + ';' + str(codigo_classificacao)

            retorno.append(linha + '\n')

        print (f'{icon} - {i} - {total_linhas}')
                             
        i = i + 1
            
    return retorno

def tratar_dados():    
    path_demo_original = 'C:/mvp/puc-rio-mvp-sprint-04-sistemas-inteligentes/documentos/acidentes-rodovias/demonstrativo_originais'

    nome_lista_concessionarias = 'Lista_concessionarias.csv'
    icon = 1
    pth_lista_concessionario_completa = f'{path_demo_original}/{nome_lista_concessionarias.strip()}'
  
    with open(pth_lista_concessionario_completa, "r") as arquivo:
        lista_concessionarias = arquivo.readlines() 
    
    for linha in lista_concessionarias:      
        infolinha = linha.split(',')   
        nome_concessionaria = infolinha[2].removesuffix('\n')
        path_arquivo = f'{path_demo_original}/{nome_concessionaria}'
        with open(path_arquivo, "r") as arquivo:
            dados_originais = arquivo.readlines()

        dados_layout_novo = layout_customizado(dados_originais, icon)    
            
        gravar_arquivo_layout_novo(nome_concessionaria, dados_layout_novo)
        icon = icon + 1

def gravar_tipos(lista):
    i = 1
    inserts = []
    path_arq_insert = 'c:/temp/insert_tipo_acidente.sql'

    if os.path.exists(path_arq_insert):
        os.remove(path_arq_insert)
    
    for tipo in lista:
        sql = f"INSERT INTO tipo_acidente VALUES({i},'{tipo}')\n"
        inserts.append(sql)
        i=i+1

    # grava todo o conteudo
    with open(path_arq_insert, 'w') as f:
        f.writelines(inserts )
 
def codigo_ponto_cardeal(descricao):
    codigo = 0

    if descricao == 'SUL':
        codigo = 1
    elif descricao == 'NORTE':
        codigo = 2
    elif descricao == 'LESTE':
        codigo = 3
    elif descricao == 'OESTE':
        codigo = 4

    return codigo        

def montar_lista_trecho(lista, dados):
    existe_na_lista = False

    for dado in dados:
        info = dado.split('')
        trecho = info[5]

        if trecho != "trecho":
            if (len(lista) == 0):
                lista.append(trecho.strip())
                existe_na_lista = False
            else:
                existe_na_lista = False
                for item in lista:
                    if trecho.strip() == item.strip():
                        existe_na_lista = True
                        break

                if existe_na_lista == False:
                    lista.append(trecho.strip())    

def montar_lista_tipo_acidentes(lista, dados):
    existe_na_lista = False

    for dado in dados:
        info = dado.split('')
        tipo_acidente = info[7]

        if tipo_acidente != "tipo_acidente":
            if (len(lista) == 0):
                lista.append(tipo_acidente.strip())
                existe_na_lista = False
            else:
                existe_na_lista = False
                for item in lista:
                    if tipo_acidente.strip() == item.strip():
                        existe_na_lista = True
                        break

                if existe_na_lista == False:
                    lista.append(tipo_acidente.strip())    

def gravar_trechos(lista):
    i = 1
    inserts = []
    path_arq_insert = 'c:/temp/insert_trecho.sql'

    if os.path.exists(path_arq_insert):
        os.remove(path_arq_insert)
    
    for trecho in lista:
        sql = f"INSERT INTO trecho VALUES({i},'{trecho}')\n"
        inserts.append(sql)
        i=i+1

    # grava todo o conteudo
    with open(path_arq_insert, 'w') as f:
        f.writelines(inserts )

def identificar_tipos_de_acidentes():
    path_demo_original = 'C:/mvp/puc-rio-mvp-sprint-04-sistemas-inteligentes/documentos/acidentes-rodovias/demonstrativo_originais'
    nome_lista_concessionarias = 'Lista_concessionarias.csv'
     
    pth_lista_concessionario_completa = f'{path_demo_original}/{nome_lista_concessionarias.strip()}'

    tipos_acidentes = []
     
    with open(pth_lista_concessionario_completa, "r") as arquivo:
        lista_concessionarias = arquivo.readlines() 
    
   
    icon = 1 
    icont_linhas = 1     
    lista_trechos = []
    for linha in lista_concessionarias:    
        dados = linha.split(',')
        nome_concessionaria = dados[2].removesuffix('\n')
        path_arquivo = f'{path_demo_original}/{nome_concessionaria}'

        with open(path_arquivo, "r") as arquivo:
            dados_originais = arquivo.readlines()
        

        icont_linhas = 1
        total_linhas = len(dados_originais)

        # trecho
        #montar_lista_trecho(lista_trechos, dados_originais)

        # tipo
        montar_lista_tipo_acidentes(tipos_acidentes,dados_originais)

        print(f'{icon} - {icont_linhas} - {total_linhas}')       
        icont_linhas = icont_linhas + 1        

        icon = icon + 1      
    if (len(tipos_acidentes)>0):
        gravar_tipos(tipos_acidentes)
    
    if (len(lista_trechos)>0):
        gravar_trechos(lista_trechos)

def recuperar_codigo_tipo_acidente(lista_tipos, descricao):
    codigo = 0
    for x in lista_tipos:
        if x.descricao.strip() == descricao.strip():
            codigo = x.id
            return codigo

    return codigo

def montar_sql_tabela_acidentes(lista, dados_encontrados, codigo_concessionaria):
    lista_trechos = montar_lista_trechos()
    lista_tipos_acidentes = montar_lista_tipo_acidentes()
     
    for registro in dados_encontrados:
        dado_tabela_sql = registro.split(';')        
        
         
        if dado_tabela_sql[0] != "data" and dado_tabela_sql[0].strip() != "":            
            #if (datetime.strptime(dado_tabela_sql[0], '%d/%m/%Y').date() >= datetime.strptime('01/01/2018', '%d/%m/%Y').date()):
                
            # coletando dados            
            dia = dado_tabela_sql[0][0:2]           
            mes = dado_tabela_sql[0][3:5]            
            descricao_acidente = dado_tabela_sql[7]
            id_incidente_tip = recuperar_codigo_tipo_acidente(lista_tipos_acidentes, descricao_acidente)
            qtd_caminhao = dado_tabela_sql[8]


            id_risco = dado_tabela_sql[14]

            sql = f"{codigo_concessionaria},{id_incidente_tip},  {dia},{mes},{qtd_caminhao},{id_risco}"
            
            lista.append(sql)            

    return lista

def montar_lista_trechos():
    lista = []
    lista.append(Trecho(1,"BR-393/RJ"))
    lista.append(Trecho(2,"Alça Sul"))
    lista.append(Trecho(3,"Alça Sul (Estrada União Indústria)/RJ"))
    lista.append(Trecho(4,"BR-381/SP"))
    lista.append(Trecho(5,"BR-381/MG"))
    lista.append(Trecho(6,"BR-381/MG-CONT"))
    lista.append(Trecho(7,"Contorno/MG"))
    lista.append(Trecho(8,"BR-101/RJ"))
    lista.append(Trecho(9,"BR-101/SC"))
    lista.append(Trecho(10,"BR-116/PR"))
    lista.append(Trecho(11,"BR-376/PR"))
    lista.append(Trecho(12,"BR-116/SC"))
    lista.append(Trecho(13,"BR-376/SC"))
    lista.append(Trecho(14,"BR-116/CW"))
    lista.append(Trecho(15,"BR-116/SP"))
    lista.append(Trecho(16,"CW-116/SP"))
    lista.append(Trecho(17,"BR-324/BA"))
    lista.append(Trecho(18,"BR-116/BA - ContSuFS"))
    lista.append(Trecho(19,"BR-116/BA"))
    lista.append(Trecho(20,"BR-116/BA - Cont VC"))
    lista.append(Trecho(21,"BA-528"))
    lista.append(Trecho(22,"BA-526"))
    lista.append(Trecho(23,"CONTORNO - VC/BA"))
    lista.append(Trecho(24,"526/BA"))
    lista.append(Trecho(25,"CONTORNO SUL  - FS/BA"))
    lista.append(Trecho(26,"CONTORNO NORTE - FS - 116/BA"))
    lista.append(Trecho(27,"528/BA"))
    lista.append(Trecho(28,"BR-060/DF"))
    lista.append(Trecho(29,"BR-153/GO"))
    lista.append(Trecho(30,"BR-153/MG"))
    lista.append(Trecho(31,"BR-060/GO"))
    lista.append(Trecho(32,"BR-262/MG"))
    lista.append(Trecho(33,"BR-262/GO"))
    lista.append(Trecho(34,"BR-60/GO"))
    lista.append(Trecho(35,"BR-040/RJ"))
    lista.append(Trecho(36,"BR-040/MG"))
    lista.append(Trecho(37,"BR-163/MT"))
    lista.append(Trecho(38,"BR-364/MT"))
    lista.append(Trecho(39,"BR-070/MT"))
    lista.append(Trecho(40,"BR-70/MT"))
    lista.append(Trecho(41,"BR-116/RJ"))
    lista.append(Trecho(42,"BR-101/ES"))
    lista.append(Trecho(43,"BR-101/BA"))
    lista.append(Trecho(44,"BR-101/ES (Contorno de Vitória)"))
    lista.append(Trecho(45,"BR-101/ES (Contorno de Iconha)"))
    lista.append(Trecho(46,"BR-101/ES (Contorno Iconha)"))
    lista.append(Trecho(47,"Contorno de Iconha/ES"))
    lista.append(Trecho(48,"BR-050/MG"))
    lista.append(Trecho(49,"BR-050/GO"))
    lista.append(Trecho(50,"Contorno"))
    lista.append(Trecho(51,"CONTORNO"))
    lista.append(Trecho(52,"BR-50/MG"))
    lista.append(Trecho(53,"Contorno de Uberlândia/MG"))
    lista.append(Trecho(54,"Acessos Niterói"))
    lista.append(Trecho(55,"Subida do Vão Central"))
    lista.append(Trecho(56,"Mocangue"))
    lista.append(Trecho(57,"Cajú"))
    lista.append(Trecho(58,"Descida do Vão Central"))
    lista.append(Trecho(59,"Emergência I"))
    lista.append(Trecho(60,"Curvão"))
    lista.append(Trecho(61,"Retão"))
    lista.append(Trecho(62,"Vão Central"))
    lista.append(Trecho(63,"Praça de Pedágio"))
    lista.append(Trecho(64,"Emergência II"))
    lista.append(Trecho(65,"PT"))
    lista.append(Trecho(66,"N03"))
    lista.append(Trecho(67,"N10"))
    lista.append(Trecho(68,"R1"))
    lista.append(Trecho(69,"N01"))
    lista.append(Trecho(70,"R2A"))
    lista.append(Trecho(71,"R3"))
    lista.append(Trecho(72,"N11"))
    lista.append(Trecho(73,"N09"))
    lista.append(Trecho(74,"N12"))
    lista.append(Trecho(75,"N08"))
    lista.append(Trecho(76,"N13"))
    lista.append(Trecho(77,"N14"))
    lista.append(Trecho(78,"MERGULHÃO"))
    lista.append(Trecho(79,"R4"))
    lista.append(Trecho(80,"Acesso N 08/RJ"))
    lista.append(Trecho(81,"Acesso R 2/RJ"))
    lista.append(Trecho(82,"Acesso N 13/RJ"))
    lista.append(Trecho(83,"Acesso R 1/RJ"))
    lista.append(Trecho(84,"Acesso N 09/RJ"))
    lista.append(Trecho(85,"Acesso N 07/RJ"))
    lista.append(Trecho(86,"Acesso N 12/RJ"))
    lista.append(Trecho(87,"Acesso N 02/RJ"))
    lista.append(Trecho(88,"Acesso R 2 A/RJ"))
    lista.append(Trecho(89,"Acesso N 06/RJ"))
    lista.append(Trecho(90,"Acesso N 03/RJ"))
    lista.append(Trecho(91,"Acesso N 19/RJ"))
    lista.append(Trecho(92,"Acesso N 05/RJ"))
    lista.append(Trecho(93,"Acesso N 10/RJ"))
    lista.append(Trecho(94,"Acesso N 04/RJ"))
    lista.append(Trecho(95,"Acesso N 17/RJ"))
    lista.append(Trecho(96,"Acesso N 11/RJ"))
    lista.append(Trecho(97,"Acesso N 14/RJ"))
    lista.append(Trecho(98,"Acesso N 18/RJ"))
    lista.append(Trecho(99,"Acesso N 01/RJ"))
    lista.append(Trecho(100,"Acesso R 4/RJ"))
    lista.append(Trecho(101,"Acesso N 11 A/RJ"))
    lista.append(Trecho(102,"BR-116/RS"))
    lista.append(Trecho(103,"BR-392/RS"))
    lista.append(Trecho(104,"BR-604/RS"))
    lista.append(Trecho(105,"BR-293/RS"))
    lista.append(Trecho(106,"BR-364/GO"))
    lista.append(Trecho(107,"BR-365/MG"))
    lista.append(Trecho(108,"BR-364/MG"))
    lista.append(Trecho(109,"BR-101/SP"))
    lista.append(Trecho(110,"BR-163/MS"))
    lista.append(Trecho(111,"BR-153/SP"))
    lista.append(Trecho(112,"BR-040/GO"))
    lista.append(Trecho(113,"BR-040/DF"))
    lista.append(Trecho(114,"Fora_Rota"))
    lista.append(Trecho(115,"BR-40/MG"))
    lista.append(Trecho(116,"BR-101/RS"))
    lista.append(Trecho(117,"BR-386/RS"))
    lista.append(Trecho(118,"BR-290/RS"))
    lista.append(Trecho(119,"BR-448/RS"))
    return lista

def montar_lista_tipo_acidentes():
    lista = []
    lista.append(TipoAcidente(2, "Derrapagem"))
    lista.append(TipoAcidente(3, "Abalroamento transversal"))
    lista.append(TipoAcidente(4, "Colisão traseira"))
    lista.append(TipoAcidente(5, "Abalroamento longitudinal"))
    lista.append(TipoAcidente(6, "Capotamento"))
    lista.append(TipoAcidente(7, "Colisão frontal"))
    lista.append(TipoAcidente(8, "Queda de moto"))
    lista.append(TipoAcidente(9, "Atropelamento de pedestre atravessando"))
    lista.append(TipoAcidente(10, "Atropelamento de animal"))
    lista.append(TipoAcidente(11, "Engavetamento"))
    lista.append(TipoAcidente(12, "Choque em objeto fixo"))
    lista.append(TipoAcidente(13, "Colisão Traseira"))
    lista.append(TipoAcidente(14, "Colisão com Objeto Fixo"))
    lista.append(TipoAcidente(15, "Abalr.Transversal"))
    lista.append(TipoAcidente(16, "Abalr.Mesmo Sentido"))
    lista.append(TipoAcidente(17, "Outros tipos de acidente"))
    lista.append(TipoAcidente(18, "Tombamento"))
    lista.append(TipoAcidente(19, "Colisão Frontal"))
    lista.append(TipoAcidente(20, "Atropelamento"))
    lista.append(TipoAcidente(21, "Atropelamento de Animal"))
    lista.append(TipoAcidente(22, "Saída de Pista"))
    lista.append(TipoAcidente(23, "Abalr.Sentido Oposto"))
    lista.append(TipoAcidente(24, "Colisão Lateral"))    
    lista.append(TipoAcidente(25, 'Choque - Defensa, barreira ou "submarino"'))
    lista.append(TipoAcidente(26, "Queda de Bicicleta"))
    lista.append(TipoAcidente(27, "Queda de Moto"))
    lista.append(TipoAcidente(28, "Outros - Sequência"))
    lista.append(TipoAcidente(29, "Saida de Pista"))
    lista.append(TipoAcidente(30, "Colisão Transversal"))
    lista.append(TipoAcidente(31, "Atropelamento - Morador"))
    lista.append(TipoAcidente(32, "Choque - Poste"))
    lista.append(TipoAcidente(33, "Outros"))
    lista.append(TipoAcidente(34, "Choque - Arvore"))
    lista.append(TipoAcidente(35, "Choque - Outros"))
    lista.append(TipoAcidente(36, "Choque - Elemento de Drenagem"))
    lista.append(TipoAcidente(37, "Atropelamento - Ciclista"))
    lista.append(TipoAcidente(38, "Choque - Suporte de Sinalização"))
    lista.append(TipoAcidente(39, "Abalroamento Mesmo Sentido"))
    lista.append(TipoAcidente(40, "Atropelamento - Andarilho"))
    lista.append(TipoAcidente(41, "Choque - Talude"))
    lista.append(TipoAcidente(42, "Abalroamento Sentido Oposto"))
    lista.append(TipoAcidente(43, "Atropelamento - Outros"))
    lista.append(TipoAcidente(44, "Atropelamento - Usuário"))
    lista.append(TipoAcidente(45, "Choque - Objeto sobre a pista"))
    lista.append(TipoAcidente(46, "Atropelamento - Funcionário"))
    lista.append(TipoAcidente(47, "Objeto lançado contra veículo"))
    lista.append(TipoAcidente(48, "Choque - Veiculo parado na pista"))
    lista.append(TipoAcidente(49, "Choque - Veiculo parado no acostamento"))
    lista.append(TipoAcidente(50, "Atropelamento - Sem Informação"))
    lista.append(TipoAcidente(51, "Atropelamento - Ambulante"))
    lista.append(TipoAcidente(52, ""))
    lista.append(TipoAcidente(53, "Acidentes de outra natureza"))
    lista.append(TipoAcidente(54, "Colisão com veículos (traseira)"))
    lista.append(TipoAcidente(55, "Colisão lateral no mesmo sentido"))
    lista.append(TipoAcidente(56, "Colisão c/ obstáculos"))
    lista.append(TipoAcidente(57, "Saídas de pista"))
    lista.append(TipoAcidente(58, "Colisão lateral no sentido contrário"))
    lista.append(TipoAcidente(59, "Colisão com veículos (frontal)"))
    lista.append(TipoAcidente(60, "Atropelamento de pedestre"))
    lista.append(TipoAcidente(61, "Atropelamento de animais"))
    lista.append(TipoAcidente(62, "Colisão Lateral Mesmo Sentido"))
    lista.append(TipoAcidente(63, "Atropelamento - Animal"))
    lista.append(TipoAcidente(64, "Atropelamento - Pedestre"))
    lista.append(TipoAcidente(65, "Acidente - Outra Natureza"))
    lista.append(TipoAcidente(66, "Abalroamento - Sentido Oposto"))
    lista.append(TipoAcidente(67, "Colisão Lateral Sentido Oposto"))
    lista.append(TipoAcidente(68, "Abalroamento - Mesmo Sentido"))
    lista.append(TipoAcidente(69, "Atropelamento - Pedestre Usuário"))
    lista.append(TipoAcidente(70, "Atropelamento - PedestreFuncionário"))
    lista.append(TipoAcidente(71, "Atropelamento - Pedestre Andarilho"))
    lista.append(TipoAcidente(72, "Derramamento de Carga"))
    lista.append(TipoAcidente(73, "Norte"))
    lista.append(TipoAcidente(74, "Sul"))
    lista.append(TipoAcidente(75, "Choque"))
    lista.append(TipoAcidente(76, "Saída de pista"))
    lista.append(TipoAcidente(77, "Colisão transversal"))
    lista.append(TipoAcidente(78, "Colisão lateral em sentido contrário"))
    lista.append(TipoAcidente(79, "Atropelamento de ciclista"))
    lista.append(TipoAcidente(80, "Choque - Cancela de Pedagio"))
    lista.append(TipoAcidente(81, "Choque - Objeto não identificado"))
    lista.append(TipoAcidente(82, "Soterramento"))
    lista.append(TipoAcidente(83, "Incêndio"))
    lista.append(TipoAcidente(84, "Submersão"))
    lista.append(TipoAcidente(85, "Explosão"))
    lista.append(TipoAcidente(86, "Transposição de Pista"))
    lista.append(TipoAcidente(87, "Queda"))
    lista.append(TipoAcidente(88, "Não Def"))
    lista.append(TipoAcidente(89, "Não Def."))
    lista.append(TipoAcidente(90, "Travessia Canteiro Central"))
    lista.append(TipoAcidente(91, "Problema Mecanico / Eletrico"))
    lista.append(TipoAcidente(92, "Choque - Defensa, barreira ousubmarino"))
    lista.append(TipoAcidente(93, "Choque Contra Objeto Fixo"))
    lista.append(TipoAcidente(94, "Atropelamento de Pedestre"))
    lista.append(TipoAcidente(95, "Sequência"))
    lista.append(TipoAcidente(96, "Carreta deu L"))
    lista.append(TipoAcidente(97, "Queda de Ciclista"))
    lista.append(TipoAcidente(98, "Outros - seguências"))
    lista.append(TipoAcidente(99, "Outros - sequências"))
    lista.append(TipoAcidente(100, "Choque - Poste/"))
    lista.append(TipoAcidente(101, "Choque- Placa/Suporte Sinalização"))
    lista.append(TipoAcidente(102, "Choque- Poste/Equipamento"))
    lista.append(TipoAcidente(103, "Choque - Barreira"))
    lista.append(TipoAcidente(104, "Choque - Defensa"))
    lista.append(TipoAcidente(105, "Atropelamento - Morador/Trabalhador"))
    lista.append(TipoAcidente(106, "Queda em Ribanceira"))
    lista.append(TipoAcidente(107, "Choque - Submarino"))
    lista.append(TipoAcidente(108, "Queda de Ponte/Viaduto"))
    lista.append(TipoAcidente(109, "Choque - Cabine de Pedágio"))
    lista.append(TipoAcidente(110, "Atropelamento - Esportista/Romeiro"))
    lista.append(TipoAcidente(111, "Queda de bicicleta"))
    lista.append(TipoAcidente(112, "Choque - Objeto Fixo"))
    lista.append(TipoAcidente(113, "Choque em objeto na pista"))
    lista.append(TipoAcidente(114, "choque - Objeto Fixo"))
    lista.append(TipoAcidente(115, "Colisão veiculo parado acostamento"))
    lista.append(TipoAcidente(116, "Choque com objeto na pista"))
    lista.append(TipoAcidente(117, "Abalroamento - Longitudinal"))
    lista.append(TipoAcidente(118, "Abalroamento - Transversal"))
    lista.append(TipoAcidente(119, "Queda de Carga"))
    lista.append(TipoAcidente(120, "Atropelamento - Pedestre atravessando"))
    lista.append(TipoAcidente(121, "Choque-outros"))
    lista.append(TipoAcidente(122, "Atropel. de pedestre atravessando"))
    lista.append(TipoAcidente(123, "Atropel. de pedestre caminhando"))
    lista.append(TipoAcidente(124, "Choque em defensa"))
    lista.append(TipoAcidente(125, "Queda de carga"))
    lista.append(TipoAcidente(126, "Choque em barreira New Jersey"))
    lista.append(TipoAcidente(127, "Choque em veículo parado na pista"))
    lista.append(TipoAcidente(128, "derrapagem"))
    lista.append(TipoAcidente(129, "Atropelamento em abrigo de ônibus"))
    lista.append(TipoAcidente(130, "choque em objeto fixo"))
    lista.append(TipoAcidente(131, "Abalroamento Longitudinal"))
    lista.append(TipoAcidente(132, "colisão Frontal"))
    lista.append(TipoAcidente(133, "Choque em Objeto Fixo"))
    lista.append(TipoAcidente(134, "colisão frontal"))
    lista.append(TipoAcidente(135, "Choque em Objeto fixo"))
    lista.append(TipoAcidente(136, "Imprudência"))
    lista.append(TipoAcidente(137, "colisão traseira"))
    lista.append(TipoAcidente(138, "capotamento"))
    lista.append(TipoAcidente(139, "Abalroamento Transversal"))
    lista.append(TipoAcidente(140, "Atropelamento - Pessoa"))
    lista.append(TipoAcidente(141, "Atropelamento de Cachorro"))
    lista.append(TipoAcidente(142, "Queda de vegetação c/ veículo"))
    lista.append(TipoAcidente(143, "Atropelamento - Cachorro"))
    lista.append(TipoAcidente(144, "Colisão"))
    lista.append(TipoAcidente(145, "Atropelamento Animal"))
    lista.append(TipoAcidente(146, "Queda de ciclista"))
    lista.append(TipoAcidente(147, "Choque com Objeto Fixo"))
    lista.append(TipoAcidente(148, "Veículo em Chamas"))
    lista.append(TipoAcidente(149, "Choque com Veículo Estacionado"))
    lista.append(TipoAcidente(150, "Atropelamento de Equino"))
    lista.append(TipoAcidente(151, "Atropelamento e Fuga"))
    lista.append(TipoAcidente(152, "Atropelamento de Bovino"))
    lista.append(TipoAcidente(153, "Danos Eventuais"))
    lista.append(TipoAcidente(154, "Colisão com ciclista"))
    lista.append(TipoAcidente(155, "Atropelamento - Bovino"))
    lista.append(TipoAcidente(156, "Atropelamento - Equino"))
    lista.append(TipoAcidente(157, "Atropelamento - Bubalino"))
    lista.append(TipoAcidente(158, "Choque na cancela"))
    lista.append(TipoAcidente(159, "Desatrelamento"))
    lista.append(TipoAcidente(160, "Choque - Barranco"))
    lista.append(TipoAcidente(161, "Choque - Defensa, barreira ou meio fio"))
    lista.append(TipoAcidente(162, "Choque - Obstáculo Fixo"))
    lista.append(TipoAcidente(163, "Choque - Sinalização"))
    lista.append(TipoAcidente(164, "Choque - New jersey"))
    lista.append(TipoAcidente(165, "Choque - Meio fio"))
    lista.append(TipoAcidente(166, "Choque - Defensa metálica"))
    lista.append(TipoAcidente(167, "Queda de barreira, ribanceira, ponte ou viaduto"))
    lista.append(TipoAcidente(168, "Choque na praça ? submarino"))
    lista.append(TipoAcidente(169, "Queda de veículo em ribanceira, ponte ou viaduto"))
    lista.append(TipoAcidente(170, "Choque - Talude ou Barranco"))
    lista.append(TipoAcidente(171, "Queda de Carro"))
    lista.append(TipoAcidente(172, "Colisão - Traseira"))
    lista.append(TipoAcidente(173, "Choque com objeto sobre a pista"))
    lista.append(TipoAcidente(174, "Colisão - Lateral"))
    lista.append(TipoAcidente(175, "Choque Defensa"))
    lista.append(TipoAcidente(176, "Choque Praça - Cabine"))
    lista.append(TipoAcidente(177, "Colisão - Transversal"))
    lista.append(TipoAcidente(178, "Colisão - Frontal"))
    lista.append(TipoAcidente(179, "Choque com veículo na faixa de"))
    lista.append(TipoAcidente(180, "Choque Barreira"))
    lista.append(TipoAcidente(181, "Choque - Meio Fio"))
    lista.append(TipoAcidente(182, "Choque com objeto sobre a pist"))
    lista.append(TipoAcidente(183, "Choque - Pilar"))
    lista.append(TipoAcidente(184, "Choque - Canaleta"))
    lista.append(TipoAcidente(185, "Choque Praça"))
    lista.append(TipoAcidente(186, "Choque Talude"))
    lista.append(TipoAcidente(187, "Choque veículo parado na pista"))
    lista.append(TipoAcidente(188, "Atropelamento Ciclista"))
    lista.append(TipoAcidente(189, "Queda de Ponte / Viaduto"))
    lista.append(TipoAcidente(190, "Choque - Veículo parado na pista"))
    lista.append(TipoAcidente(191, "Abalr. Transversal"))
    lista.append(TipoAcidente(192, "Abalr. Mesmo Sentido"))
    lista.append(TipoAcidente(193, "Abalr. Sentido Oposto"))
    lista.append(TipoAcidente(194, "Colisão com Veículo Estac."))
    lista.append(TipoAcidente(195, "Atropelamento sem morte"))
    lista.append(TipoAcidente(196, "Outros(especificar)"))
    lista.append(TipoAcidente(197, "Atropelamento com morte"))
    lista.append(TipoAcidente(198, "Colisão com objeto Fixo"))
    lista.append(TipoAcidente(199, "Outros Tipos de Acidente"))
    lista.append(TipoAcidente(200, "Colisão com Objeto fixo"))
    lista.append(TipoAcidente(201, "Abal. Sentido Oposto"))
    lista.append(TipoAcidente(202, "Colisão com objeto fixo"))
    lista.append(TipoAcidente(203, "Abalroamento no Mesmo Sentido"))
    lista.append(TipoAcidente(204, "Abalr. Sentido Oposto."))
    lista.append(TipoAcidente(205, "Outros Tipos"))
    lista.append(TipoAcidente(206, "Saída dePista"))
    lista.append(TipoAcidente(207, "Abalroamento transversal."))
    lista.append(TipoAcidente(208, "Outros Tipos de acidente"))
    lista.append(TipoAcidente(209, "Abalrroamento Transversal."))
    lista.append(TipoAcidente(210, "Colisão objeto fixo"))
    lista.append(TipoAcidente(211, "Saida de pista"))
    lista.append(TipoAcidente(212, "Abalr.mesmo sentido"))
    lista.append(TipoAcidente(213, "Abalroamento mesmo sentido"))
    lista.append(TipoAcidente(214, "Abalroamento em Sent.Oposto"))
    lista.append(TipoAcidente(215, "Abalroamento no mesmo Sentido"))
    lista.append(TipoAcidente(216, "Abalroamento sentido Oposto"))
    lista.append(TipoAcidente(217, "Abalroamento em sentido oposto"))
    lista.append(TipoAcidente(218, "Abalroamento no mesmo sentido"))
    lista.append(TipoAcidente(219, "Abalroamanento Traversasl"))
    lista.append(TipoAcidente(220, "Abalroamentono mesmo sentido"))
    lista.append(TipoAcidente(221, "Colisão com veículo estacionado"))
    lista.append(TipoAcidente(222, "atropelamento"))
    lista.append(TipoAcidente(223, "Abalroamento Trarnversal"))
    lista.append(TipoAcidente(224, "Outros tipos de Acidente"))
    lista.append(TipoAcidente(225, "abalr.mesmo Sentido"))
    lista.append(TipoAcidente(226, "Abalroamento em mesmo sentido"))
    lista.append(TipoAcidente(227, "Abalromanemto mesmo sentido"))
    lista.append(TipoAcidente(228, "Abalroamente Transversal"))
    lista.append(TipoAcidente(229, "Abalr.Sent.Oposto"))
    lista.append(TipoAcidente(230, "Abalr.em mesmo sentido"))
    lista.append(TipoAcidente(231, "Abalr.Mesmo sentido"))
    lista.append(TipoAcidente(232, "Ablr.Sentido Oposto"))
    lista.append(TipoAcidente(233, "Colisão Ojeto Fixo"))
    lista.append(TipoAcidente(234, "Abal.mesmo sentido"))
    lista.append(TipoAcidente(235, "Abalr. Mesmo sentido"))
    lista.append(TipoAcidente(236, "Colisão Objeto Fixo"))
    lista.append(TipoAcidente(237, "Abal.mesmo.sentido"))
    lista.append(TipoAcidente(238, "Abal.sentido. Oposto"))
    lista.append(TipoAcidente(239, "Abal.Transversal"))
    lista.append(TipoAcidente(240, "Abal.sent.oposto"))
    lista.append(TipoAcidente(241, "Abalr.sentido oposto"))
    lista.append(TipoAcidente(242, "Abalr. Sentido oposto"))
    lista.append(TipoAcidente(243, "abalr. Transversal"))
    lista.append(TipoAcidente(244, "Tombamento de moto"))
    lista.append(TipoAcidente(245, "Colisão Traseira - veículos"))
    lista.append(TipoAcidente(246, "Colisão com Obstáculos"))
    lista.append(TipoAcidente(247, "Colisão Lateral - sentido contrário"))
    lista.append(TipoAcidente(248, "Colisão Lateral - mesmo sentido"))
    lista.append(TipoAcidente(249, "Colisão Frontal - veículos"))
    lista.append(TipoAcidente(250, "Tombamento de Moto"))
    lista.append(TipoAcidente(251, "Atropelamento de pedestre caminhando"))
    lista.append(TipoAcidente(252, "Queda de ribanceira"))
    lista.append(TipoAcidente(253, "Choque em Barreira New Jersey"))
    lista.append(TipoAcidente(254, "Choque em Defensa"))
    lista.append(TipoAcidente(255, "Atropelamento de Pedestre Atravessando"))
    lista.append(TipoAcidente(256, "Atropelamento de Pedestre Caminhando"))
    lista.append(TipoAcidente(257, "Queda de ponte/viaduto"))
    lista.append(TipoAcidente(258, "Atropelamento - Pedestre caminhando"))
    lista.append(TipoAcidente(259, "Choque contra Objeto Fixo"))
    lista.append(TipoAcidente(260, "Atropelamentode Pedestre"))
    lista.append(TipoAcidente(261, "Atropelamento de Ciclista"))
    lista.append(TipoAcidente(262, "Choque na Praça - Cabine"))
    lista.append(TipoAcidente(263, "Choque contra objeto na faixa de rolamento"))
    lista.append(TipoAcidente(264, "Choque na Praça - Submarino"))
    lista.append(TipoAcidente(265, "INCIDENTE - Choque na Praça - Cancela"))
    lista.append(TipoAcidente(266, "Queda de carga sobre a pista"))
    lista.append(TipoAcidente(267, "Incidente"))
    lista.append(TipoAcidente(268, "Colisão na Praça - Cancela"))
    lista.append(TipoAcidente(269, "INCIDENTE - Colisão na Praça - Cancela"))
    lista.append(TipoAcidente(270, "Colisão na Praça - Submarino"))
    lista.append(TipoAcidente(271, "Choque contra veículo no acostamento"))
    lista.append(TipoAcidente(272, "Não Localizado / Evadiu-se"))
    lista.append(TipoAcidente(273, "Choque com objeto fixo"))
    lista.append(TipoAcidente(274, "Atropelamento - Abrigo de ônibus"))
    lista.append(TipoAcidente(275, "Colisão lateral"))
    lista.append(TipoAcidente(276, "Choque c/ Objeto Fixo"))
    lista.append(TipoAcidente(277, "Queda Veículo"))
    lista.append(TipoAcidente(278, "Queda de Ribanceira"))
    lista.append(TipoAcidente(279, 'Choque / defensa, barreira ou "submarino"'))
    lista.append(TipoAcidente(280, "Choque / árvore"))
    lista.append(TipoAcidente(281, "Atropelamento de Andarilho"))
    lista.append(TipoAcidente(282, "Choque com objeto"))
    lista.append(TipoAcidente(283, "Queda de Viaduto"))
    lista.append(TipoAcidente(284, "Choque / objeto não identificado"))
    lista.append(TipoAcidente(285, "Choque c/ Veículo Parado"))
    lista.append(TipoAcidente(286, "Colisão com veículo da concessionária"))
    lista.append(TipoAcidente(287, "Choque com veículo da concessionária estacionado"))
    lista.append(TipoAcidente(288, "Choque com veículo na faixa de rolamento"))
    lista.append(TipoAcidente(289, "Atropelamento - Morador/Trabalhador/Estudante"))
    lista.append(TipoAcidente(290, "Choque Praça - Submarino"))
    lista.append(TipoAcidente(291, "Atropelamento - Suicida"))
    lista.append(TipoAcidente(292, "Choque - Caixa de Captação/Fibra"))
    lista.append(TipoAcidente(293, "Choque com veículo no acostamento"))
    lista.append(TipoAcidente(294, "Atropelamento - Esportista"))
    lista.append(TipoAcidente(295, "Teste Wanderson"))
    lista.append(TipoAcidente(296, "Choque - Painel Propaganda"))
    return lista

def recuperar_codigo_trecho (lista_trechos, descricao):
    codigo = 0
    for x in lista_trechos:
        if x.descricao == descricao:
            codigo = x.id
            return codigo

    return codigo

def gravar_sql_tabela_acidentes(lista, nome_arquivo):
    nome_arquivo_gravar = nome_arquivo.removesuffix('.csv')
    id_novo = 1
    inserts = []
    path_arq_insert = f'c:/temp/insert_acidentes_{nome_arquivo_gravar}.sql'

    if os.path.exists(path_arq_insert):
        os.remove(path_arq_insert)
    
    for valores in lista:
        sql = f'INSERT INTO acidente_ocorrencia VALUES({id_novo},{valores});\n'
        inserts.append(sql)
        id_novo = id_novo + 1

    # grava todo o conteudo
    with open(path_arq_insert, 'w') as f:
        f.writelines(inserts )

def gerar_insert_para_bd():
    path_demo_novo_layout = 'C:/mvp/puc-rio-mvp-sprint-04-sistemas-inteligentes/documentos/acidentes-rodovias/novo_layout'
    nome_lista_concessionarias = 'Lista_concessionarias.csv'
    pth_lista_concessionario_completa = f'{path_demo_novo_layout}/{nome_lista_concessionarias.strip()}'
   
    lista_sql = []
     
    with open(pth_lista_concessionario_completa, "r") as arquivo:
        lista_concessionarias = arquivo.readlines() 
    ''' Apagar a base '''            
    apagar_registro_ocorrencias()
    icont = 1 
    

    for linha in lista_concessionarias: 
        lista_sql = []   
        dados = linha.split(',')
        nome_concessionaria = dados[2].removesuffix('\n')        
        path_arquivo = f'{path_demo_novo_layout}/{nome_concessionaria}'

        with open(path_arquivo, "r") as arquivo:
            acidentes = arquivo.readlines()
        
        montar_sql_tabela_acidentes(lista_sql,acidentes, icont)                

        if len(lista_sql)>0:
            # gravar_sql_tabela_acidentes(lista_sql, nome_concessionaria )
            gravar_na_base(lista_sql)


        print(f'{icont} - 22 - {nome_concessionaria}')

        icont = icont + 1

def gravar_na_base(lista):
    con = sqlite3.connect(r"C:\mvp\puc-rio-mvp-sprint-04-sistemas-inteligentes\documentos\acidentes-rodovias\database\db.sqlite3")    
    id_novo = 0
    for valores in lista:
        id_novo = id_novo + 1
        x = valores
        x = x.removesuffix('\n')
        sql = f'INSERT INTO acidente_ocorrencia VALUES({id_novo},{x})'        
        con.execute(sql)
        con.commit()
        

    con.close()

def apagar_registro_ocorrencias():
    con = sqlite3.connect(r"C:\mvp\puc-rio-mvp-sprint-04-sistemas-inteligentes\documentos\acidentes-rodovias\database\db.sqlite3")           
    sql = f'DELETE FROM acidente_ocorrencia'
    con.execute(sql)
    con.commit()
    con.close()

def extrair_ocorrencias():
    con = sqlite3.connect(r"C:\mvp\puc-rio-mvp-sprint-04-sistemas-inteligentes\documentos\acidentes-rodovias\database\db.sqlite3")    
    cur = con.cursor()
    
    ii = 1

    for i in range(22):

        dados = cur.execute(f"SELECT a.id_acidente_tip, a.dia, a.mes,   a.id_risco ,co.Sigla FROM acidente_ocorrencia a INNER JOIN concessionaria co on (co.id = a.id_conce) WHERE a.id_conce = {ii}")

        linhas = []

        strGravar = 'id_acidente_tip; dia; mes; total; id_risco\n'
        linhas.append(strGravar)        

        for linha in dados:
            path_arq_insert = f"{ii}_{linha[4]}.csv"
        
            strGravar = f'{linha[0]};{linha[1]};{linha[2]};{linha[3]};{linha[4]}'   
            linhas.append(f'{strGravar}\n')

        # exclui antes de gravar     
        if os.path.exists(path_arq_insert):
            os.remove(path_arq_insert)

        if len(linhas)>0:
            # grava todo o conteudo
            with open(path_arq_insert, 'w') as f:
                f.writelines(linhas)

        ii = ii + 1
    con.close()
    print('Gravado com sucesso!')

def extrair_ocorrencias_arq_unico():
    con = sqlite3.connect(r"C:\mvp\puc-rio-mvp-sprint-04-sistemas-inteligentes\documentos\acidentes-rodovias\database\db.sqlite3")    
    cur = con.cursor()
    
    dados = cur.execute(f"SELECT id_conce, id_acidente_tip, dia, mes, qt_caminhao, id_risco FROM acidente_ocorrencia order by id_conce,id_acidente_tip, dia, mes")

    path_arq_insert = "acidente_ocorrencia.csv"

    if os.path.exists(path_arq_insert):
        os.remove(path_arq_insert)

    linhas = []

    strGravar = 'id_conce; id_acidente_tip; dia; mes; total; id_risco\n'
    linhas.append(strGravar)        
    for linha in dados:
        strGravar = f'{linha[0]};{linha[1]};{linha[2]};{linha[3]};{linha[4]};{linha[5]}'   
        linhas.append(f'{strGravar}\n')
        
    if len(linhas)>0:
        # grava todo o conteudo
        with open(path_arq_insert, 'w') as f:
            f.writelines(linhas)

     
    con.close()
    print('Gravado com sucesso!')

def abrir_panda_csv():
    df = pd.read_csv('acidente_ocorrencia.csv', sep='\t')
    print(df)

#tratar_dados()
#print('preparar base')
#gerar_insert_para_bd()
#extrair_ocorrencias_arq_unico()
#abrir_panda_csv()
print('extrair base')
extrair_ocorrencias()
