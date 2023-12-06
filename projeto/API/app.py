from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Model,  ViagemPredicao, AcidentesRiscos, Risco
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
viagem_predicao_tag = Tag(name="Viagem_Predicao", description="Predição de riscos à acidentes para a viagem")
acidentes_riscos_tag = Tag(name="AcidenteRisco", description="visualização registros de acidentes e riscos")
risco_tag = Tag(name='Risco', description="Consulta de riscos")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')



# ***************************************************  Metodos de Viagem Predicao***************************************************

# Rota viagem predicao
@app.post('/predicao', tags=[viagem_predicao_tag],
          responses={"200": ViagemPredicaoViewSchema,                     
                     "500": ErrorSchema})
def add_predicao(form: ViagemPredicaoSchema):
    """ Retorna uma representação do resultado da predicao feita para a viagem
        Args:
            dia (int): dia da viagem informada
            mes (int): mes da viagem informada
            id_sentido (int): codigo do sentido da rodovia que será a viagem
            id_trecho (int): codigo do trecho a ser percorrido na viagem
            percentual_risco (float): valor fracionado do percentual que a predicao deve identificar a classificação de risco mais frequente na rodovia
    """    
    try: 
        # Carregando modelo
        ml_path = 'ml_model/18_nova_dutra.pkl'
        modelo = Model.carrega_modelo(ml_path)

        # cria objeto viagem predicao
        viagem_predicao = ViagemPredicao(
                                        dia = form.dia, 
                                        mes = form.mes, 
                                        id_sentido = form.id_sentido, 
                                        id_trecho = form.id_trecho,
                                        pc_risco =  form.percentual_risco,
                                        id_risco = Model.preditor(modelo, form) )
               
        
        return apresenta_resultado_predicao(viagem_predicao.id_risco), 200    

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível executar a predicao :/"
        logger.warning(f"Erro ao executar a predição - erro = {e}")
        return {"message": error_msg}, 500    

# ***************************************************  Metodos de Acidentes e riscos ***************************************
# Rota consulta de acidentes riscos
@app.get('/acidentes_riscos', tags=[acidentes_riscos_tag],
        responses={"200": ListaAcidentesRiscosSchema,
                  "404": ErrorSchema,
                  "500": ErrorSchema})
def get_acidentes_riscos(query:BuscaAcidentesRiscoSchema):
    """Consulta busca as informações de acidentes e riscos coligados com os parametros de busca

    """
    dia = query.dia
    mes = query.mes
    id_trecho = query.id_trecho
    id_sentido = query.id_sentido
    
    logger.debug(
        f"Consultando acidentes e risco por dia = {dia}, mês ={mes }, id_trecho = {id_trecho}, id_sentido = {id_sentido} ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        acidentes_riscos = session.query(AcidentesRiscos)\
                             .filter(AcidentesRiscos.dia == dia,
                                     AcidentesRiscos.mes== mes, 
                                     AcidentesRiscos.id_trecho == id_trecho,
                                     AcidentesRiscos.id_sentido == id_sentido)

        if not acidentes_riscos:
            # se não há cadastrado
            error_msg = "acidentes não encontrado na base :/"
            logger.warning(f"Erro ao buscar a operacao error, {error_msg}")
            return {"message": error_msg}, 404
        else:
            logger.debug(
                f"A acidentes e risco por dia = {dia}, mês ={mes }, id_trecho = {id_trecho}, id_sentido = {id_sentido} ")
            # retorna a representação de  s
            return apresenta_lista_acidentes_riscos(acidentes_riscos), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar os acidentes e riscos:/{str(e)}"
        logger.warning(
            f"Erro ao consultar os acidentes e riscos com erro {e}, {error_msg}")
        return {"message": error_msg}, 500


# ***************************************************  Metodos de Risco ***************************************************
# Rota consulta de Riscos
@app.get('/riscos',tags=[risco_tag],
        responses={"200": ListaRiscosSchema,
                    "404": ErrorSchema,
                    "500": ErrorSchema})          
def get_riscos():
    """Lista as informações de riscos

    """
     
    
    logger.debug(
        f"Consultando lista de risco ")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        riscos = session.query(Risco)                             

        if not riscos:
            # se não há cadastrado
            error_msg = "Riscos não encontrado na base :/"
            logger.warning(f"Erro ao buscar a operacao error, {error_msg}")
            return {"message": error_msg}, 404
        else:
            logger.debug(
                f"lista de riscos encontrados")
            # retorna a representação de  s
            return apresenta_lista_riscos(riscos), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar os riscos:/{str(e)}"
        logger.warning(
            f"Erro ao consultar os riscos com erro {e}, {error_msg}")
        return {"message": error_msg}, 500


