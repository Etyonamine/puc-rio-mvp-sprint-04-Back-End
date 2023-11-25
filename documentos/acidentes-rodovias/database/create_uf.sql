CREATE TABLE UF(
 id_uf INTEGER PRIMARY KEY, 
 sig_uf varchar(2),
 ds_uf varchar(100) 
);
 
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(1, 'Acre' , 'AC'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(2, 'Alagoas' , 'AL'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(3, 'Amapá' , 'AP'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(4, 'Amazonas' , 'AM'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(5, 'Bahia' , 'BA'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(6, 'Ceará' , 'CE'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(7, 'Distrito Federal' , 'DF'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(8, 'Espírito Santo' , 'ES'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(9, 'Goiás' , 'GO'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(27,'Maranhão' , 'MA' 		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(10,'Mato Grosso' , 'MT'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(11,'Mato Grosso do Sul' , 'MS'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(12,'Minas Gerais' , 'MG'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(13,'Pará' , 'PA'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(14,'Paraíba' , 'PB'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(15,'Paraná' , 'PR'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(16,'Pernambuco' , 'PE'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(17,'Piauí' , 'PI'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(18,'Roraima' , 'RR'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(19,'Rondônia' , 'RO'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(20,'Rio de Janeiro' , 'RJ'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(21,'Rio Grande do Norte' , 'RN'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(22,'Rio Grande do Sul' , 'RS'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(23,'Santa Catarina' , 'SC'	       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(24,'São Paulo' , 'SP'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(25,'Sergipe' , 'SE'		       );
 INSERT INTO UF (id_uf, ds_uf, sig_uf)VALUES(26,'Tocantins' , 'TO' 		       );

CREATE TABLE concessionaria_estados(
id INTEGER PRIMARY KEY,
id_uf INTEGER NOT NULL,
	 FOREIGN KEY(id_uf) REFERENCES UF(artistid)
);