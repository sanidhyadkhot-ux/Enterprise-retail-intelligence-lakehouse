# Power BI Measure Catalog

## Sales Measures

```DAX
Total Revenue = SUM(fact_sales[revenue])
Total Orders = DISTINCTCOUNT(fact_sales[sale_id])
Gross Profit = SUM(fact_sales[gross_profit])
Average Order Value = DIVIDE([Total Revenue], [Total Orders])
```

## Inventory Measures

```DAX
Stock On Hand = SUM(fact_inventory[stock_on_hand])
Low Stock Products = CALCULATE(COUNTROWS(fact_inventory), fact_inventory[stockout_risk] <> "Low")
Recommended Reorder Quantity = SUM(fact_inventory[recommended_reorder_qty])
```
