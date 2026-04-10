select 
hour_of_day,
count(*)as total_transactions,
sum(amount) as total_volume
from public.aiml_dataset_enriched
group by 1