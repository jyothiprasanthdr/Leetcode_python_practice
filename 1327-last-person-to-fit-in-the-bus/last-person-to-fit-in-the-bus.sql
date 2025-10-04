# Write your MySQL query statement below

with cte as (select person_name,sum(weight) over (order by turn) as cum_weight from Queue)

select person_name from  cte  where cum_weight <=1000 order by cum_weight desc limit 1;





