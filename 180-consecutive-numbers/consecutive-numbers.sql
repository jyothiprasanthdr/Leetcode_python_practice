# Write your MySQL query statement below
with cte as (select num,lead(num) over (order by id) as next_num,  lag(num) over (order by id ) as prev_num  from Logs)


select distinct  num as ConsecutiveNums from cte where num = next_num and num = prev_num;