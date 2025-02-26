# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
import sys

# Load dataset (or create synthetic data)
try:
    airquality = fetch_openml(name="air-quality", version=1, as_frame=True).frame
except:
    np.random.seed(42)
    airquality = pd.DataFrame({
        "Ozone": np.random.choice([np.nan, 10, 20, 30, 40], size=100, p=[0.2, 0.2, 0.2, 0.2, 0.2]),
        "Solar.R": np.random.choice([np.nan, 100, 200, 300, 400], size=100, p=[0.1, 0.225, 0.225, 0.225, 0.225]),
        "Wind": np.random.choice([np.nan, 5, 10, 15, 20], size=100, p=[0.15, 0.2125, 0.2125, 0.2125, 0.2125]),
        "Temp": np.random.choice([np.nan, 60, 70, 80, 90], size=100, p=[0.05, 0.2375, 0.2375, 0.2375, 0.2375]),
        "Month": np.random.choice([5, 6, 7, 8, 9], size=100),
        "Day": np.arange(1, 101) % 31 + 1
    })

# Calculate missing value statistics
missing_counts = airquality.isnull().sum()  # Number of missing values per variable
total_rows = len(airquality)  # Total number of rows
missing_proportions = missing_counts / total_rows  # Proportion of missing values

# Create a formatted table
missing_summary = pd.DataFrame({
    "Variable": missing_counts.index,
    "nmiss": missing_counts.values,  # Number of missing values
    "n": total_rows,  # Total observations per variable
    "propmiss": missing_proportions.values  # Proportion of missing values
})

# Sort by proportion of missing values (descending)
missing_summary = missing_summary.sort_values(by="propmiss", ascending=False)

# Print table
print("\033[1;34mProportions of Missingness Per Variable in a Table\033[0m")  # Blue colored title
print(missing_summary.to_string(index=False, justify='left'))  # Print without index

# Display the table using Matplotlib (Styled like the Image)
plt.figure(figsize=(8, 5))
plt.axis("off")  # Remove axes
plt.table(cellText=missing_summary.values, colLabels=missing_summary.columns, loc="center", cellLoc="center")

plt.title("Proportions of Missingness Per Variable", fontsize=14, fontweight="bold", color="blue")
plt.show()


# Calculate proportions of missing values per variable
missing_proportions = airquality.isnull().sum() / len(airquality)

# Sort variables by missingness (descending)
missing_proportions = missing_proportions.sort_values(ascending=True)

# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(missing_proportions.index, missing_proportions.values, color='red', edgecolor='black')
plt.xlabel("Proportion of Missing Values")
plt.ylabel("Variables")
plt.title("Proportions of Missingness Per Variable")
plt.xlim(0, 1)  # Set x-axis limit from 0 to 1
plt.show()
