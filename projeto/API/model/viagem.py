from model import Base
from sqlalchemy import Column, String, Integer, DateTime,ForeignKey , Numeric
from datetime import datetime
from typing import  Union

class Viagem(Base):
    __tablename__ = 'viagem'
    id = Column("id_viagem", Integer, primary_key=True) 
    data = Column("dt_viagem",DateTime)
    id_uf_origem = Column("id_uf_ori", Integer)
    id_uf_destino = Column("id_uf_dst", Integer)
    id_sentido = Column ("id_sentido", Integer)
    id_trecho =  Column ("id_trecho", Integer)
    valor_mercadoria = Column ("vl_mercadoria", Integer)
    valor_taxa_agravo = Column ("vl_taxa_agravo", Numeric)
    valor_taxa_basica = Column ("vl_taxa_basica", Numeric)
    valor_premio = Column ("vl_premio", Numeric)
    id_risco = Column ("id_risco", Integer)
    percentual_risco  = Column("pc_risco", Numeric)
    data_inclusao = Column("dt_inclusao",DateTime, default=datetime.now())
    
    def __init__(self, data:String, id_uf_ori:int, id_uf_dst:int,
                id_sentido: int , id_trecho: int, vl_merc: float, vl_tx_bsc: float,
                pc_risco: float,vl_pmo: float, data_insercao:Union[DateTime, None] = None):
        """Criando a classe 
            data = data de viagem
            id_uf_origem = estado origem da viagem
            id_uf_destino = estado destino da viagem
            id_sentido = sentido da rodovia da viagem
            id_trecho = sentido do trecho da rodovia
            valor_mercadoria = valor do mercadoria que fará viagem
            valor_taxa_agravo = valor calculado conforme retorno da predicao (1-baixo (0,02%) 2 - medio (0,03%) - alto (0,05%))
            valor_taxa_basica = valor da taxa de calculo para o premio do seguro no percurso da viagem
            valor_premio = valor calculado taxa basica x valor de mercadoria
            id_risco = codigo do risco retornado pela predição.
            percentual_risco = valor passado para a predição para avaliar o risco com maior ocorrencia.
            data_inclusao = data de inclusao do registro.
        """
        self.data =  datetime.strptime(data, "%Y-%m-%d %H:%M:%S")  
        self.id_uf_origem = id_uf_ori
        self.id_uf_destino = id_uf_dst
        self.id_sentido = id_sentido
        self.id_trecho = id_trecho
        self.valor_mercadoria = vl_merc
        self.valor_taxa_basica = vl_tx_bsc
        self.valor_premio = vl_pmo
        self.data_inclusao = data_insercao
        self.percentual_risco = pc_risco

        
