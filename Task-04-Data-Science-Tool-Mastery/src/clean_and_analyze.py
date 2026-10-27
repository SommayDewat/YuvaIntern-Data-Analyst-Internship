
from pathlib import Path
import json

import numpy as np
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)

input_file = DATA_DIR / "restaurant_tips.csv"
df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)

# 1. Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# 2. Inspect missing values
missing_before = df.isnull().sum().to_dict()

# 3. Remove exact duplicate rows
duplicate_count = int(df.duplicated().sum())
df = df.drop_duplicates().copy()

# 4. Validate numerical columns
numeric_columns = ["total_bill", "tip", "size"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Remove records with missing critical values, if any
rows_before_validation = len(df)
df = df.dropna(subset=numeric_columns).copy()
rows_removed_missing = rows_before_validation - len(df)

# Check plausible business values
invalid_mask = (
    (df["total_bill"] <= 0)
    | (df["tip"] < 0)
    | (df["size"] <= 0)
)
invalid_count = int(invalid_mask.sum())
df = df.loc[~invalid_mask].copy()

# 5. NumPy calculations
bills = df["total_bill"].to_numpy()
tips = df["tip"].to_numpy()

summary = {
    "rows_after_cleaning": int(len(df)),
    "columns_after_cleaning": int(df.shape[1]),
    "duplicates_removed": duplicate_count,
    "rows_removed_for_missing_numeric_values": rows_removed_missing,
    "invalid_numeric_records_removed": invalid_count,
    "total_bill_mean": round(float(np.mean(bills)), 2),
    "total_bill_median": round(float(np.median(bills)), 2),
    "total_bill_std": round(float(np.std(bills)), 2),
    "tip_mean": round(float(np.mean(tips)), 2),
    "tip_median": round(float(np.median(tips)), 2),
    "tip_to_bill_ratio_percent": round(
        float((df["tip"].sum() / df["total_bill"].sum()) * 100), 2
    ),
    "missing_values_in_original_data": {
        str(key): int(value) for key, value in missing_before.items()
    },
}

# 6. Create a derived feature
df["tip_percentage"] = (
    df["tip"] / df["total_bill"] * 100
).round(2)

# 7. Save cleaned data and results
cleaned_file = DATA_DIR / "restaurant_tips_cleaned.csv"
df.to_csv(cleaned_file, index=False)

summary_file = RESULTS_DIR / "analysis_summary.json"
with summary_file.open("w", encoding="utf-8") as file:
    json.dump(summary, file, indent=4)

print("\n--- CLEANING SUMMARY ---")
print(json.dumps(summary, indent=4))

print("\n--- TIP PERCENTAGE SUMMARY ---")
print(df["tip_percentage"].describe().round(2))

print("\n--- AVERAGE TIP BY DAY ---")
print(df.groupby("day", observed=False)["tip"].mean().round(2))

print("\nCleaned dataset saved to:", cleaned_file)
print("Analysis summary saved to:", summary_file)
print("\nCleaning and analysis completed successfully!")
