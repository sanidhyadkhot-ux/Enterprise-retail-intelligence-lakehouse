# Gold Data Model

## Dimensions

- dim_date
- dim_product
- dim_customer
- dim_supplier

## Facts

- fact_sales
- fact_inventory
- fact_supplier_performance

## Relationships

- fact_sales.product_id -> dim_product.product_id
- fact_sales.customer_id -> dim_customer.customer_id
- fact_inventory.product_id -> dim_product.product_id
- fact_supplier_performance.supplier_id -> dim_supplier.supplier_id
