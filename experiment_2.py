"""
Experiment 2: Exploratory Data Analysis (EDA)

Topics:
- Loading the student dataset
- Dataset information
- Descriptive statistics
- Missing values
- Duplicate records
- Basic observations
"""

import pandas as pd


# Load the same dataset used in the EDA notebook
data_path = "/kaggle/input/student-classification-dataset/student.csv"
df = pd.read_csv(data_path)

# Remove unnecessary columns
df = df.drop(columns=["Unnamed: 0", "Id"])


# -------------------------------
# DISPLAY DATASET
# -------------------------------

print("STUDENT DATASET")
print(df)


# -------------------------------
# DATASET INFORMATION
# -------------------------------

print("\nDATASET INFORMATION")
df.info()


# -------------------------------
# DESCRIPTIVE STATISTICS
# -------------------------------

print("\nDESCRIPTIVE STATISTICS")
print(df.describe())


# -------------------------------
# MISSING VALUES
# -------------------------------

print("\nMISSING VALUES")
print(df.isnull().sum())


# -------------------------------
# DUPLICATE RECORDS
# -------------------------------

print("\nNUMBER OF DUPLICATE ROWS")
print(df.duplicated().sum())

print("\nDUPLICATE ROWS")
print(df[df.duplicated()])


# -------------------------------
# BASIC EDA OBSERVATIONS
# -------------------------------

print("\nBASIC OBSERVATIONS")

print(
    "AVERAGE STUDENT AGE:",
    df["Student_Age"].mean()
)

print(
    "AVERAGE WEEKLY STUDY HOURS:",
    df["Weekly_Study_Hours"].mean()
)

print(
    "HIGHEST WEEKLY STUDY HOURS:",
    df["Weekly_Study_Hours"].max()
)

print(
    "LOWEST WEEKLY STUDY HOURS:",
    df["Weekly_Study_Hours"].min()
)

print(
    "MOST COMMON HIGH SCHOOL TYPE:",
    df["High_School_Type"].mode()[0]
)

print(
    "MOST COMMON TRANSPORTATION:",
    df["Transportation"].mode()[0]
)
