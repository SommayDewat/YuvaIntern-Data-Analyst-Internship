from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / "data" / "retail_sales.csv"
RESULTS = BASE / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

# 1. Load data
df = pd.read_csv(DATA)
initial_rows = len(df)

# 2. Clean and validate
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

numeric_columns = ["order_id", "quantity", "unit_price", "discount"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.drop_duplicates()
df = df.dropna(subset=[
    "order_id", "order_date", "region", "category",
    "product", "quantity", "unit_price", "discount"
])

df = df[
    (df["quantity"] > 0)
    & (df["unit_price"] >= 0)
    & (df["discount"] >= 0)
    & (df["discount"] <= df["quantity"] * df["unit_price"])
].copy()

df["order_id"] = df["order_id"].astype(int)
df["quantity"] = df["quantity"].astype(int)

# 3. Engineer sales metrics
df["gross_sales"] = df["quantity"] * df["unit_price"]
df["net_sales"] = df["gross_sales"] - df["discount"]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# 4. Aggregate results
category_sales = (
    df.groupby("category", as_index=False)
    .agg(orders=("order_id", "nunique"),
         units_sold=("quantity", "sum"),
         net_sales=("net_sales", "sum"))
    .sort_values("net_sales", ascending=False)
)

region_sales = (
    df.groupby("region", as_index=False)
    .agg(orders=("order_id", "nunique"),
         net_sales=("net_sales", "sum"))
    .sort_values("net_sales", ascending=False)
)

monthly_sales = (
    df.groupby("month", as_index=False)
    .agg(net_sales=("net_sales", "sum"))
    .sort_values("month")
)

# 5. Save outputs
df.to_csv(RESULTS / "cleaned_retail_sales.csv", index=False)
category_sales.to_csv(RESULTS / "category_sales_summary.csv", index=False)
region_sales.to_csv(RESULTS / "region_sales_summary.csv", index=False)
monthly_sales.to_csv(RESULTS / "monthly_sales_summary.csv", index=False)

quality = {
    "input_rows": int(initial_rows),
    "cleaned_rows": int(len(df)),
    "duplicate_rows_removed": int(initial_rows - len(pd.read_csv(DATA).drop_duplicates())),
    "missing_values_after_cleaning": int(df.isna().sum().sum()),
    "duplicate_rows_after_cleaning": int(df.duplicated().sum()),
    "invalid_quantity_rows": int((df["quantity"] <= 0).sum()),
    "net_sales_total": round(float(df["net_sales"].sum()), 2),
    "date_range_start": str(df["order_date"].min().date()),
    "date_range_end": str(df["order_date"].max().date())
}
with open(RESULTS / "data_quality_summary.json", "w", encoding="utf-8") as f:
    json.dump(quality, f, indent=2)

# 6. Visualizations
for filename, column, title, ylabel in [
    ("sales_by_category.png", category_sales, "Net Sales by Category", "Net Sales"),
    ("sales_by_region.png", region_sales, "Net Sales by Region", "Net Sales"),
    ("monthly_sales_trend.png", monthly_sales, "Monthly Net Sales Trend", "Net Sales"),
]:
    x_col = "month" if "monthly" in filename else (
        "category" if "category" in filename else "region"
    )
    plt.figure(figsize=(8, 5))
    plt.bar(column[x_col], column["net_sales"])
    plt.title(title)
    plt.xlabel(x_col.replace("_", " ").title())
    plt.ylabel(ylabel)
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(RESULTS / filename, dpi=150)
    plt.close()

# 7. Print business insights
print("RETAIL SALES ANALYSIS COMPLETED")
print("=" * 40)
print(f"Rows before cleaning: {initial_rows}")
print(f"Rows after cleaning: {len(df)}")
print(f"Total net sales: Rs. {df['net_sales'].sum():,.2f}")
print(f"Total units sold: {df['quantity'].sum()}")
print(f"Unique orders: {df['order_id'].nunique()}")

print("\nSales by category:")
print(category_sales.to_string(index=False))

print("\nSales by region:")
print(region_sales.to_string(index=False))

print("\nMonthly sales:")
print(monthly_sales.to_string(index=False))

print("\nOutput files saved in:", RESULTS)
