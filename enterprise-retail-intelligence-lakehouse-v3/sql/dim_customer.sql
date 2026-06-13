CREATE OR REPLACE VIEW gold.dim_customer AS
SELECT customer_id, customer_segment, location
FROM silver.customers;
