drop table if exists cliente;
drop table if exists averbacao;
drop table if exists averbacao_risco_detalhe;

create table cliente(
id_cliente INTEGER PRIMARY KEY,
ds_cliente TEXT (300) NOT NULL
);

CREATE TABLE averbacao (
id_averbacao INTEGER PRIMARY KEY,
id_cliente INTEGER NOT NULL, 
dat_averbacao date NOT NULL,
sig_uf_ori TEXT(2) NOT NULL,
sig_uf_dst TEXT(2) NOT NULL,
id_risco INTEGER NOT NULL,
vl_premio NUMERIC(15,2) NOT NULL, 
vl_mercadoria NUMERIC(15,2) NOT NULL,
vl_taxa_agravo NUMERIC(15,2) NOT NULL,
vl_taxa_basica NUMERIC(15,2) NOT NULL,
dat_inclusao datetime,
FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

CREATE TABLE averbacao_risco_detalhe(
id_averbacao INTEGER,
id_conce INTEGER, 
id_acidente_tip INTEGER,
id_risco INTEGER,
PRIMARY KEY(id_averbacao, id_conce, id_acidente_tip),
FOREIGN KEY (id_averbacao) REFERENCES averbacao (id_averbacao), 
FOREIGN KEY (id_conce) REFERENCES concessionaria (id_conce), 
FOREIGN KEY (id_acidente_tip) REFERENCES tipo_acidente (id_acidente_tip), 
FOREIGN KEY (id_risco) REFERENCES classificacao_risco (id_risco)
)

