# Write your MySQL query statement below


with CTE as (select d.name as Department, e.name as Employee , e.salary as Salary, dense_rank() over(partition by e.departmentId order by salary desc ) as rnk  from Employee e join Department d on d.id= e.departmentId )


select Department,  Employee,  Salary  from CTE where rnk <=3 ;