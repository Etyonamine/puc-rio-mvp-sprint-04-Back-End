DROP TABLE IF EXISTS ACIDENTES_RISCOS;

CREATE table ACIDENTES_RISCOS(
dia INTEGER, 
mes INTEGER,
id_trecho INTEGER,
id_sentido INTEGER,
ds_sentido TEXT, 
ds_trecho_oco TEXT, 
ds_acidente_tip TEXT,
ds_risco TEXT,
total_acidentes INTEGER, 
PRIMARY KEY (dia, mes, id_trecho, id_sentido,ds_acidente_tip,ds_risco)
);

INSERT INTO ACIDENTES_RISCOS   SELECT * FROM V_ACIDENTES_RISCOS;
COMMIT;