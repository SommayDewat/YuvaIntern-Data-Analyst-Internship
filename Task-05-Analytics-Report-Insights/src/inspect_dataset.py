
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Find the dataset
files = list(DATA_DIR.glob("*.csv"))

if not files:
    raise FileNotFoundError(
        "No CSV found. Place the Superstore CSV inside the data folder."
    )

DATA_FILE = files[0]

# Read CSV
df = pd.read_csv(DATA_FILE, encoding="latin1")

print("=" * 50)
print("SUPERSTORE DATASET INSPECTION")
print("=" * 50)

print("\nDataset file:", DATA_FILE.name)
print("\nShape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five records:")
print(df.head().to_string(index=False))

print("\nData types:")
print(df.dtypes.to_string())

print("\nMissing values:")
print(df.isnull().sum().to_string())

print("\nDuplicate records:", df.duplicated().sum())

print("\nNumerical summary:")
print(df.describe().round(2).to_string())

print("\nDataset inspection completed!")
