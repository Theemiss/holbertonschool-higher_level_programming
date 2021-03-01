-- list record 
SELECT   score, count(*) as number FROM second_table GROUP BY score   ORDER BY number DESC; 
