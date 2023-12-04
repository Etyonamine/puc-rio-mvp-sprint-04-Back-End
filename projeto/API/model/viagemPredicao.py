
from datetime import date


class ViagemPredicao:
    def __init__(self, dia:int , mes:int, id_trecho:int, id_sentido:int, 
                 pc_risco:float, id_risco:int ):
        self.dia = dia
        self.mes = mes
        self.id_sentido = id_sentido
        self.id_trecho = id_trecho
        self.percentual_risco = pc_risco
        self.id_risco = id_risco

