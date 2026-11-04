from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"
CHART_DIR = RESULTS_DIR / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_DIR / "superstore_cleaned.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

sns.set_theme(style="whitegrid", palette="deep")


def save_chart(filename):
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Saved: {filename}")


# 1. Monthly sales trend
monthly = (
    df.assign(month=df["order_date"].dt.to_period("M").dt.to_timestamp())
    .groupby("month", as_index=False)["sales"]
    .sum()
)

plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly, x="month", y="sales", marker="o")
plt.title("Monthly Sales Trend", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
save_chart("01_monthly_sales_trend.png")


# 2. Sales and profit by category
category = (
    df.groupby("category", as_index=False)
    .agg(sales=("sales", "sum"), profit=("profit", "sum"))
    .melt(id_vars="category", var_name="metric", value_name="amount")
)

plt.figure(figsize=(10, 6))
sns.barplot(data=category, x="category", y="amount", hue="metric")
plt.title("Sales and Profit by Product Category", fontsize=15, weight="bold")
plt.xlabel("Category")
plt.ylabel("Amount ($)")
save_chart("02_category_sales_profit.png")


# 3. Regional sales performance
region = (
    df.groupby("region", as_index=False)["sales"]
    .sum()
    .sort_values("sales", ascending=False)
)

plt.figure(figsize=(9, 5))
sns.barplot(data=region, x="region", y="sales")
plt.title("Sales Performance by Region", fontsize=15, weight="bold")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
save_chart("03_regional_sales.png")


# 4. Profit by sub-category
subcategory = (
    df.groupby("sub_category", as_index=False)["profit"]
    .sum()
    .sort_values("profit")
)

plt.figure(figsize=(11, 8))
sns.barplot(data=subcategory, x="profit", y="sub_category")
plt.axvline(0, linewidth=1)
plt.title("Profitability by Product Sub-Category", fontsize=15, weight="bold")
plt.xlabel("Total Profit ($)")
plt.ylabel("Sub-Category")
save_chart("04_subcategory_profit.png")


# 5. Profit by discount band
df["discount_band"] = pd.cut(
    df["discount"],
    bins=[-0.001, 0, 0.2, 0.4, 0.6, 0.8],
    labels=["No Discount", "1-20%", "21-40%", "41-60%", "61-80%"]
)

discount = (
    df.groupby("discount_band", observed=False, as_index=False)["profit"]
    .sum()
)

plt.figure(figsize=(10, 5))
sns.barplot(data=discount, x="discount_band", y="profit")
plt.axhline(0, linewidth=1)
plt.title("Total Profit by Discount Band", fontsize=15, weight="bold")
plt.xlabel("Discount Band")
plt.ylabel("Total Profit ($)")
save_chart("05_discount_profit_analysis.png")


# 6. Sales and profit by customer segment
segment = (
    df.groupby("segment", as_index=False)
    .agg(sales=("sales", "sum"), profit=("profit", "sum"))
    .melt(id_vars="segment", var_name="metric", value_name="amount")
)

plt.figure(figsize=(9, 5))
sns.barplot(data=segment, x="segment", y="amount", hue="metric")
plt.title("Sales and Profit by Customer Segment", fontsize=15, weight="bold")
plt.xlabel("Customer Segment")
plt.ylabel("Amount ($)")
save_chart("06_customer_segment_performance.png")


print("\nAll visualizations created successfully!")
print(f"Chart folder: {CHART_DIR}")