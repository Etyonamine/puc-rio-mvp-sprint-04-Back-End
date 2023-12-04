DROP VIEW IF EXISTS V_ACIDENTES_RISCOS;

CREATE VIEW V_ACIDENTES_RISCOS
AS 
	SELECT oco.dia, oco.mes,oco.id_trecho ,oco.id_sentido, snt.ds_sentido, tr.Ds_trecho_oco, tpo_acd.Ds_Acidente_Tip ,rsc.ds_risco,  SUM(oco.qt_acidente) total_acidentes
	FROM acidente_ocorrencia oco
		 INNER JOIN tipo_acidente tpo_acd
			ON (tpo_acd.id_acidente_tip = oco.id_acidente_tip)
		 INNER JOIN risco_ocorrencia rsc
			ON (rsc.id_risco = oco.id_risco)
		 INNER JOIN trecho_ocorrencia tr
			ON (tr.id = oco.id_trecho)
		 INNER JOIN sentido snt
			ON (snt.id_sentido = oco.id_sentido)
	GROUP BY oco.dia, oco.mes,oco.id_trecho ,oco.id_sentido, snt.ds_sentido, tr.Ds_trecho_oco, tpo_acd.Ds_Acidente_Tip ,rsc.ds_risco;
	
 