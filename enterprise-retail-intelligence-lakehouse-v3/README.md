# Enterprise Retail Intelligence Lakehouse

![Project Type](https://img.shields.io/badge/Project-End--to--End%20Data%20Platform-blue)
![Stack](https://img.shields.io/badge/Stack-ADF%20%7C%20Databricks%20%7C%20Fabric%20%7C%20Power%20BI-green)
![AI](https://img.shields.io/badge/AI-Demand%20Forecasting%20%7C%20Stockout%20Prediction-purple)
![Role Focus](https://img.shields.io/badge/Roles-Data%20Analyst%20%7C%20BI%20Analyst%20%7C%20Analytics%20Engineer%20%7C%20Data%20Engineer-orange)

## 1. Executive Summary

**Enterprise Retail Intelligence Lakehouse** is a recruiter-focused, end-to-end data platform project that turns retail sales, inventory, supplier and customer data into analytics-ready models, Power BI dashboards and AI-driven inventory recommendations.

This project is designed as a modern cloud data solution using:

- **Azure Data Factory** for ingestion orchestration
- **Azure Databricks / PySpark** for data engineering and transformation
- **Bronze, Silver and Gold Medallion Architecture**
- **Microsoft Fabric Warehouse** for serving curated data
- **SQL dimensional modelling** for analytics
- **Power BI** for executive reporting
- **Machine Learning** for demand forecasting and stockout prediction

The project is inspired by a real grocery inventory and sales management business case involving product management, procurement/GRN, FIFO costing, point-of-sale transactions, stock ledger movement, low-stock alerts and dashboard reporting.

---

## 2. Business Problem

Small and mid-sized retailers often have fragmented data across sales systems, spreadsheets, supplier records and inventory tools. This creates operational problems such as:

- Stockouts on high-demand products
- Overstocking slow-moving products
- Poor visibility into daily revenue and product profitability
- Manual reporting delays
- Limited supplier performance tracking
- Difficulty forecasting demand
- Weak inventory valuation and reorder planning

The goal of this project is to build a scalable retail intelligence platform that provides accurate, timely and actionable business insights.

---

## 3. Project Objectives

This project demonstrates the complete modern data lifecycle:

1. Ingest raw retail data from multiple source systems.
2. Store raw data in the Bronze layer.
3. Clean, validate and standardise records in the Silver layer.
4. Build curated business-ready Gold models.
5. Load Gold tables into a Fabric Warehouse.
6. Create Power BI-ready facts and dimensions.
7. Build demand forecasting and stockout prediction models.
8. Generate business recommendations for retail managers.

---

## 4. Roles Covered

This project is designed to support multiple target roles:

| Role | How This Project Supports It |
|---|---|
| Data Analyst | Power BI dashboards, KPIs, SQL analysis, business recommendations |
| BI Analyst | Star schema, DAX-ready measures, executive reporting design |
| Analytics Engineer | Medallion architecture, SQL models, clean analytics layer |
| Data Engineer | ADF ingestion, Databricks notebooks, PySpark transformations |
| Data & AI Consultant | Forecasting, stockout prediction, business recommendations |

---

## 5. High-Level Architecture

```text
Retail Source Systems
│
├── Sales Transactions
├── Inventory Stock Ledger
├── Supplier / GRN Data
├── Customer Data
└── Product Master Data
        │
        ▼
Azure Data Factory
        │
        ▼
Azure Data Lake / Bronze Layer
        │
        ▼
Azure Databricks / PySpark
        │
        ▼
Silver Layer
Cleaned, validated and conformed data
        │
        ▼
Gold Layer
Facts, dimensions and business aggregates
        │
        ▼
Microsoft Fabric Warehouse
        │
        ▼
Power BI Dashboards
        │
        ▼
AI Models
Demand Forecasting, Stockout Prediction, Inventory Optimisation
```

See: `architecture/architecture_diagram.md`

---

## 6. Source Systems

The platform uses four primary source data domains:

| Source | Description | Example Fields |
|---|---|---|
| Sales Data | POS transactions and sales line items | sale_id, product_id, customer_id, quantity, revenue |
| Inventory Data | Stock movements, on-hand quantity and reorder thresholds | product_id, stock_on_hand, reorder_point |
| Supplier Data | Supplier delivery and GRN records | supplier_id, lead_time_days, fill_rate |
| Customer Data | Customer profile and purchase behaviour | customer_id, segment, location |

---

## 7. Medallion Architecture

### Bronze Layer

Raw ingested data with minimal transformation.

Purpose:

- Preserve original source records
- Enable auditability
- Support reprocessing if business rules change

Tables:

- `bronze_sales`
- `bronze_inventory`
- `bronze_suppliers`
- `bronze_customers`
- `bronze_products`

### Silver Layer

Cleaned and standardised data.

Key transformations:

- Remove duplicates
- Standardise date fields
- Validate quantity and revenue values
- Join product/category metadata
- Clean supplier lead time fields
- Flag invalid inventory records

Tables:

- `silver_sales`
- `silver_inventory`
- `silver_suppliers`
- `silver_customers`
- `silver_products`

### Gold Layer

Business-ready analytics layer.

Tables:

- `fact_sales`
- `fact_inventory`
- `fact_supplier_performance`
- `dim_product`
- `dim_customer`
- `dim_supplier`
- `dim_date`

---

## 8. Data Model

```text
dim_date
   │
   ├── fact_sales ─── dim_product
   │        │
   │        └── dim_customer
   │
   ├── fact_inventory ─── dim_product
   │
   └── fact_supplier_performance ─── dim_supplier
```

The Gold layer follows a star schema to make Power BI reporting fast, clean and recruiter-friendly.

---

## 9. Key KPIs

### Sales KPIs

- Total Revenue
- Total Orders
- Average Order Value
- Gross Margin
- Units Sold
- Top Selling Products

### Inventory KPIs

- Stock on Hand
- Inventory Value
- Low Stock Product Count
- Stockout Risk Score
- Days of Inventory Remaining
- Reorder Quantity

### Supplier KPIs

- Average Lead Time
- Supplier Fill Rate
- Late Delivery Count
- Supplier Reliability Score

### Customer KPIs

- Active Customers
- Repeat Customer Rate
- Customer Lifetime Value Proxy
- Segment Revenue Contribution

---

## 10. AI and Machine Learning Components

### Demand Forecasting

Forecasts product-level demand using historical sales volume.

Use case:

- Predict next 7, 14 and 30 days of product demand
- Support procurement planning
- Reduce manual guesswork

Output:

- `outputs/charts/demand_forecast.png`
- `src/demand_forecasting.py`

### Stockout Prediction

Predicts whether a product is likely to stock out based on:

- Current stock
- Reorder threshold
- Sales velocity
- Supplier lead time
- Recent demand pattern

Output:

- `outputs/charts/stockout_risk.png`
- `src/stockout_prediction.py`

### Inventory Optimisation

Calculates recommended reorder quantity using:

- Average daily demand
- Lead time
- Safety stock
- Current stock on hand

Output:

- `data/gold/inventory_recommendations.csv`

---

## 11. Power BI Dashboard Design

The Power BI design includes four reporting pages.

### Page 1: Executive Overview

KPIs:

- Total Revenue
- Gross Margin
- Total Orders
- Inventory Value
- Stockout Risk Count

Visuals:

- Daily Revenue Trend
- Revenue by Category
- Top Products by Sales
- Payment Method Split

### Page 2: Inventory Control

KPIs:

- Stock on Hand
- Low Stock Count
- Days of Inventory
- Reorder Quantity

Visuals:

- Low Stock Products
- Inventory Value by Category
- Stockout Risk Matrix
- Recommended Reorders

### Page 3: Supplier Performance

KPIs:

- Average Lead Time
- Fill Rate
- Late Delivery Count
- Supplier Risk Score

Visuals:

- Supplier Lead Time Trend
- Supplier Fill Rate Ranking
- Delayed GRNs

### Page 4: Customer Intelligence

KPIs:

- Active Customers
- Repeat Purchase Rate
- Revenue by Segment
- Average Order Value

Visuals:

- Customer Segment Revenue
- Top Customer Groups
- RFM-style customer value proxy

---

## 12. Repository Structure

```text
enterprise-retail-intelligence-lakehouse
│
├── README.md
├── PROJECT_SUMMARY.md
├── requirements.txt
│
├── architecture/
│   ├── architecture_diagram.md
│   └── data_model.md
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── docs/
│   ├── business_requirements.md
│   ├── powerbi_dashboard_spec.md
│   └── business_recommendations.md
│
├── notebooks/
│   ├── 01_adf_ingestion_design.py
│   ├── 02_bronze_to_silver_databricks.py
│   ├── 03_silver_to_gold_databricks.py
│   ├── 04_fabric_warehouse_load.py
│   └── 05_ai_forecasting_and_stockout_prediction.py
│
├── outputs/
│   ├── charts/
│   └── powerbi_mockups/
│
├── powerbi/
│   └── dashboard_measure_catalog.md
│
├── sql/
│   ├── create_gold_schema.sql
│   ├── fact_sales.sql
│   ├── fact_inventory.sql
│   ├── dim_product.sql
│   ├── dim_customer.sql
│   └── dim_supplier.sql
│
└── src/
    ├── config.py
    ├── generate_sample_data.py
    ├── medallion_pipeline.py
    ├── demand_forecasting.py
    └── stockout_prediction.py
```

---

## 13. How to Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/generate_sample_data.py
python src/medallion_pipeline.py
python src/demand_forecasting.py
python src/stockout_prediction.py
```

---

## 14. Business Recommendations

Based on the analytics layer, the project recommends:

1. Prioritise replenishment for products with high sales velocity and low stock.
2. Monitor suppliers with high lead times and declining fill rates.
3. Use demand forecasting to prepare stock before seasonal sales spikes.
4. Reduce working capital tied in slow-moving inventory.
5. Use category-level margin analysis to optimise promotional pricing.
6. Introduce automated reorder thresholds for high-demand items.
7. Use dashboard alerts for daily store manager decision-making.

---

## 15. Resume-Ready Project Bullets

- Built an end-to-end retail Lakehouse platform using Azure Data Factory, Databricks, Microsoft Fabric, SQL and Power BI.
- Designed Bronze, Silver and Gold Medallion architecture for sales, inventory, supplier, customer and product data.
- Developed PySpark transformation logic to clean, validate and model raw retail data into analytics-ready fact and dimension tables.
- Created Power BI dashboard specifications covering revenue, inventory health, supplier performance and customer behaviour.
- Implemented demand forecasting and stockout prediction workflows to support inventory optimisation and replenishment planning.
- Built a star schema data model for reporting across sales, inventory, suppliers and customer segments.

---

## 16. Future Enhancements

- Add Azure Event Hub for near real-time POS streaming
- Add Microsoft Fabric Data Activator alerts for stockout events
- Add Power BI embedded analytics
- Add customer segmentation model
- Add dbt-style testing and documentation
- Add CI/CD using GitHub Actions
- Add Unity Catalog governance layer
- Add GenAI assistant for retail managers

---

## 17. Why This Project Matters

This project demonstrates practical, business-facing data engineering and analytics skills. It combines cloud architecture, analytics engineering, BI storytelling and AI use cases into one portfolio-ready project.

It is suitable for:

- Data Analyst roles
- BI Analyst roles
- Analytics Engineer roles
- Junior Data Engineer roles
- Data & AI Consultant roles
- Azure / Fabric Consultant roles
