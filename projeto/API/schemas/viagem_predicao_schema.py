from pydantic import BaseModel
from datetime import date, datetime
from model.viagemPredicao import ViagemPredicao


class ViagemPredicaoSchema(BaseModel):
    """Define como uma nova classe de predicao deve ser representado
    """
    dia:int = 1
    mes:int = 1
    id_sentido:int = 2
    id_trecho: int = 1
    pc_risco: float = 80.00


class ViagemPredicaoViewSchema(BaseModel):
    """Define como sera o retorno de uma predicao da viagem
    """
    id_risco:int = 1

def apresenta_resultado_predicao(id_risco: int):
        return {
            "id_risco": id_risco
        }