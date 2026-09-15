SELECT
    order_id,
    customer_id,
    product_id,
    quantity,
    price,
    quantity * price AS order_total,
    order_date
FROM {{ ref('stg_orders') }}