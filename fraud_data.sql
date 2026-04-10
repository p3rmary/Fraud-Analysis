create table  public.fraud_data as
select 
hour_of_day,
datetime,
nameorig,
amount,
type,
oldbalanceorg as oldbalanceorig,
newbalanceorig,
namedest,
oldbalancedest,
newbalancedest,
isfraud,
isflaggedfraud
from public.aiml_dataset_enriched 
where isfraud = '1'
