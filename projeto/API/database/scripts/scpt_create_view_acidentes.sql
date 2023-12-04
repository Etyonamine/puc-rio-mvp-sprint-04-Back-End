DROP VIEW IF EXISTS V_ACIDENTES_RISCOS_ACIDENTES;

CREATE VIEW V_ACIDENTES_RISCOS_ACIDENTES
AS 
	SELECT oco.dia, oco.mes, oco.id_trecho, oco.id_sentido, tpo_acd.Ds_Acidente_Tip ,rsc.ds_risco,  SUM(oco.qt_acidente) total_acidentes
	FROM acidente_ocorrencia oco
		 INNER JOIN tipo_acidente tpo_acd
			ON (tpo_acd.id_acidente_tip = oco.id_acidente_tip)
		 INNER JOIN risco_ocorrencia rsc
			ON (rsc.id_risco = oco.id_risco)
	GROUP BY oco.dia, oco.mes, oco.id_trecho, oco.id_sentido, tpo_acd.Ds_Acidente_Tip ,rsc.ds_risco;
	
 