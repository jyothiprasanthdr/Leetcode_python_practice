# Write your MySQL query statement below

With ranked_sales as (select product_id, year as first_year, quantity, price, Rank() over (partition by product_id order by year) as rnk from Sales)


select product_id, first_year, quantity, price from ranked_sales where rnk=1;