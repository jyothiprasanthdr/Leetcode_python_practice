# Write your MySQL query statement below


WITH salary_categories AS (
    SELECT 'Low Salary' AS salary_type
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
),
salaries AS (
    SELECT *,
           CASE 
               WHEN income < 20000 THEN 'Low Salary'
               WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
               WHEN income > 50000 THEN 'High Salary'
           END AS salary_type
    FROM Accounts
)
SELECT sc.salary_type as category,
       COALESCE(COUNT(s.account_id), 0) AS accounts_count
FROM salary_categories sc
LEFT JOIN salaries s
       ON sc.salary_type = s.salary_type
GROUP BY sc.salary_type
ORDER BY sc.salary_type;

