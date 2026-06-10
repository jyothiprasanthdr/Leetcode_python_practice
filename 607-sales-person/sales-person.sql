# Write your MySQL query statement below
with red_sales as (select sales_id from orders o
left join 
company c on o.com_id = c.com_id
where c.name = 'RED')

select s.name from Salesperson s
where s.sales_id not in (select sales_id from red_sales)
