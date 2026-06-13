# Architecture Diagram

```text
+---------------------+
| Retail Source Data  |
| Sales, Inventory,   |
| Suppliers, Customers|
+----------+----------+
           |
           v
+---------------------+
| Azure Data Factory  |
| Batch ingestion     |
+----------+----------+
           |
           v
+---------------------+
| Bronze Layer        |
| Raw CSV/Parquet     |
+----------+----------+
           |
           v
+---------------------+
| Azure Databricks    |
| PySpark transforms  |
+----------+----------+
           |
           v
+---------------------+
| Silver Layer        |
| Clean conformed data|
+----------+----------+
           |
           v
+---------------------+
| Gold Layer          |
| Facts & Dimensions  |
+----------+----------+
           |
           v
+---------------------+
| Fabric Warehouse    |
| SQL serving layer   |
+----------+----------+
           |
           v
+---------------------+
| Power BI Dashboard  |
| Executive reporting |
+----------+----------+
           |
           v
+---------------------+
| AI Models           |
| Forecast + Stockout |
+---------------------+
```
