from model import Base
from sqlalchemy import Column, String, Integer, DateTime,ForeignKey , Numeric

class Uf(Base):
    id = Column("id_uf", Integer, primary_key=True)    
    sigla = Column("sig_uf",String(2))
    descricao = Column("ds_descricao",String(100))