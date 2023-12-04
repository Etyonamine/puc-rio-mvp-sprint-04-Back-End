from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Paciente, Model, Viagem, ViagemPredicao, AcidentesRiscos
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Paciente", description="Adição, visualização, remoção e predição de pacientes com Diabetes")
viagem_predicao_tag = Tag(name="Viagem_Predicao", description="Predição de riscos à acidentes para a viagem")
acidentes_riscos_tag = Tag(name="AcidenteRisco", description="visualização registros de acidentes e riscos")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# ***************************************************  Metodos de Viagem ***************************************

# Rota novo registro na tabela viagem
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
@app.get('/acidentes_riscos', tags=[acidentes_riscos_tag],
        responses={"200": ListaAcidentesRiscosSchema,
                  "404": ErrorSchema,
                  "500": ErrorSchema})
def get_acidentes_riscos(query:BuscaAcidentesRiscoSchema):
    """Consulta busca as informações de acidentes e riscos coligados com os parametros de busca

    """

    


                




