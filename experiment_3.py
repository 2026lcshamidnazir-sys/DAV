"""
Experiment 3: Data Visualization using Matplotlib and Seaborn

Topics:
- Histogram
- Box plot
- Scatter plot
- Pair plot
- Correlation heatmap
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the student dataset
data_path = "student.csv"
df = pd.read_csv(data_path)

# Remove unnecessary columns
df = df.drop(columns=["Unnamed: 0", "Id"])


# -------------------------------
# CONVERT GRADE TO NUMERICAL VALUE
# -------------------------------

grade_values = {
    "AA": 1.000,
    "BA": 0.875,
    "BB": 0.750,
    "CB": 0.625,
    "CC": 0.500,
    "DC": 0.375,
    "DD": 0.250,
    "Fail": 0.000
}

df["Grade_Score"] = df["Grade"].map(grade_values)


# -------------------------------
# 1. HISTOGRAM
# -------------------------------

plt.figure(figsize=(7, 4))

plt.hist(
    df["Student_Age"],
    bins=5,
    edgecolor="black"
)

plt.title("Distribution of Student Age")
plt.xlabel("Student Age")
plt.ylabel("Number of Students")

plt.show()


# -------------------------------
# 2. BOX PLOT
# -------------------------------

plt.figure(figsize=(7, 4))

sns.boxplot(
    y=df["Weekly_Study_Hours"]
)

plt.title("Box Plot of Weekly Study Hours")
plt.ylabel("Weekly Study Hours")

plt.show()


# -------------------------------
# 3. SCATTER PLOT
# -------------------------------

plt.figure(figsize=(7, 4))

sns.scatterplot(
    data=df,
    x="Weekly_Study_Hours",
    y="Grade_Score"
)

plt.title("Weekly Study Hours vs Grade Score")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Grade Score")

plt.show()


# -------------------------------
# 4. PAIR PLOT
# -------------------------------

sns.pairplot(
    df[
        [
            "Student_Age",
            "Weekly_Study_Hours",
            "Grade_Score"
        ]
    ]
)

plt.show()


# -------------------------------
# 5. CORRELATION HEATMAP
# -------------------------------

plt.figure(figsize=(7, 5))

correlation = df[
    [
        "Student_Age",
        "Weekly_Study_Hours",
        "Grade_Score"
    ]
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="crest",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.show()
