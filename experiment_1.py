```python
import numpy as np
import pandas as pd

# Load student dataset
df = pd.read_csv("student.csv")

# NumPy Array
study_hours = np.array(df["Weekly_Study_Hours"])

print("NUMPY ARRAY")
print("Weekly Study Hours:", study_hours)
print("Mean Study Hours:", np.mean(study_hours))
print("Maximum Study Hours:", np.max(study_hours))
print("Minimum Study Hours:", np.min(study_hours))
print("First three values:", study_hours[:3])
print("Last three values:", study_hours[-3:])

# Pandas DataFrame
print("\nPANDAS DATAFRAME")
print(df[["Student_Age", "Sex", "Weekly_Study_Hours", "Attendance", "Grade"]])

print("\nFirst 3 rows:")
print(df.iloc[:3])

print("\nStudent Age column:")
print(df["Student_Age"])

print("\nStudents with more than 5 weekly study hours:")
print(df[df["Weekly_Study_Hours"] > 5])

print("\nFirst 2 rows and first 2 columns:")
print(df.iloc[:2, :2])
```
