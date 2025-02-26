
# **Missing Data Analysis & Visualization**

This repository contains Python scripts for analyzing and visualizing **missing data** using various statistical methods and visualization techniques. It includes **MCAR tests, UpSet plots, heatmaps, and correlation matrices** to help understand the patterns of missing values in datasets.

## **Installation Requirements**
Before running any script, install the required dependencies using:
```bash
pip install pandas numpy matplotlib seaborn missingno upsetplot scikit-learn pyampute
```


## **📂 Files Overview**

### **1️⃣ LittlTestMCAR.py**
#### **Description:**
- 📊 **Performs Little's MCAR (Missing Completely at Random) test** to determine if missing values occur randomly in the dataset.
- 🔍 Uses `pyampute` to conduct **statistical testing** on missing data.
- 🎨 **Visualizes missing data patterns** using a **matrix plot** and a **heatmap**.

#### **Requirements:**
✅ `pandas` ✅ `numpy` ✅ `pyampute` ✅ `missingno` ✅ `matplotlib`

#### **Run the script:**
```bash
python LittlTestMCAR.py
```

### **2️⃣ missing_data_correlation.py**
#### **Description:**
- 📊 **Loads the air quality dataset** (or creates synthetic data if unavailable).
- 📏 **Calculates the proportion of missing values** for each feature.
- 🔥 **Visualizes missing values correlation** using `missingno.heatmap()`.

#### **Requirements:**
✅ `pandas` ✅ `numpy` ✅ `missingno` ✅ `matplotlib`

#### **Run the script:**
```bash
python missing_data_correlation.py
```
### **3️⃣ missing_data_heatmap.py**
#### **Description:**
- 📊 **Loads or generates** a dataset with missing values.
- 🎨 Uses `seaborn` to create a **heatmap** showing missing values distribution.
- 🔍 Helps **identify missing data patterns** visually.

#### **Requirements:**
✅ `pandas` ✅ `numpy` ✅ `matplotlib` ✅ `seaborn`

#### **Run the script:**
```bash
python missing_data_heatmap.py
```

### **4️⃣ UpSetVisualization.py**
#### **Description:**
- 📊 **Creates an UpSet plot** to visualize the **co-occurrence** of missing values.
- 🔄 **Converts missing values** into a **boolean matrix** for better pattern detection.
- 🖥 Uses `upsetplot` to generate **interactive missing data patterns**.

#### **Requirements:**
✅ `pandas` ✅ `numpy` ✅ `matplotlib` ✅ `upsetplot`

#### **Run the script:**
```bash
python UpSetVisualization.py
```

## ** Visualizations**
After running the scripts, you will see plots like:

### ** Missing Data Heatmap**
![Missing Data Heatmap](missing_data_heatmap.png)

### ** Missing Data Correlation**
![Missing Data Correlation](missing_data_correlation.png)

### ** UpSet Plot**
![UpSet Plot](upset_plot.png)


## **Requirements For the heatmap**
Install the required dependencies before running the script:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
