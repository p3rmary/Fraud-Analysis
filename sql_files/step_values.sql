create table step_values as 
select distinct 
step,
date,
datetime,
hour_of_day,
day_of_week,
is_weekend
from public.aiml_dataset_enriched
order by step 