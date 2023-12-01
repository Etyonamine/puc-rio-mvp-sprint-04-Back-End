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

SELECT a.id_conce , 
	 upper(tpo.Ds_Acidente_Tipo) tipo, 
	  sum(a.qt_caminhao) total		,
	   a.id_acidente_tip
FROM acidente_ocorrencia a
	inner join tipo_acidente tpo on a.id_acidente_tip = tpo.id
	INNER JOIN concessionaria con on con.id = a.id_conce
GROUP BY con.nome,		tpo.Ds_Acidente_Tipo, a.id_conce, a.id_acidente_tip
Having sum(a.qt_caminhao) > 0 
--and a.id_acidente_tip in (96)
and a.id_conce = 4
order by 3 DESC;
	
select * from tipo_acidente  where Ds_Acidente_Tipo like ('%Não%');

select * from tipo_acidente where id in (6,13,18,29,96) order by Ds_Acidente_Tipo ;
select * from concessionaria where id in (4,6,8)



