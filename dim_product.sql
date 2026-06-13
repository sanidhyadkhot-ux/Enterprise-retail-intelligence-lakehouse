CREATE OR REPLACE VIEW gold.dim_product AS
SELECT product_id, product_name, category, unit_cost, unit_price, reorder_point
FROM silver.products;
