SELECT
    customer,
    total_sales,
    CASE 
        WHEN total_sales < 30000 THEN 'Low Value'
        WHEN total_sales <= 70000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS customer_segment
FROM {{ ref('customer_sales') }}
ORDER BY total_sales DESC