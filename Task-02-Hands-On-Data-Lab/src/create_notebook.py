import nbformat as nbf
from pathlib import Path

base = Path("Task-02-Hands-On-Data-Lab")
notebook_path = base / "notebooks" / "01_retail_sales_analysis.ipynb"

nb = nbf.v4.new_notebook()
cells = [
    nbf.v4.new_markdown_cell("""# Retail Sales Data Analysis

## Objective
Practice data loading, cleaning, validation, feature engineering, aggregation, visualization, and business interpretation using a synthetic retail dataset.

## Dataset
The dataset contains 20 sample orders across three product categories, four regions, and January–March 2026.

**Disclaimer:** This is synthetic learning data, not real business data.

## Analysis workflow
1. Load and inspect the data
2. Check data quality
3. Calculate gross and net sales
4. Compare category, regional, and monthly performance
5. Summarize findings and limitations
"""),
    nbf.v4.new_code_cell("""from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path.cwd()
if not (BASE / "data").exists():
    BASE = BASE / "Task-02-Hands-On-Data-Lab"

DATA = BASE / "data" / "retail_sales.csv"
RESULTS = BASE / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)
print("Dataset shape:", df.shape)
display(df.head())
"""),
    nbf.v4.new_markdown_cell("## 1. Data quality checks\nCheck missing values, duplicate rows, data types, and valid numerical ranges before analysis."),
    nbf.v4.new_code_cell("""print("Data types:")
display(df.dtypes.to_frame("data_type"))

print("Missing values per column:")
display(df.isna().sum().to_frame("missing_values"))

print("Exact duplicate rows:", int(df.duplicated().sum()))
print("Unique order IDs:", df["order_id"].nunique())
print("Non-positive quantities:", int((df["quantity"] <= 0).sum()))
print("Negative prices:", int((df["unit_price"] < 0).sum()))
print("Negative discounts:", int((df["discount"] < 0).sum()))
"""),
    nbf.v4.new_markdown_cell("## 2. Cleaning and feature engineering\nConvert dates and numeric columns, remove exact duplicates, and exclude incomplete or invalid records. Net sales are calculated as quantity × unit price − order-level discount."),
    nbf.v4.new_code_cell("""df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
for col in ["order_id", "quantity", "unit_price", "discount"]:
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
df["gross_sales"] = df["quantity"] * df["unit_price"]
df["net_sales"] = df["gross_sales"] - df["discount"]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

print("Rows after cleaning:", len(df))
print("Missing values after cleaning:", int(df.isna().sum().sum()))
print("Duplicate rows after cleaning:", int(df.duplicated().sum()))
"""),
    nbf.v4.new_markdown_cell("## 3. Key performance indicators\nCalculate total sales, number of orders, units sold, and average order value."),
    nbf.v4.new_code_cell("""total_sales = df["net_sales"].sum()
orders = df["order_id"].nunique()
units = df["quantity"].sum()
average_order_value = total_sales / orders if orders else 0

kpis = pd.DataFrame({
    "Metric": ["Net sales", "Unique orders", "Units sold", "Average order value"],
    "Value": [total_sales, orders, units, round(average_order_value, 2)]
})
display(kpis)
"""),
    nbf.v4.new_markdown_cell("## 4. Category and regional analysis"),
    nbf.v4.new_code_cell("""category_sales = df.groupby("category", as_index=False).agg(
    orders=("order_id", "nunique"),
    units_sold=("quantity", "sum"),
    net_sales=("net_sales", "sum")
).sort_values("net_sales", ascending=False)

region_sales = df.groupby("region", as_index=False).agg(
    orders=("order_id", "nunique"),
    net_sales=("net_sales", "sum")
).sort_values("net_sales", ascending=False)

display(category_sales)
display(region_sales)
"""),
    nbf.v4.new_markdown_cell("## 5. Monthly sales trend"),
    nbf.v4.new_code_cell("""monthly_sales = df.groupby("month", as_index=False).agg(
    net_sales=("net_sales", "sum")
).sort_values("month")

display(monthly_sales)

plt.figure(figsize=(8, 4))
plt.plot(monthly_sales["month"], monthly_sales["net_sales"], marker="o")
plt.title("Monthly Net Sales Trend")
plt.xlabel("Month")
plt.ylabel("Net sales (INR)")
plt.tight_layout()
plt.show()
"""),
    nbf.v4.new_markdown_cell("## 6. Visualizations"),
    nbf.v4.new_code_cell("""plt.figure(figsize=(8, 4))
plt.bar(category_sales["category"], category_sales["net_sales"])
plt.title("Net Sales by Category")
plt.xlabel("Category")
plt.ylabel("Net sales (INR)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
plt.bar(region_sales["region"], region_sales["net_sales"])
plt.title("Net Sales by Region")
plt.xlabel("Region")
plt.ylabel("Net sales (INR)")
plt.tight_layout()
plt.show()
"""),
    nbf.v4.new_markdown_cell("""## 7. Findings and limitations

- Electronics generated the highest category sales in this sample.
- North was the highest-sales region.
- March had the highest monthly sales in the observed period.
- Clothing sold more units than the other categories, but its total sales were lower than Electronics.
- The dataset is small and synthetic; results are illustrative, not generalizable business conclusions.
- The discount is treated as an order-level amount. Real datasets require confirmation of discount definitions and business rules.
"""),
    nbf.v4.new_code_cell("""# Export the cleaned analysis data and summaries
df.to_csv(RESULTS / "cleaned_retail_sales.csv", index=False)
category_sales.to_csv(RESULTS / "category_sales_summary.csv", index=False)
region_sales.to_csv(RESULTS / "region_sales_summary.csv", index=False)
monthly_sales.to_csv(RESULTS / "monthly_sales_summary.csv", index=False)

print("Analysis outputs saved to:", RESULTS.resolve())
""")
]

nb.cells = cells
nb.metadata = {
    "kernelspec": {
        "display_name": "Python (YuvaIntern Internship)",
        "language": "python",
        "name": "yuva-internship"
    },
    "language_info": {"name": "python"}
}
nbf.write(nb, notebook_path)
print("Notebook created:", notebook_path)
print("Cells:", len(nb.cells))
