CREATE OR REPLACE VIEW gold.dim_supplier AS
SELECT supplier_id, supplier_name, avg_lead_time_days, fill_rate
FROM silver.suppliers;
