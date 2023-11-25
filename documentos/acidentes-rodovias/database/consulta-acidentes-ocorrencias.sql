SELECT con.nome, 
		tpo.Ds_Acidente_Tipo, 
		vit.ds_vitima_inc,
		trc.Ds_trecho_oco,
		pto.Ds_ponto_cardeal sentido,
		a.*
FROM acidente_ocorrencia a
	inner join tipo_acidente tpo on a.id_acidente_tip = tpo.id
	INNER JOIN concessionaria con on con.id = a.id_conce
	INNER JOIN vitima_incidencia vit on vit.id_vitima_inc = a.id_vitima_inc
	INNER JOIN trecho_ocorrencia trc on trc.id = a.id_trecho_oco 
	INNER JOIN ponto_cardeal pto on pto.id = a.id_ponto_cardeal
WHERE a.id_acidente_tip = 52
and a.dat_acidente ='19/03/2022';

SELECT con.nome, 
	  upper(tpo.Ds_Acidente_Tipo) tipo, 
	  sum(a.qt_caminhao) total		
FROM acidente_ocorrencia a
	inner join tipo_acidente tpo on a.id_acidente_tip = tpo.id
	INNER JOIN concessionaria con on con.id = a.id_conce
	INNER JOIN vitima_incidencia vit on vit.id_vitima_inc = a.id_vitima_inc
	INNER JOIN trecho_ocorrencia trc on trc.id = a.id_trecho_oco 
	INNER JOIN ponto_cardeal pto on pto.id = a.id_ponto_cardeal
GROUP BY con.nome,		tpo.Ds_Acidente_Tipo
Having sum(a.qt_caminhao) > 0 
order by 1,3;
	
select * from tipo_acidente  where Ds_Acidente_Tipo like ('%Não%');

select * from tipo_acidente order by Ds_Acidente_Tipo ;



