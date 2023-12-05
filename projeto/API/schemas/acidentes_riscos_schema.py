from pydantic import BaseModel
from typing import Optional, List
from model.acidentes_risco import AcidentesRiscos

class AcidentesRiscosViewSchema (BaseModel):
    """ Define como deverá retornado

    """    
    id: int = 1
    trecho:str = 'BR-116/SP'
    sentido:str = 'Pista Sul'
    acidente:str = 'Tombamento'
    risco:str = 'Baixo'
    total:int = 10



class ListaAcidentesRiscosSchema(BaseModel):
    """ Define como retorna a lista de acidentes e riscos encontrados
    """
    AcidentesRiscos: List[AcidentesRiscosViewSchema]

class BuscaAcidentesRiscoSchema(BaseModel):
    """Define os parametros para a busca dos acidentes e riscos

    """
    dia: int = 1
    mes: int = 1
    id_trecho: int = 1
    id_sentido: int = 1
    


def apresenta_lista_acidentes_riscos(lista: List[AcidentesRiscos]):
    """ Retorna uma representação da lista de unidades federativas seguindo o schema definido em
        UfViewSchema.

    """
    result = []
    i = 1
    for item in lista:
       
        result.append({
            "id": str(i),
            "trecho": item.trecho,
            "sentido": item.id_sentido,
            "acidente": item.tipo_acidente,
            "risco": item.risco,
            "total": item.total
        })
        i = i + 1

    return {"lista": result}    