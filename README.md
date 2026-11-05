# Currency Exchange Rate Forecast Using Machine Learning

## 1. Project Overview

Currency exchange rates play an important role in international trade, financial transactions, investments, and global economic activities. Exchange rates fluctuate due to several economic and market-related factors, making their future movements difficult to estimate.

This project focuses on analyzing historical exchange rate data between the Indian Rupee (INR) and the United States Dollar (USD) using machine learning techniques. A Decision Tree Regression algorithm is used to learn patterns from historical market data and estimate exchange rate values.

The project uses Python libraries for data processing, analysis, visualization, model development, and prediction.

## 2. Abstract

Currency exchange rate forecasting is an important application of data analysis and machine learning. Changes in exchange rates can influence international business, imports, exports, investments, and financial planning.

The objective of this project is to develop a machine learning-based approach for analyzing and estimating INR-USD exchange rate values using historical currency data. Historical market attributes are processed and analyzed to identify patterns and relationships between exchange rate variables.

A Decision Tree Regression algorithm is applied to build the prediction model. Python libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn are used for data manipulation, exploratory data analysis, visualization, model training, and evaluation.

The project demonstrates how machine learning regression techniques can be applied to historical financial data to estimate currency exchange rate values.

## 3. Problem Statement

Currency exchange rates are constantly changing due to economic conditions, market demand, international trade, inflation, interest rates, and other financial factors.

Manually estimating exchange rate movements can be difficult because of the large amount of historical data and changing market conditions.

This project aims to analyze historical INR-USD exchange rate data and develop a machine learning model that uses relevant market attributes to estimate closing exchange rate values.

## 4. Objectives

- To collect and analyze historical INR-USD exchange rate data.
- To understand exchange rate trends and patterns.
- To perform data preprocessing and exploratory data analysis.
- To identify relevant input features for machine learning.
- To develop a Decision Tree Regression model.
- To estimate exchange rate closing values.
- To evaluate the model using regression evaluation metrics.
- To visualize historical data and prediction results.

## 5. Dataset Description

The project uses historical INR-USD exchange rate data.

The dataset contains the following attributes:

| Attribute | Description |
|---|---|
| Date | Date of the exchange rate observation |
| Open | Opening exchange rate |
| High | Highest exchange rate |
| Low | Lowest exchange rate |
| Close | Closing exchange rate |
| Adj Close | Adjusted closing value, if available |
| Volume | Trading volume, if available |

The original project dataset was named `INR.csv`.

For this recreated GitHub implementation, a compatible historical dataset can be downloaded separately using the data collection script.

## 6. Technologies Used

- **Python:** Main programming language.
- **NumPy:** Numerical operations.
- **Pandas:** Dataset loading and manipulation.
- **Matplotlib:** Data visualization.
- **Seaborn:** Statistical visualization and correlation analysis.
- **Scikit-learn:** Machine learning model development and evaluation.

## 7. Algorithm Used

### Decision Tree Regression

Decision Tree Regression is a supervised machine learning algorithm used to predict continuous numerical values.

It works by dividing data into smaller groups based on feature conditions and learning decision rules from the training data.

In this project, the algorithm learns relationships between historical exchange rate attributes and closing exchange rate values.

**Advantages:**
- Easy to understand and implement.
- Can model nonlinear relationships.
- Requires relatively little data preprocessing.
- Suitable for regression problems.

## 8. Methodology

### Step 1: Data Collection
Historical INR-USD exchange rate data is collected from a financial data source.

### Step 2: Data Preprocessing
The dataset is loaded using Pandas and inspected for missing values, invalid records, and data consistency.

### Step 3: Exploratory Data Analysis
Historical closing exchange rates are visualized using Matplotlib. Correlation analysis is used to understand relationships between numerical attributes.

### Step 4: Feature Selection
The original implementation uses Open, High, and Low as input features and Close as the target variable.

### Step 5: Train-Test Split
The dataset is divided into training and testing subsets to evaluate the model on unseen observations.

### Step 6: Model Development
A Decision Tree Regressor is selected to estimate continuous exchange rate values.

### Step 7: Model Training
The model learns patterns from the training dataset.

### Step 8: Prediction
The trained model generates estimated closing exchange rate values for the test data.

### Step 9: Model Evaluation
Regression evaluation metrics such as MAE, MSE, RMSE, and R-squared can be used to measure model performance.

### Step 10: Visualization
Graphs are used to examine historical exchange rate trends and compare actual and estimated values.

## 9. Model Evaluation

The following metrics are used in the recreated implementation:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted values.
- **Mean Squared Error (MSE):** Measures the average squared prediction error.
- **Root Mean Squared Error (RMSE):** Measures prediction error in the original exchange rate unit.
- **R-squared (R²):** Indicates how well the model explains variation in the target values.

Actual evaluation values should be generated by running the Python implementation. No unverified accuracy or performance values are reported here.

## 10. Expected Outputs

The implementation is designed to generate:

- Historical exchange rate graph.
- Correlation heatmap.
- Actual versus predicted exchange rate graph.
- Model evaluation metrics.
- Predicted exchange rate values.

## 11. Conclusion

This project demonstrates the application of machine learning techniques to historical currency exchange rate analysis. By using a Decision Tree Regression algorithm, the project explores how historical market attributes can be used to estimate closing exchange rate values.

The project provides practical exposure to data preprocessing, exploratory data analysis, feature selection, regression modelling, prediction, and visualization using Python.

## 12. Future Enhancements

- Compare Decision Tree Regression with Random Forest and other regression algorithms.
- Explore advanced time-series forecasting techniques.
- Include additional economic and financial indicators.
- Extend the analysis to other currency pairs.
- Improve model performance through hyperparameter tuning.
- Develop a simple web application to display exchange rate estimates.

## 13. Project Structure

```text
currency-exchange-rate-forecast/
│
├── dataset/
├── src/
│   ├── fetch_data.py
│   └── train_model.py
├── outputs/
├── images/
├── README.md
├── PROJECT_REPORT.md
├── requirements.txt
└── .gitignore
```

## 14. How to Run

Install the dependencies:

```bash
pip install -r requirements.txt
```

Download historical data:

```bash
python src/fetch_data.py
```

Train and evaluate the model:

```bash
python src/train_model.py
```

## 15. Author

**Aditi Balakrishnan**

## 16. Disclaimer

This project is intended for educational and portfolio purposes only. Exchange rate estimates are not guaranteed and should not be considered financial advice.

This GitHub repository is a recreated implementation based on the original project topic and previously documented project details. It is not a copy of the original college-project source files or verified original results.
