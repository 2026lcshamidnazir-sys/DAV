```python
"""
Experiment 2: Exploratory Data Analysis (EDA)
Topics: Loading a dataset, descriptive statistics,
missing values and duplicate records.
"""

import pandas as pd

# Load the student dataset
df = pd.read_csv("student.csv")

print("STUDENT DATASET")
print(df)

# Basic information
print("\nDATASET INFORMATION")
print(df.info())

# Descriptive statistics
print("\nDESCRIPTIVE STATISTICS")
print(df.describe())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Check duplicate rows
print("\nNUMBER OF DUPLICATES")
print(df.duplicated().sum())

# Display duplicate rows
print("\nDUPLICATE ROWS")
print(df[df.duplicated()])

# Basic EDA observations
print("\nAVERAGE AGE:", df["Student_Age"].mean())
print("HIGHEST STUDY HOURS:", df["Weekly_Study_Hours"].max())
print("LOWEST STUDY HOURS:", df["Weekly_Study_Hours"].min())
```
