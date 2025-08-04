# Cybersecurity Threats Modeling

This project predicts multiple cybersecurity-related targets using machine learning:

## Tasks

- Predict Attack Type
- Predict Security Vulnerability Type
- Predict Defense Mechanism Used
- Predict Financial Loss (regression)
- Predict Incident Resolution Time (regression)

## Structure

- `data/`: Dataset (CSV)
- `models/`: Trained models
- `src/`: Preprocessing, training, config
- `notebooks/`: Jupyter exploration

## How to Run

1. Train all models:
```bash
python src/train_model.py



## Summary

 Step  Task

1. Set up project folder
2. Create virtual environment
3. Load and inspect CSV
4. Preprocess with LabelEncoder
5. Train and save RandomForest model
6. Use `main.py` to test prediction on new data



## Significance of Cells in Notebook "exploratory_analysis.ipynb"

Cell 1: Imports
-Pandas: for loading and manipulating tabular data.
-Matplotlib & Seaborn: for visual exploration.
-sns.set(...): applies a clean visual style across plots.

Cell 2: Load Dataset
-Loads your dataset into a DataFrame.
-Displays the first few rows to verify the structure, columns, and sample records.

Cell 3: Data Overview
-Shape: shows number of rows and columns.
-dtypes: confirms which columns are numeric vs categorical.
-Missing values: identifies any gaps or NaNs to address.

Cell 4: Target Columns Summary
-Counts the distributions of each classification target, which informs class balance.
-Uses describe() on regression targets to show mean, min, max, quartiles—so you can check for scale and outliers.

Cell 5: Visualize Categorical Target Distributions
-Creates bar charts for each classification target.
-Helps visualize whether classes are imbalanced.
-Useful for planning strategies like over/undersampling.

Cell 6: Visualize Regression Target Distributions
-Generates histograms with KDE curves for numeric targets.
-Reveals distribution shape, skewness, and presence of extreme values.

Cell 8: Grouped Insights
-First plot: Average financial loss grouped by attack type—shows which attacks are costliest.
-Second plot: Average resolution time by defense mechanism—highlights which defenses speed up incident recovery.

 Why It Matters
-Quality control: Validates data completeness and consistency.
-Imbalance detection: Shows if certain classes dominate, which affects model choice.
-Distribution awareness: Clarifies numeric target ranges and need for normalization or transformation.
-Feature insights: Reveals patterns—helps in feature engineering and modeling strategy.