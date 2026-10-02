```python
"""
Experiment 3: Data Visualization using Matplotlib and Seaborn
Topics: Histogram, box plot, scatter plot, pair plot and correlation heatmap.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the student dataset
df = pd.read_csv("student.csv")

# Convert Grade into a numerical value for correlation
grade_values = {
    "AA": 4,
    "BA": 3.5,
    "BB": 3,
    "CB": 2.5,
    "CC": 2,
    "DC": 1.5,
    "DD": 1,
    "Fail": 0
}

df["Grade_Score"] = df["Grade"].map(grade_values)

# 1. Histogram
plt.figure(figsize=(7, 4))
plt.hist(df["Weekly_Study_Hours"], bins=6, edgecolor="black")
plt.title("Distribution of Weekly Study Hours")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Number of Students")
plt.show()

# 2. Box Plot
plt.figure(figsize=(7, 4))
sns.boxplot(y=df["Weekly_Study_Hours"])
plt.title("Box Plot of Weekly Study Hours")
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x="Weekly_Study_Hours", y="Student_Age")
plt.title("Weekly Study Hours vs Student Age")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Student Age")
plt.show()

# 4. Pair Plot
sns.pairplot(df[["Student_Age", "Weekly_Study_Hours", "Grade_Score"]])
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(7, 5))
corr = df[["Student_Age", "Weekly_Study_Hours", "Grade_Score"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
```
