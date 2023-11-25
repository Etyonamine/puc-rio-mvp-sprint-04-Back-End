DROP TABLE acidente_ocorrencia;
CREATE TABLE "acidente_ocorrencia" (
	"id"	INTEGER,
	"id_conce"	INTEGER,
	"dat_acidente"	date,
	"hora_acidente"	datetime,
	"qtde_acidente"	INTEGER,
	"id_vitima_inc"	INTEGER,
	"nro_acidente_Km"	NUMERIC(10, 2),
	"id_trecho_oco"	VARCHAR(100),
	"id_ponto_cardeal"	INTEGER,
	"id_acidente_tip"	INTEGER,
	"qt_caminhao"	INTEGER,
	"qt_ilesos"	INTEGER,
	"qt_leve"	INTEGER,
	"qt_moderado"	INTEGER,
	"qt_grave"	INTEGER,
	"qt_mortos"	INTEGER,
	PRIMARY KEY("id","id_conce"),
	FOREIGN KEY(id_conce) REFERENCES concessionaria(id)
);