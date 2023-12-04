from model import Base
from sqlalchemy import Column, String, Integer, DateTime,ForeignKey , Numeric

class AcidentesRiscos(Base):
    __tablename__ = 'V_ACIDENTES_RISCOS'
    dia = Column("dia",Integer)
    mes = Column("mes",Integer)
    id_trecho = Column("id_trecho",Integer)
    id_sentido = Column("id_sentido",Integer)
    trecho = Column("id_trecho_oco",String)
    tipo_acidente = Column("ds_acidente_tip",String)
    risco = Column("ds_risco", String)
    total = Column("total_acidentes", Integer)
