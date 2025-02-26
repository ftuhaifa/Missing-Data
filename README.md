# **Missing Data Visualization using a Heatmap**

This repository contains a Python script that **visualizes missing data**. The heatmap helps to identify patterns of missing values across different features.

## **Features**
- 📊 **Loads the air quality dataset** from `fetch_openml()`, or generates a synthetic dataset if unavailable.
- 🔍 **Identifies missing values** and converts them into a boolean matrix.
- 🎨 **Visualizes missing data** using `seaborn`'s **heatmap**, where missing values are represented in black.
- 🛠 **Easily customizable** for other datasets by modifying column names and probabilities.

## **Requirements For the heatmap**
Install the required dependencies before running the script:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
