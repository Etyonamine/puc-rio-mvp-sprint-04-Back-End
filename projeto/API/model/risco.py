from model import Base
from sqlalchemy import Column, String, Integer, DateTime,ForeignKey , Numeric

class Risco(Base):
    __tablename__ = 'risco_ocorrencia'
    id_risco = Column("id_risco", Integer, primary_key=True)
    descricao = Column("ds_risco", String)
    percentual_taxa = Column("pc_taxa", Numeric)
    