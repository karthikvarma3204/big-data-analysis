"""Explore the bundled sample sales dataset with Dask."""
from pathlib import Path
import dask.dataframe as dd

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "sales_data_sample (1).csv"
OUTPUT = ROOT / "processed_sales_data.csv"

def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Missing data file: {SOURCE}")
    df = dd.read_csv(str(SOURCE))
    print("First five rows:\n", df.head())
    print("\nSummary statistics:\n", df.describe().compute())
    print("\nMissing values:\n", df.isnull().sum().compute())
    print("\nAverage sales by category:\n", df.groupby("Category")["Sales"].mean().compute())
    print("\nCategory counts:\n", df["Category"].value_counts().compute())
    df.to_csv(str(OUTPUT), single_file=True, index=False)
    print(f"\nSaved processed data to {OUTPUT}")

if __name__ == "__main__":
    main()
