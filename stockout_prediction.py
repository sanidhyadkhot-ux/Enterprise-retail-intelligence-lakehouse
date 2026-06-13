import pandas as pd
import matplotlib.pyplot as plt
from config import GOLD_DIR, OUTPUT_DIR

inventory = pd.read_csv(GOLD_DIR / "fact_inventory.csv")
risk = inventory["stockout_risk"].value_counts()

plt.figure(figsize=(6,5))
risk.plot(kind="bar")
plt.title("Stockout Risk by Product Count")
plt.xlabel("Risk Level")
plt.ylabel("Product Count")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "charts" / "stockout_risk.png", dpi=120)
print("Stockout risk chart saved.")
