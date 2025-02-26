import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the airquality dataset (similar to R's dataset)
from sklearn.datasets import fetch_openml

# Load dataset (if available) or use an alternative
try:
    airquality = fetch_openml(name="air-quality", version=1, as_frame=True).frame
except:
    # Creating a synthetic dataset similar to airquality
    np.random.seed(42)
    airquality = pd.DataFrame({
        "Ozone": np.random.choice([np.nan, 10, 20, 30, 40], size=100, p=[0.2, 0.2, 0.2, 0.2, 0.2]),
        "Solar.R": np.random.choice([np.nan, 100, 200, 300, 400], size=100, p=[0.1, 0.225, 0.225, 0.225, 0.225]),
        "Wind": np.random.choice([np.nan, 5, 10, 15, 20], size=100, p=[0.15, 0.2125, 0.2125, 0.2125, 0.2125]),
        "Temp": np.random.choice([np.nan, 60, 70, 80, 90], size=100, p=[0.05, 0.2375, 0.2375, 0.2375, 0.2375]),
        "Month": np.random.choice([5, 6, 7, 8, 9], size=100),
        "Day": np.arange(1, 101) % 31 + 1
    })

# Plot missing data heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(airquality.isnull(), cmap=["yellow", "black"], cbar=True, yticklabels=False)
plt.title("Missing Data Heatmap")
plt.xlabel("Features")
plt.ylabel("Samples")
plt.show()
