# Currency Exchange Rate Prediction Using Machine Learning

## Project Overview
This project focuses on predicting the currency exchange rate between the Indian Rupee (INR) and the United States Dollar (USD) using Machine Learning techniques.

Historical currency exchange rate data is analyzed to identify patterns and relationships between different exchange rate attributes. A Decision Tree Regressor algorithm is implemented to predict the closing exchange rate based on the Open, High, and Low values.

## Problem Statement
Currency exchange rates fluctuate due to various economic and financial factors, making accurate forecasting a challenging task. This project aims to develop a machine learning model that analyzes historical INR-USD exchange rate data and predicts closing exchange rates using historical market attributes.

## Objectives
- Analyze historical INR-USD exchange rate data.
- Understand exchange rate trends through data visualization.
- Examine relationships between Open, High, Low, and Close values.
- Develop a predictive model using Decision Tree Regression.
- Evaluate the model using training and testing datasets.
- Visualize predicted exchange rates.

## Dataset Description
The dataset contains historical INR-USD exchange rate information with the following attributes:

- Date
- Open
- High
- Low
- Close
- Adj Close
- Volume

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Methodology
1. Data Collection: Import historical INR-USD exchange rate data.
2. Data Preprocessing: Load and prepare the dataset for analysis.
3. Exploratory Data Analysis: Analyze the dataset using statistical methods and visualizations.
4. Correlation Analysis: Examine relationships between numerical attributes using a correlation matrix and heatmap.
5. Feature Selection: Select Open, High, and Low as input features and Close as the target variable.
6. Data Splitting: Divide the dataset into 80% training data and 20% testing data.
7. Model Development: Implement a Decision Tree Regressor.
8. Model Training: Train the model using historical exchange rate data.
9. Prediction: Predict closing exchange rates using the trained model.
10. Visualization: Display historical trends and prediction results.

## Machine Learning Algorithm
**Decision Tree Regressor**

A Decision Tree Regressor is a supervised machine learning algorithm used for predicting continuous numerical values. It learns relationships between input features and the target variable by dividing the dataset into decision-based branches.

## Python Libraries
- NumPy – Numerical computations.
- Pandas – Data manipulation and analysis.
- Matplotlib – Data visualization.
- Seaborn – Statistical visualization.
- Scikit-learn – Machine learning model development.

## Expected Outcome
The project aims to develop a machine learning model that predicts INR-USD closing exchange rates based on historical exchange rate attributes and demonstrates the application of regression techniques in financial forecasting.

## Future Enhancements
- Experiment with Random Forest and other regression algorithms.
- Incorporate additional economic indicators.
- Improve prediction performance through hyperparameter tuning.
- Explore time-series forecasting techniques.

## Author
Aditi Balakrishnan

## License
This project is intended for educational and learning purposes.
