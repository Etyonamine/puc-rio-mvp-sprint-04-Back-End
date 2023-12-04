from pydantic import BaseModel
from datetime import date, datetime
from model.viagemPredicao import ViagemPredicao

class ViagemSchema(BaseModel):
    """Define como uma nova viagem a ser inserido deve ser representado
    """
    data:str ='2023-01-01 01:00:00'
    id_uf_ori:int = 20
    id_uf_dst:int = 24
    id_sentido:int = 1
    id_trecho:int = 1
    vl_mercadoria:float = 200000.00
    pc_risco:float = 80.00
    vl_taxa_basica:float = 0.005
    vl_premio:float = 20.00
 
 