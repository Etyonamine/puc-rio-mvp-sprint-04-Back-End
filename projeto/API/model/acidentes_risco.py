from model import Base
from sqlalchemy import Column, String, Integer, DateTime,ForeignKey , Numeric

class AcidentesRiscos(Base):
    __tablename__ = 'ACIDENTES_RISCOS'
    dia = Column("dia",Integer,  primary_key=True)
    mes = Column("mes",Integer,  primary_key=True)
    id_trecho = Column("id_trecho",Integer, primary_key=True)
    id_sentido = Column("id_sentido",Integer,  primary_key=True)
    trecho = Column("ds_trecho_oco",String)
    tipo_acidente = Column("ds_acidente_tip",String, primary_key=True)
    risco = Column("ds_risco", String, primary_key=True)
    total = Column("total_acidentes", Integer)
