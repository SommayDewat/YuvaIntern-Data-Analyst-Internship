
from pathlib import Path
import seaborn as sns
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RESULTS_DIR = PROJECT_DIR / "results"

DATA_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

# Load the sample restaurant tips dataset
print("Loading dataset...")
df = sns.load_dataset("tips")

# Save a local CSV copy so the project can be reproduced
csv_path = DATA_DIR / "restaurant_tips.csv"
df.to_csv(csv_path, index=False)

print("\n--- DATASET OVERVIEW ---")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print("\nColumn names:")
print(df.columns.tolist())

print("\n--- FIRST 5 ROWS ---")
print(df.head().to_string(index=False))

print("\n--- DATA TYPES ---")
print(df.dtypes.to_string())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum().to_string())

print("\n--- DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- NUMERICAL SUMMARY ---")
print(df.describe().round(2).to_string())

# Save an inspection report
report_path = RESULTS_DIR / "dataset_inspection.txt"

with report_path.open("w", encoding="utf-8") as file:
    file.write("DATASET INSPECTION REPORT\n")
    file.write("=" * 40 + "\n")
    file.write(f"Rows: {df.shape[0]}\n")
    file.write(f"Columns: {df.shape[1]}\n\n")
    file.write("Data types:\n")
    file.write(df.dtypes.to_string())
    file.write("\n\nMissing values:\n")
    file.write(df.isnull().sum().to_string())
    file.write(f"\n\nDuplicate rows: {df.duplicated().sum()}\n")
    file.write("\nNumerical summary:\n")
    file.write(df.describe().round(2).to_string())

print(f"\nDataset saved to: {csv_path}")
print(f"Inspection report saved to: {report_path}")
print("\nDataset inspection completed successfully!")
