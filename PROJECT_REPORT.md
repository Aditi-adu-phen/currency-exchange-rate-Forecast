# Project Report
## Currency Exchange Rate Forecast Using Machine Learning

### 1. Introduction

Foreign exchange rates represent the value of one currency in relation to another. The INR-USD exchange rate indicates the value of the Indian Rupee relative to the United States Dollar. Exchange rate movements are influenced by economic conditions, financial markets, international trade, and global events.

Machine learning techniques can be applied to historical exchange rate data to identify patterns and estimate subsequent exchange rate values.

### 2. Abstract

This project explores the use of machine learning for INR-USD exchange rate forecasting. Historical exchange rate data is analyzed using Python, and a Decision Tree Regression algorithm is used to estimate closing exchange rate values. Data preprocessing, feature engineering, model training, evaluation, and visualization form the main stages of the implementation.

### 3. Problem Statement

Exchange rates fluctuate over time, making it challenging to estimate future currency values. The project addresses this challenge by applying a regression-based machine learning approach to historical exchange rate observations.

### 4. Objectives

- Study historical INR-USD exchange rate movements.
- Analyze the relationships among market attributes.
- Prepare historical data for machine learning.
- Apply Decision Tree Regression.
- Estimate subsequent closing exchange rate values.
- Evaluate model performance.

### 5. Dataset

The original project used a dataset named INR.csv containing Date, Open, High, Low, Close, Adjusted Close, and Volume fields.

The recreated implementation obtains historical USD-INR observations from an external financial data source and stores the required fields in a CSV file.

### 6. Tools and Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

### 7. Algorithm

Decision Tree Regression is a supervised learning technique that predicts continuous numerical values by learning decision rules from input features.

It is used to estimate exchange rate closing values based on historical market observations.

### 8. Methodology

1. Collect historical exchange rate data.
2. Load and inspect the dataset.
3. Clean incomplete records.
4. Explore exchange rate trends.
5. Prepare historical input features.
6. Divide observations into training and testing sets in chronological order.
7. Train a Decision Tree Regression model.
8. Generate predictions.
9. Evaluate predictions using regression metrics.
10. Visualize the results.

### 9. Evaluation

The implementation calculates Mean Absolute Error, Mean Squared Error, Root Mean Squared Error, and R-squared. Actual metric values are produced when the model is executed.

### 10. Expected Outcome

The implementation is designed to provide historical exchange rate visualizations, actual-versus-predicted comparisons, evaluation metrics, and an estimate for the next available trading observation.

### 11. Conclusion

The project demonstrates how machine learning regression techniques can be used to study historical currency exchange rate data and estimate subsequent exchange rate values. It provides practical experience in Python programming, data analysis, feature engineering, regression modelling, and visualization.

### 12. Future Scope

The project can be extended by comparing multiple regression algorithms, incorporating economic indicators, applying advanced time-series forecasting techniques, and developing a web-based interface for displaying forecasts.

### 13. Disclaimer

This project is for educational purposes only. The generated estimates are not guaranteed exchange rates and should not be used as financial advice.
