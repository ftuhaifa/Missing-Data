
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


## **2️⃣ Proportions_Of_Missing_Values_Per_Variable.py**
#### **Description:**
- 📊 **Calculates missing value statistics** (number, proportion, and total observations per variable).
- 📄 **Displays a formatted table** showing missing data statistics in a **structured and readable** format.
- 🎨 **Visualizes missing data proportions** using:
  - A **styled table** in `Matplotlib`, formatted like a report.
  - A **horizontal bar chart** to show missing value proportions for each variable.

#### **Requirements:**
✅ `pandas` ✅ `numpy` ✅ `matplotlib` ✅ `seaborn` ✅ `sklearn`

#### **Run the script:**
```bash
python Proportions_Of_Missing_Values_Per_Variable.py
```

### **3️⃣ missing_data_correlation.py**
#### **Description:**
- 📊 **Creates synthetic data** 
- 📏 **Calculates the proportion of missing values** for each feature.
- 🔥 **Visualizes missing values correlation** using `missingno.heatmap()`.

#### **Requirements:**
✅ `pandas` ✅ `numpy` ✅ `missingno` ✅ `matplotlib`

#### **Run the script:**
```bash
python missing_data_correlation.py
```
### **4️⃣ missing_data_heatmap.py**
#### **Description:**
- 📊 **Generates** a dataset with missing values.
- 🎨 Uses `seaborn` to create a **heatmap** showing missing values distribution.
- 🔍 Helps **identify missing data patterns** visually.

#### **Requirements:**
✅ `pandas` ✅ `numpy` ✅ `matplotlib` ✅ `seaborn`

#### **Run the script:**
```bash
python missing_data_heatmap.py
```

### **5️⃣ UpSetVisualization.py**
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

## **Visualizations and Results**
After running the scripts, you will see results like:

## **MCAR Test Result**
After running the **Little's MCAR test**, the obtained **p-value** is:

```bash
0.04679423596759624
### ❌ Reject null hypothesis: Missingness is NOT MCAR (MAR or MNAR).
```
### (MAR or MNAR) Means it could be Missing at random or missing not at random.

![image](https://github.com/user-attachments/assets/aa0c1cf3-d708-40ae-a573-c5ce44fe203f)


![image](https://github.com/user-attachments/assets/b9ec676d-905d-4db4-bef8-576fb1fc218b)




<h1>Proportions Of Missing Values Per Variable</h1>

```bash
Proportions of Missingness Per Variable in a Table
Variable  nmiss  n   propmiss
  Ozone  28     100 0.28     
   Wind  15     100 0.15     
Solar.R   9     100 0.09     
   Temp   8     100 0.08     
  Month   0     100 0.00     
    Day   0     100 0.00 
```

![image](https://github.com/user-attachments/assets/e52ad0ad-a754-4e96-8b6b-5082821aa642)




![image](https://github.com/user-attachments/assets/5fe1ed2b-d54e-4234-9fd6-3d7509b5cce0)


<h1>Missing Data Heatmap</h1>

![image](https://github.com/user-attachments/assets/0cf7a6dd-49ca-4a3a-bb6b-91560c1510e3)





<h1> Missing Data Correlation</h1>

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




<h1>UpSet Plot</h1>

 ![image](https://github.com/user-attachments/assets/397fb02b-24c2-474d-a3ad-8abc41ec26e0)




## **Requirements For the heatmap**
Install the required dependencies before running the script:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
