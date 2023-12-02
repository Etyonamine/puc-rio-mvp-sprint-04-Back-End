from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Paciente, Model, Uf
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
uf_tag = Tag(name="UF", description ="Visualização de informaçõe de estados federativos do Brasil")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de listagem de Unidades federativas do Brasil
@app.get('/uf',tags=[uf_tag],
        responses={"200": ListaUfSchema,
                   "404": ErrorSchema})
def get_uf():
    """Consulta as UF 

    Retorna uma listagem de unidades federativas
    """
    logger.debug(f"Consultando as unidades federativas do Brasil")
    try:
        # criando conexão com a base
        session = Session()
        # fazendo a busca
        lista = session.query(Uf).order_by(Uf.descricao.asc()).all()
         
        if not lista:            
            # se não há registros cadastrados
            return {"lista": []}, 200
        else:
            logger.debug(f"%d uf encontrados" %
                         len(lista))
            # retorna a representação de tipo_operacaos
            return apresenta_lista_uf(lista), 200
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível consultar as UF de listas :/{str(e)}"
        logger.warning(
            f"Erro ao consultar as unidades federativas, {error_msg}")
        return {"message": error_msg}, 500
