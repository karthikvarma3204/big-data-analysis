import dask.dataframe as dd  

# Load the large dataset
df = dd.read_csv("sales_data.csv")  

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Basic data summary
print("\nSummary Statistics:")
print(df.describe().compute())

# Count missing values
print("\nMissing Values:")
print(df.isnull().sum().compute())

# Group by 'Category' and calculate the average 'Sales'
category_sales_avg = df.groupby("Category")["Sales"].mean().compute()
print("\nAverage Sales by Category:")
print(category_sales_avg)

# Find the most popular category
popular_category = df["Category"].value_counts().compute()
print("\nTop Categories:")
print(popular_category)

# Save the processed data
df.to_csv("processed_sales_data.csv", single_file=True)
print("\nProcessed data saved as 'processed_sales_data.csv'.")
