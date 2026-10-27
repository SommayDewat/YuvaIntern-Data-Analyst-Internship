
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "restaurant_tips_cleaned.csv"
CHART_DIR = PROJECT_DIR / "results" / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)

sns.set_theme(style="whitegrid")

# Chart 1: Distribution of total bills
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="total_bill", bins=20, kde=True)
plt.title("Distribution of Restaurant Bills")
plt.xlabel("Total Bill")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig(CHART_DIR / "bill_distribution.png", dpi=150)
plt.close()

# Chart 2: Average tip by day
day_order = ["Thur", "Fri", "Sat", "Sun"]
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="day", y="tip", order=day_order, errorbar=None)
plt.title("Average Tip by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.tight_layout()
plt.savefig(CHART_DIR / "average_tip_by_day.png", dpi=150)
plt.close()

# Chart 3: Bill versus tip
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="time",
    size="size",
    sizes=(30, 150),
    alpha=0.8
)
plt.title("Relationship Between Bill Amount and Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.tight_layout()
plt.savefig(CHART_DIR / "bill_vs_tip.png", dpi=150)
plt.close()

# Chart 4: Average tip percentage by time
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="time", y="tip_percentage", errorbar=None)
plt.title("Average Tip Percentage by Meal Time")
plt.xlabel("Meal Time")
plt.ylabel("Average Tip Percentage (%)")
plt.tight_layout()
plt.savefig(CHART_DIR / "tip_percentage_by_time.png", dpi=150)
plt.close()

# Chart 5: Correlation heatmap for numeric variables
numeric_df = df[["total_bill", "tip", "size", "tip_percentage"]]
correlations = numeric_df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    correlations,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)
plt.title("Correlation Between Numeric Variables")
plt.tight_layout()
plt.savefig(CHART_DIR / "correlation_heatmap.png", dpi=150)
plt.close()

print("All visualizations created successfully!")
print(f"Chart folder: {CHART_DIR}")

for chart in sorted(CHART_DIR.glob("*.png")):
    print("-", chart.name)

