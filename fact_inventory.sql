CREATE OR REPLACE VIEW gold.fact_inventory AS
SELECT
    product_id,
    supplier_id,
    stock_on_hand,
    reorder_point,
    avg_daily_demand,
    days_of_inventory,
    stockout_risk,
    recommended_reorder_qty
FROM silver.inventory_enriched;
