CREATE TABLE public.aiml_dataset_enriched AS
SELECT
    *,
    TIMESTAMP '2024-01-01' + (step * INTERVAL '1 hour') AS datetime,
    EXTRACT(HOUR FROM TIMESTAMP '2024-01-01' + (step * INTERVAL '1 hour')) AS hour_of_day,
    TRIM(TO_CHAR(TIMESTAMP '2024-01-01' + (step * INTERVAL '1 hour'), 'Day')) AS day_of_week,
    EXTRACT(DOW FROM TIMESTAMP '2024-01-01' + (step * INTERVAL '1 hour')) IN (0, 6) AS is_weekend
FROM public.aiml_dataset;
