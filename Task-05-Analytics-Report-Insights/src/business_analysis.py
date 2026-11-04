
from pathlib import Path
import json
import pandas as pd
import numpy as np

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"

df = pd.read_csv(DATA_DIR / "superstore_cleaned.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

# 1. Overall business KPIs
total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
total_quantity = df["quantity"].sum()

kpis = {
    "total_sales": round(float(total_sales), 2),
    "total_profit": round(float(total_profit), 2),
    "total_orders": int(total_orders),
    "total_customers": int(total_customers),
    "total_quantity_sold": int(total_quantity),
    "average_order_value": round(
        float(total_sales / total_orders), 2
    ),
    "profit_margin_percent": round(
        float(total_profit / total_sales * 100), 2
    ),
    "average_discount_percent": round(
        float(df["discount"].mean() * 100), 2
    )
}

# 2. Category performance
category_summary = (
    df.groupby("category")
    .agg(
        sales=("sales", "sum"),
        profit=("profit", "sum"),
        quantity=("quantity", "sum")
    )
    .reset_index()
)

category_summary["profit_margin_percent"] = (
    category_summary["profit"] / category_summary["sales"] * 100
).round(2)

category_summary = category_summary.sort_values(
    "sales", ascending=False
)

# 3. Regional performance
region_summary = (
    df.groupby("region")
    .agg(
        sales=("sales", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "nunique")
    )
    .reset_index()
)

region_summary["profit_margin_percent"] = (
    region_summary["profit"] / region_summary["sales"] * 100
).round(2)

# 4. Monthly performance
df["order_month"] = df["order_date"].dt.to_period("M").astype(str)

monthly_summary = (
    df.groupby("order_month")
    .agg(
        sales=("sales", "sum"),
        profit=("profit", "sum"),
        orders=("order_id", "nunique")
    )
    .reset_index()
)

# 5. Sub-category profitability
subcategory_summary = (
    df.groupby("sub_category")
    .agg(
        sales=("sales", "sum"),
        profit=("profit", "sum"),
        quantity=("quantity", "sum")
    )
    .reset_index()
    .sort_values("profit")
)

# 6. Discount analysis
df["discount_band"] = pd.cut(
    df["discount"],
    bins=[-0.001, 0, 0.2, 0.4, 0.6, 0.8],
    labels=["No Discount", "1-20%", "21-40%", "41-60%", "61-80%"]
)

discount_summary = (
    df.groupby("discount_band", observed=False)
    .agg(
        records=("order_id", "size"),
        average_sales=("sales", "mean"),
        average_profit=("profit", "mean"),
        total_profit=("profit", "sum")
    )
    .reset_index()
)

# 7. Save outputs
outputs = {
    "category_performance.csv": category_summary,
    "regional_performance.csv": region_summary,
    "monthly_performance.csv": monthly_summary,
    "subcategory_performance.csv": subcategory_summary,
    "discount_analysis.csv": discount_summary
}

for filename, data in outputs.items():
    data.to_csv(RESULTS_DIR / filename, index=False)

with (RESULTS_DIR / "business_kpis.json").open(
    "w", encoding="utf-8"
) as file:
    json.dump(kpis, file, indent=4)

print("\n========== BUSINESS KPI SUMMARY ==========")
print(json.dumps(kpis, indent=4))

print("\n========== CATEGORY PERFORMANCE ==========")
print(category_summary.round(2).to_string(index=False))

print("\n========== REGIONAL PERFORMANCE ==========")
print(region_summary.round(2).to_string(index=False))

print("\n========== LOWEST PROFIT SUB-CATEGORIES ==========")
print(subcategory_summary.head(5).round(2).to_string(index=False))

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_summary.round(2).to_string(index=False))

print("\nBusiness analysis completed successfully!")
