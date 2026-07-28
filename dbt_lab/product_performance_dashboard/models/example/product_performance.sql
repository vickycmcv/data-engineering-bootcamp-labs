SELECT
    product,
    COUNT(*) AS total_orders,
    SUM(amount) AS product_revenue
FROM {{ ref('sales_data') }}
GROUP BY product
ORDER BY product_revenue DESC