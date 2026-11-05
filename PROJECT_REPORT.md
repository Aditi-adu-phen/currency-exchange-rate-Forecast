# Project Report
# Currency Exchange Rate Forecast Using Machine Learning

## 1. Introduction

Currency exchange rates are important in international trade, financial transactions, investments, and economic activities. Exchange rates fluctuate due to several factors, including market demand, inflation, interest rates, and global economic conditions.

Machine learning techniques can be applied to historical financial data to identify patterns and estimate numerical values.

This project explores the use of Decision Tree Regression for analyzing historical USD-INR exchange rate data and estimating closing exchange rates.

## 2. Abstract

The objective of this project is to develop a machine learning-based approach for analyzing historical currency exchange rate data.

The implementation uses Python to collect and process historical USD-INR data. Historical observations are transformed into time-based features, which are used to train a Decision Tree Regression model.

The model generates closing exchange rate estimates and is evaluated using regression metrics such as Mean Absolute Error, Mean Squared Error, Root Mean Squared Error, and R-squared.

The project demonstrates the application of supervised machine learning and data analysis techniques to historical financial data.

## 3. Problem Statement

Currency exchange rates change continuously due to economic conditions and market-related factors. Understanding historical movements and estimating future values can be challenging.

This project aims to explore how historical exchange rate observations can be processed and used to train a machine learning model for estimating closing exchange rate values.

## 4. Objectives

- Collect historical USD-INR exchange rate data.
- Perform data preprocessing and analysis.
- Create historical features from previous trading observations.
- Implement a Decision Tree Regression model.
- Train the model using historical data.
- Generate closing exchange rate estimates.
- Evaluate model performance using regression metrics.
- Visualize historical and predicted exchange rate values.

## 5. Dataset Description

The implementation uses historical USD-INR exchange rate observations.

The dataset can include the following attributes:

| Attribute | Description |
|---|---|
| Date | Date of the observation |
| Open | Opening exchange rate |
| High | Highest exchange rate |
| Low | Lowest exchange rate |
| Close | Closing exchange rate |
| Adj Close | Adjusted closing value, if available |
| Volume | Trading volume, if available |

The original college project used a dataset named `INR.csv`. The recreated implementation downloads historical data through the `yfinance` library and stores it in `dataset/usd_inr.csv`.

## 6. Technologies and Tools

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data processing and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Machine learning and model evaluation |
| yfinance | Historical market data retrieval |
| Joblib | Saving the trained model |

## 7. Algorithm

### Decision Tree Regression

Decision Tree Regression is a supervised learning algorithm used for predicting continuous numerical values.

The algorithm learns decision rules by splitting the training data based on feature conditions. These rules are used to estimate values for unseen observations.

In this project, the Decision Tree Regressor uses historical exchange rate features to estimate the closing exchange rate.

## 8. Methodology

### 8.1 Data Collection

Historical USD-INR exchange rate data is downloaded using the `yfinance` Python library.

### 8.2 Data Preprocessing

The downloaded dataset is loaded using Pandas, sorted chronologically, and prepared for feature engineering.

### 8.3 Feature Engineering

The implementation creates features from previous trading observations, including previous Open, High, Low, and Close values, earlier closing values, and a five-day moving average.

The current observation's Close value is used as the prediction target.

### 8.4 Train-Test Split

The prepared dataset is divided chronologically:

- 80% of the observations for training.
- 20% of the observations for testing.

This preserves the time order of the observations.

### 8.5 Model Training

A Decision Tree Regressor is trained using the historical features and corresponding closing exchange rate values.

### 8.6 Prediction

The trained model generates closing exchange rate estimates for the test dataset.

### 8.7 Model Evaluation

The model calculates the following evaluation metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

### 8.8 Visualization

Matplotlib is used to generate visualizations of historical exchange rate movements and actual versus predicted closing values.

## 9. Model Evaluation Metrics

| Metric | Explanation |
|---|---|
| MAE | Average absolute difference between actual and predicted values. |
| MSE | Average squared difference between actual and predicted values. |
| RMSE | Square root of MSE, expressed in the target variable's unit. |
| R² Score | Measures how well the model explains the variation in the target values. |

The actual metric values are produced by executing the implementation. No performance figures are assumed or reported without execution.

## 10. Expected Results

The implementation is designed to produce:

- Historical exchange rate visualization.
- Actual versus predicted exchange rate visualization.
- Model evaluation metrics.
- Predicted closing exchange rate values.
- A saved Decision Tree Regression model.
- A next-observation exchange rate estimate.

These outputs are generated by the Python scripts when executed successfully.

## 11. Applications

The project demonstrates concepts that are relevant to:

- Historical financial data analysis.
- Currency exchange rate trend analysis.
- Machine learning-based regression.
- Time-based feature engineering.
- Financial data visualization.

The estimates are for educational demonstration and are not intended for financial decision-making.

## 12. Limitations

- Exchange rates are affected by many external economic and market factors.
- The implementation uses a limited set of historical features.
- Decision Tree Regression may not capture every time-series pattern.
- Model performance depends on the dataset and selected parameters.
- Predictions are estimates and are not guaranteed to match actual market movements.

## 13. Future Enhancements

- Compare Decision Tree Regression with Random Forest and other algorithms.
- Explore advanced time-series forecasting methods.
- Include additional economic indicators.
- Extend the project to multiple currency pairs.
- Perform hyperparameter tuning.
- Develop a web-based interface for displaying predictions.

## 14. Conclusion

This project demonstrates how machine learning can be applied to historical currency exchange rate data.

By using Decision Tree Regression, historical exchange rate features can be used to estimate closing values. The implementation provides practical exposure to data collection, preprocessing, feature engineering, model training, evaluation, and visualization using Python.

## 15. Author

**Aditi Balakrishnan**

## 16. Recreation Note

This report describes a recreated GitHub implementation based on the original college project topic and previously documented project details. The original college-project source files and verified original results were not available for direct reproduction. Therefore, the code and outputs in this repository should be understood as a recreated implementation rather than the original submission.
