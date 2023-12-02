from pydantic import BaseModel
from typing import Optional, List
from model.uf import Uf

import numpy as np

class UfViewSchema(BaseModel):
    """ Define como deverá retornado
    """
    id: int = 1
    sigla: str = 'SP'
    descricao: str = 'SÃO PAULO'


class ListaUfSchema(BaseModel):
    """ Define como retorna a lista de Operacaos de operacao.
    """
    Uf: List[UfViewSchema]


def apresenta_lista_uf(lista: List[Uf]):
    """ Retorna uma representação da lista de unidades federativas seguindo o schema definido em
        UfViewSchema.

    """
    result = []
    for item in lista:
       
        result.append({
            "id": item.id,
            "sigla": item.sigla,
            "descricao": item.descricao
        })

    return {"lista": result}    