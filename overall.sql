create table totals as 
SELECT 
    date,
	type,
    SUM(amount) AS overall_volume,
    COUNT(*) AS total_transactions,

    -- fraud
    COUNT(*) FILTER (WHERE isfraud = 1) AS fraud_tx,
    SUM(amount) FILTER (WHERE isfraud = 1) AS fraud_volume,

    -- non-fraud
    COUNT(*) FILTER (WHERE isfraud = 0) AS non_fraud_tx,
    SUM(amount) FILTER (WHERE isfraud = 0) AS non_fraud_volume

FROM public.aiml_dataset_enriched
GROUP BY 1,2
ORDER BY 1;