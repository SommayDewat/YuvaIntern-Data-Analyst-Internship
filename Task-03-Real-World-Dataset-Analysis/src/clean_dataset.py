from pathlib import Path
import json
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
DATA_PATH = BASE / "data" / "SeoulBikeData.csv"
RESULTS = BASE / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH, sep=",", encoding="cp1252")
original_rows = len(df)

# Standardize column names for easier Python use.
df.columns = [
    col.strip()
    .replace(" ", "_")
    .replace("(", "")
    .replace(")", "")
    .replace("/", "_")
    .replace("°C", "C")
    .replace("%", "pct")
    for col in df.columns
]

# Parse dates using the dataset's day/month/year format.
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y", errors="coerce")

numeric_cols = [
    "Rented_Bike_Count", "Hour", "TemperatureC", "Humiditypct",
    "Wind_speed_m_s", "Visibility_10m", "Dew_point_temperatureC",
    "Solar_Radiation_MJ_m2", "Rainfallmm", "Snowfall_cm"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Standardize categorical text.
for col in ["Seasons", "Holiday", "Functioning_Day"]:
    df[col] = df[col].astype("string").str.strip()

missing_before = int(df.isna().sum().sum())
duplicates_before = int(df.duplicated().sum())

# Validate domain constraints and expected categories.
invalid_checks = {
    "invalid_date": int(df["Date"].isna().sum()),
    "negative_rentals": int((df["Rented_Bike_Count"] < 0).sum()),
    "hour_out_of_range": int((~df["Hour"].between(0, 23)).sum()),
    "humidity_out_of_range": int((~df["Humiditypct"].between(0, 100)).sum()),
    "negative_wind_speed": int((df["Wind_speed_m_s"] < 0).sum()),
    "negative_rainfall": int((df["Rainfallmm"] < 0).sum()),
    "negative_snowfall": int((df["Snowfall_cm"] < 0).sum()),
    "unexpected_season": int((~df["Seasons"].isin(["Spring", "Summer", "Autumn", "Winter"])).sum()),
    "unexpected_holiday": int((~df["Holiday"].isin(["Holiday", "No Holiday"])).sum()),
    "unexpected_functioning_day": int((~df["Functioning_Day"].isin(["Yes", "No"])).sum()),
}

# Keep a separate flag for statistically unusual values; do not remove them blindly.
q1 = df["Rented_Bike_Count"].quantile(0.25)
q3 = df["Rented_Bike_Count"].quantile(0.75)
iqr = q3 - q1
outlier_low = q1 - 1.5 * iqr
outlier_high = q3 + 1.5 * iqr
outlier_count = int(
    ((df["Rented_Bike_Count"] < outlier_low) |
     (df["Rented_Bike_Count"] > outlier_high)).sum()
)

# This dataset should have one record per date and hour.
duplicate_date_hour = int(df.duplicated(subset=["Date", "Hour"]).sum())

# No rows are dropped silently. Fail clearly if required fields are invalid.
quality = {
    "source_file": "SeoulBikeData.csv",
    "source_rows": original_rows,
    "source_columns": 14,
    "missing_values_before_cleaning": missing_before,
    "exact_duplicate_rows_before_cleaning": duplicates_before,
    "duplicate_date_hour_keys": duplicate_date_hour,
    "domain_validation_issues": invalid_checks,
    "rental_count_iqr_outlier_fences": {
        "lower": round(float(outlier_low), 2),
        "upper": round(float(outlier_high), 2),
        "flagged_rows": outlier_count,
        "action": "Flagged for investigation; not removed automatically"
    },
    "cleaned_rows": int(len(df)),
    "missing_values_after_processing": int(df.isna().sum().sum()),
    "date_min": str(df["Date"].min().date()) if df["Date"].notna().any() else None,
    "date_max": str(df["Date"].max().date()) if df["Date"].notna().any() else None,
    "notes": [
        "Original source CSV was not modified.",
        "Dates parsed using day/month/year format.",
        "Outliers were flagged, not automatically removed."
    ]
}

df.to_csv(RESULTS / "cleaned_seoul_bike_data.csv", index=False)
with open(RESULTS / "data_quality_report.json", "w", encoding="utf-8") as f:
    json.dump(quality, f, indent=2, ensure_ascii=False)

print("DATA CLEANING AND QUALITY CHECK COMPLETE")
print(f"Rows retained: {len(df):,} / {original_rows:,}")
print(f"Missing values before: {missing_before}")
print(f"Exact duplicate rows: {duplicates_before}")
print(f"Duplicate date-hour keys: {duplicate_date_hour}")
print("\nDomain validation checks:")
for name, count in invalid_checks.items():
    print(f"  {name}: {count}")
print(f"\nRental-count outlier flags (IQR): {outlier_count}")
print(f"Cleaned data: {RESULTS / 'cleaned_seoul_bike_data.csv'}")
print(f"Quality report: {RESULTS / 'data_quality_report.json'}")
