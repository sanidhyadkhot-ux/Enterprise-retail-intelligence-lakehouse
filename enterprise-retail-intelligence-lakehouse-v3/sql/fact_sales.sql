CREATE OR REPLACE VIEW gold.fact_sales AS
SELECT
    sale_id,
    sale_date,
    product_id,
    customer_id,
    supplier_id,
    quantity,
    revenue,
    gross_profit,
    payment_method
FROM silver.sales;
