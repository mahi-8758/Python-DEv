import numpy as np
import pandas as pd

print("=" * 50)
print("DATA ANALYSIS USING NUMPY AND PANDAS")
print("=" * 50)

print("\n1. NUMPY ANALYSIS")
print("-" * 50)

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(f"Data: {data}")
print(f"Mean: {np.mean(data)}")
print(f"Median: {np.median(data)}")
print(f"Std Dev: {np.std(data)}")
print(f"Min: {np.min(data)}")
print(f"Max: {np.max(data)}")
print(f"Sum: {np.sum(data)}")

print("\n2. PANDAS DATA ANALYSIS")
print("-" * 50)

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 28],
    'Salary': [50000, 60000, 75000, 80000, 55000],
    'Department': ['HR', 'IT', 'Sales', 'IT', 'HR']
})

print("\nDataFrame:")
print(df)

print(f"\nDataFrame Shape: {df.shape}")
print(f"\nDataFrame Info:")
print(df.info())

print(f"\nBasic Statistics:")
print(df.describe())

print(f"\nGroupBy Department:")
print(df.groupby('Department')['Salary'].mean())

print(f"\nSorting by Salary:")
print(df.sort_values('Salary', ascending=False))

print("\n" + "=" * 50)