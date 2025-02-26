import pandas as pd
from pyampute.exploration.mcar_statistical_tests import MCARTest
import numpy as np


import matplotlib.pyplot as plt
import missingno as msno


# Create a sample dataset with missing values
np.random.seed(42)
airquality = pd.DataFrame({
    "Ozone": np.random.choice([np.nan, 10, 20, 30, 40], size=100, p=[0.2, 0.2, 0.2, 0.2, 0.2]),
    "Solar.R": np.random.choice([np.nan, 100, 200, 300, 400], size=100, p=[0.1, 0.225, 0.225, 0.225, 0.225]),
    "Wind": np.random.choice([np.nan, 5, 10, 15, 20], size=100, p=[0.15, 0.2125, 0.2125, 0.2125, 0.2125]),
    "Temp": np.random.choice([np.nan, 60, 70, 80, 90], size=100, p=[0.05, 0.2375, 0.2375, 0.2375, 0.2375]),
    "Month": np.random.choice([5, 6, 7, 8, 9], size=100),
    "Day": np.arange(1, 101) % 31 + 1
})

# Run Little's MCAR Test on DataFrame
mt = MCARTest(method="little")
p_value = mt.little_mcar_test(airquality)

print(p_value)


if p_value > 0.05:
    print("✅ Fail to reject null hypothesis: Missingness is MCAR (Missing Completely at Random).")
else:
    print("❌ Reject null hypothesis: Missingness is NOT MCAR (MAR or MNAR).")



# 🔍 Visualizing missing data patterns
plt.figure(figsize=(8, 5))
msno.matrix(airquality)
plt.title("Missing Data Matrix")
plt.show()

# 🔥 Heatmap to show missingness correlation
plt.figure(figsize=(8, 5))
msno.heatmap(airquality)
plt.title("Missing Data Correlation Heatmap")
plt.show()
