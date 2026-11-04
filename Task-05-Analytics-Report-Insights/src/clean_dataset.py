
from pathlib import Path
import json
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)

files = list(DATA_DIR.glob("*.csv"))
if not files:
    raise FileNotFoundError("Superstore CSV not found.")

df = pd.read_csv(files[0], encoding="latin1")

print("Original dataset:", df.shape)

# Standardize column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(r"[\s-]+", "_", regex=True)
)

# Convert date columns
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce"
)
df["ship_date"] = pd.to_datetime(
    df["ship_date"], errors="coerce"
)

# Convert numerical columns
numeric_columns = [
    "sales", "quantity", "discount", "profit"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column], errors="coerce"
    )

# Record initial quality
missing_before = df.isnull().sum()
duplicates_before = int(df.duplicated().sum())

# Remove exact duplicate rows
df = df.drop_duplicates().copy()

# Remove rows missing essential analytical fields
essential_columns = [
    "order_id", "order_date", "sales",
    "quantity", "discount", "profit"
]

rows_before = len(df)
df = df.dropna(subset=essential_columns).copy()
missing_rows_removed = rows_before - len(df)

# Validate business values
invalid_mask = (
    (df["sales"] < 0)
    | (df["quantity"] <= 0)
    | (df["discount"] < 0)
    | (df["discount"] > 1)
)

invalid_records = int(invalid_mask.sum())
df = df.loc[~invalid_mask].copy()
original_column_count = len(df.columns)

# Feature engineering
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.strftime("%b")
df["profit_margin"] = (
    df["profit"] / df["sales"] * 100
).round(2)

# Order-level metrics will be calculated separately
# in the analysis script to avoid counting order IDs as rows.

# Save cleaned dataset
output_file = DATA_DIR / "superstore_cleaned.csv"
df.to_csv(output_file, index=False)

quality_report = {
    "original_rows": int(len(pd.read_csv(files[0], encoding="latin1"))),
    "cleaned_rows": int(len(df)),
    "original_columns": int(original_column_count),
    "cleaned_columns": int(len(df.columns)),
    "missing_values_before": {
        str(k): int(v) for k, v in missing_before.items()
    },
    "exact_duplicates_before": duplicates_before,
    "rows_removed_for_missing_essential_fields": int(missing_rows_removed),
    "invalid_business_records_removed": invalid_records,
    "remaining_missing_values": int(df.isnull().sum().sum()),
    "remaining_duplicates": int(df.duplicated().sum())
}

with (RESULTS_DIR / "data_quality_report.json").open(
    "w", encoding="utf-8"
) as file:
    json.dump(quality_report, file, indent=4)

print("\n--- CLEANING SUMMARY ---")
print(json.dumps(quality_report, indent=4))
print("\nCleaned dataset saved:", output_file)
