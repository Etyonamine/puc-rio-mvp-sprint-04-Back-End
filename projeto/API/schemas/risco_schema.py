from pydantic import BaseModel
from typing import Optional, List
from model.risco import Risco

class RiscoViewSchema(BaseModel):
    """Representa como devera ser retornado as informações do risco

    """
    id_risco:int = 1
    descricao:str = 'Baixo'
    percentual_taxa:float = 0.00

class ListaRiscosSchema(BaseModel):
    """ Define como retorna a lista de acidentes e riscos encontrados
    """
    Riscos: List[RiscoViewSchema]


def apresenta_lista_riscos(lista: List[Risco]):
    """ Retorna uma representação da lista de Riscos

    """
    result = []
    i = 1
    for item in lista:
       
        result.append({
            "id_risco": item.id_risco,
            "descricao": item.descricao,
            "percentual_taxa": item.percentual_taxa
        })
    return {"lista": result}        