from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "SeoulBikeData.csv"

print("=" * 60)
print("TASK 3: REAL-WORLD DATASET INSPECTION")
print("=" * 60)

df = pd.read_csv(DATA_PATH, sep=",", encoding="cp1252")

print(f"\nFile: {DATA_PATH.name}")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nFIRST 5 ROWS")
print(df.head().to_string(index=False))

print("\nDATA TYPES")
print(df.dtypes.to_string())

print("\nMISSING VALUES")
print(df.isna().sum().to_string())

print(f"\nDuplicate rows: {df.duplicated().sum():,}")

print("\nNUMERICAL SUMMARY")
print(df.describe().round(2).to_string())

print("\nCATEGORICAL SUMMARY")
print(df.describe(include="object").to_string())

print("\nINSPECTION COMPLETE")
