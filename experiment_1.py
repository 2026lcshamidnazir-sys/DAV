import numpy as np
import pandas as pd

# Load the student dataset
data_path = "student.csv"
df = pd.read_csv(data_path)

# Remove unnecessary index columns
df = df.drop(columns=["Unnamed: 0", "Id"])

# -------------------------------
# NUMPY ARRAY
# -------------------------------

study_hours = np.array(df["Weekly_Study_Hours"])

print("NUMPY ARRAY")
print("Weekly Study Hours:", study_hours)

print("Mean Study Hours:", np.mean(study_hours))
print("Maximum Study Hours:", np.max(study_hours))
print("Minimum Study Hours:", np.min(study_hours))

print("First four study-hour values:", study_hours[:4])
print("Last three study-hour values:", study_hours[-3:])


# -------------------------------
# PANDAS DATAFRAME
# -------------------------------

print("\nPANDAS DATAFRAME")
print(df)

# First 4 rows
print("\nFirst 4 rows:")
print(df.iloc[:4])

# Student Age column
print("\nStudent Age column:")
print(df["Student_Age"])

# Students studying more than 6 hours
print("\nStudents with more than 6 weekly study hours:")
print(df[df["Weekly_Study_Hours"] > 6])

# First 3 rows and first 3 columns
print("\nFirst 3 rows and first 3 columns:")
print(df.iloc[:3, :3])
