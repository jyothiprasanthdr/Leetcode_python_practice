# Write your MySQL query statement below


WITH Ranked AS (
    SELECT 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        RANK() OVER (PARTITION BY customer_id ORDER BY order_date) AS ranked
    FROM Delivery
),
CTE AS (
    SELECT 
        SUM(CASE WHEN order_date = customer_pref_delivery_date AND ranked = 1 THEN 1 ELSE 0 END) AS Immediate,
        COUNT(DISTINCT customer_id) AS Customer_count
    FROM Ranked
)
SELECT round((Immediate / Customer_count)* 100,2) as immediate_percentage 
FROM CTE;