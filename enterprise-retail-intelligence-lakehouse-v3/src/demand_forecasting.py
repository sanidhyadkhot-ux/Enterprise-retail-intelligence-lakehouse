import pandas as pd
import matplotlib.pyplot as plt
from config import RAW_DIR, OUTPUT_DIR

sales = pd.read_csv(RAW_DIR / "sales.csv")
daily = sales.groupby("sale_date")["revenue"].sum().reset_index()
daily["sale_date"] = pd.to_datetime(daily["sale_date"])
daily["rolling_forecast"] = daily["revenue"].rolling(7, min_periods=1).mean()

plt.figure(figsize=(10,5))
plt.plot(daily["sale_date"].tail(60), daily["revenue"].tail(60), label="Actual")
plt.plot(daily["sale_date"].tail(60), daily["rolling_forecast"].tail(60), label="7-day rolling forecast")
plt.title("Retail Demand Forecast")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "charts" / "demand_forecast.png", dpi=120)
print("Forecast chart saved.")
