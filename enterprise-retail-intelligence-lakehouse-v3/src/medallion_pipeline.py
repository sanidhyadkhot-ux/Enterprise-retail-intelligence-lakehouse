import pandas as pd
from config import RAW_DIR, BRONZE_DIR, SILVER_DIR, GOLD_DIR

def run_pipeline():
    sales = pd.read_csv(RAW_DIR / "sales.csv")
    products = pd.read_csv(RAW_DIR / "products.csv")
    inventory = pd.read_csv(RAW_DIR / "inventory.csv")
    suppliers = pd.read_csv(RAW_DIR / "suppliers.csv")
    customers = pd.read_csv(RAW_DIR / "customers.csv")

    # Bronze
    for name, df in {
        "bronze_sales.csv": sales,
        "bronze_products.csv": products,
        "bronze_inventory.csv": inventory,
        "bronze_suppliers.csv": suppliers,
        "bronze_customers.csv": customers,
    }.items():
        df.to_csv(BRONZE_DIR / name, index=False)

    # Silver
    sales = sales.drop_duplicates()
    sales["sale_date"] = pd.to_datetime(sales["sale_date"])
    silver_sales = sales.merge(products[["product_id", "category", "unit_cost", "supplier_id"]], on="product_id", how="left")
    silver_sales["gross_profit"] = silver_sales["revenue"] - (silver_sales["quantity"] * silver_sales["unit_cost"])

    silver_sales.to_csv(SILVER_DIR / "silver_sales.csv", index=False)
    products.to_csv(SILVER_DIR / "silver_products.csv", index=False)
    inventory.to_csv(SILVER_DIR / "silver_inventory.csv", index=False)
    suppliers.to_csv(SILVER_DIR / "silver_suppliers.csv", index=False)
    customers.to_csv(SILVER_DIR / "silver_customers.csv", index=False)

    # Gold
    fact_sales = silver_sales[["sale_id","sale_date","product_id","customer_id","supplier_id","quantity","revenue","gross_profit","payment_method"]]
    fact_sales.to_csv(GOLD_DIR / "fact_sales.csv", index=False)

    velocity = sales.groupby("product_id")["quantity"].sum().reset_index()
    velocity["avg_daily_demand"] = velocity["quantity"] / sales["sale_date"].nunique()

    fact_inventory = inventory.merge(velocity[["product_id", "avg_daily_demand"]], on="product_id", how="left").fillna(0)
    fact_inventory = fact_inventory.merge(suppliers[["supplier_id","avg_lead_time_days","fill_rate"]], on="supplier_id", how="left")
    fact_inventory["days_of_inventory"] = fact_inventory["stock_on_hand"] / fact_inventory["avg_daily_demand"].replace(0, 0.01)
    fact_inventory["stockout_risk"] = fact_inventory.apply(
        lambda r: "High" if r["days_of_inventory"] <= r["avg_lead_time_days"] else ("Medium" if r["stock_on_hand"] <= r["reorder_point"] else "Low"),
        axis=1
    )
    fact_inventory["recommended_reorder_qty"] = ((fact_inventory["avg_daily_demand"] * (fact_inventory["avg_lead_time_days"] + 7)) - fact_inventory["stock_on_hand"]).clip(lower=0).round()

    fact_inventory.to_csv(GOLD_DIR / "fact_inventory.csv", index=False)
    products.to_csv(GOLD_DIR / "dim_product.csv", index=False)
    customers.to_csv(GOLD_DIR / "dim_customer.csv", index=False)
    suppliers.to_csv(GOLD_DIR / "dim_supplier.csv", index=False)

if __name__ == "__main__":
    run_pipeline()
    print("Medallion pipeline completed.")
