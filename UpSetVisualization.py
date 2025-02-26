import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from upsetplot import UpSet

# Generate a sample dataset with missing values
np.random.seed(42)
data = pd.DataFrame({
    "EMA": [np.nan if x < 0.3 else 1 for x in np.random.rand(1000)],
    "LPN": [np.nan if x < 0.2 else 1 for x in np.random.rand(1000)],
    "HEFCE": [np.nan if x < 0.15 else 1 for x in np.random.rand(1000)],
    "Ethnicity": [np.nan if x < 0.1 else 1 for x in np.random.rand(1000)],
    "dropOUToriginal": [np.nan if x < 0.25 else 1 for x in np.random.rand(1000)]
})

# Convert missing values to a boolean representation
missing_matrix = data.isna()

# Convert DataFrame to a MultiIndex format required by UpSet
missing_counts = missing_matrix.groupby(missing_matrix.columns.tolist()).size()

# Generate UpSet plot
upset = UpSet(missing_counts, subset_size="count", show_percentages=True)
upset.plot()
plt.show()
