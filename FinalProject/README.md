# Superstore Sales Data Analysis and Profit Prediction

## Overview
This project focuses on exploratory data analysis (EDA) and machine learning applied to a retail Superstore dataset.  
The goal is to analyze sales performance, identify key patterns in profitability, and build models to predict profit and classify whether a transaction is profitable.

---

## Objectives
- Analyze sales and profit distribution  
- Identify key drivers of profitability  
- Explore customer segments, regions, and product categories  
- Build predictive models for profit estimation  
- Classify transactions as profitable or non-profitable  

---

## Dataset
The dataset contains information about:
- Orders and sales  
- Product categories and subcategories  
- Customer segments  
- Regions  
- Discounts and profit  

---

## Tools & Technologies
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

---

## Data Preprocessing
- Handling missing values  
- Removing duplicates  
- Feature preparation and transformation  
- Encoding categorical variables  

---

## Exploratory Data Analysis
- Sales and profit distribution analysis  
- Category and subcategory performance  
- Regional and segment-based analysis  
- Discount vs profit relationship  
- Trend analysis  

---

## Machine Learning

### Regression
- Built models to predict profit value  
- Compared models using cross-validation  
- Evaluated using standard regression metrics  

### Classification
- Built models to classify transactions as:
  - profitable  
  - non-profitable  
- Evaluated model performance using classification metrics  

---

## Key Insights
- Profit and sales distributions are highly skewed, with extreme outliers on both profit and loss sides.
- Discount level is one of the most important drivers of profitability.
- High-loss transactions are associated with significantly higher discounts than high-profit transactions.
- Product category differences among high-profit orders were not statistically significant in the ANOVA test.
- Machine learning models showed strong predictive performance for both profit prediction and profitability classification. 

---

## Project Structure
```plaintext
FinalProject/
├── superstore.csv
├── descriptive.ipynb
├── classical.ipynb
├── machine.ipynb
├── main.ipynb
├── parse_data.ipynb
└── README.md
```
---

## Results
- Welch two-sample t-test showed a statistically significant difference in discount rates between high-profit and high-loss orders.
- One-way ANOVA did not show statistically significant sales differences across product categories among high-profit orders.
- The tuned Random Forest regression model achieved R² = 0.8607 and RMSE = 30.94 on the test set.
- The Random Forest classification model achieved Accuracy = 0.953 and ROC-AUC ≈ 0.988.
- The analysis suggests that discount control is the most actionable direction for improving profitability. 

---

## Future Improvements
- Hyperparameter tuning  
- Feature engineering improvements  
- Model comparison with advanced algorithms  
- Deployment as a simple dashboard or app  
