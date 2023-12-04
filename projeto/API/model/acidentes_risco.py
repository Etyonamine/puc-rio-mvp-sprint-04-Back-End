from model import Base
from sqlalchemy import Column, String, Integer, DateTime,ForeignKey , Numeric

class acidentes_riscos(Base):
    __tablename__ = 'V_ACIDENTES_RISCOS'
    dia = Column("dia",Integer)
    mes = Column("mes",Integer)
    id_trecho = Column("mes",Integer)