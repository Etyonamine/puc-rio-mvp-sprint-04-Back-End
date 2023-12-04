drop table if EXISTS viagem;

CREATE TABLE viagem (
id_viagem INTEGER PRIMARY KEY AUTOINCREMENT,
dt_viagem datetime NOT NULL,
id_uf_ori TEXT(2) NOT NULL,
id_uf_dst TEXT(2) NOT NULL,
id_sentido INTEGER NOT NULL, 
id_trecho INTEGER NOT NULL,
vl_mercadoria NUMERIC(15,2) NOT NULL,
pc_risco NUMERIC(7,5) NOT NULL,
vl_taxa_agravo NUMERIC(15,2) NOT NULL,
vl_taxa_basica NUMERIC(15,2) NOT NULL,
vl_premio NUMERIC(15,2) NOT NULL, 
id_risco INTEGER NOT NULL, 
dt_inclusao datetime,
FOREIGN KEY (id_sentido) REFERENCES sentido(id_sentido),
FOREIGN KEY (id_trecho) REFERENCES trecho_ocorrencia(id),
FOREIGN KEY (id_uf_ori) REFERENCES uf(id_uf),
FOREIGN KEY (id_uf_dst) REFERENCES uf(id_uf),
FOREIGN KEY (id_risco) REFERENCES risco_ocorrencia (id_risco)
);