# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:47:15 2025

@author: ftuha
"""

import pandas as pd

# Load dataset
from sklearn.datasets import fetch_openml

# Load airquality dataset (alternative synthetic version if needed)
try:
    airquality = fetch_openml(name="air-quality", version=1, as_frame=True).frame
except:
    import numpy as np
    np.random.seed(42)
    airquality = pd.DataFrame({
        "Ozone": np.random.choice([np.nan, 10, 20, 30, 40], size=100, p=[0.2, 0.2, 0.2, 0.2, 0.2]),
        "Solar.R": np.random.choice([np.nan, 100, 200, 300, 400], size=100, p=[0.1, 0.225, 0.225, 0.225, 0.225]),
        "Wind": np.random.choice([np.nan, 5, 10, 15, 20], size=100, p=[0.15, 0.2125, 0.2125, 0.2125, 0.2125]),
        "Temp": np.random.choice([np.nan, 60, 70, 80, 90], size=100, p=[0.05, 0.2375, 0.2375, 0.2375, 0.2375]),
        "Month": np.random.choice([5, 6, 7, 8, 9], size=100),
        "Day": np.arange(1, 101) % 31 + 1
    })

# Calculate proportion of missing values per column
missing_proportions = airquality.isnull().sum() / len(airquality)
print("Proportion of Missing Values:")
print(missing_proportions)
import missingno as msno
import matplotlib.pyplot as plt

# Visualizing missing values correlation
msno.heatmap(airquality)
plt.title("Missingness Correlation Heatmap")
plt.show()
