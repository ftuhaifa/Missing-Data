
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

## ** Visualizations and Results**
After running the scripts, you will see results like:

## ** MCAR Test Result**
After running the **Little's MCAR test**, the obtained **p-value** is:

```bash
0.04679423596759624
### ❌ Reject null hypothesis: Missingness is NOT MCAR (MAR or MNAR).
```
### (MAR or MNAR) Means it could be Missing at random or missing not at random.

![image](https://github.com/user-attachments/assets/aa0c1cf3-d708-40ae-a573-c5ce44fe203f)


![image](https://github.com/user-attachments/assets/b9ec676d-905d-4db4-bef8-576fb1fc218b)




### ** Missing Data Heatmap**

<h5>Missing Data Heatmap</h5>

![image](https://github.com/user-attachments/assets/0cf7a6dd-49ca-4a3a-bb6b-91560c1510e3)



### ** Missing Data Correlation**

###
Proportion of Missing Values:

Ozone      0.28

Solar.R    0.09

Wind       0.15

Temp       0.08

Month      0.00

Day        0.00

dtype: float64

![image](https://github.com/user-attachments/assets/422a2ca1-30a9-47e3-b081-d93855448d6f)


### ** UpSet Plot**
 ![image](https://github.com/user-attachments/assets/397fb02b-24c2-474d-a3ad-8abc41ec26e0)



## **Requirements For the heatmap**
Install the required dependencies before running the script:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
