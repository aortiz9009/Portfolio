# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:02 2024

@author: artur
"""

# Import necessary libraries
import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Fetch historical stock data for AAPL and FB
tickers = ['AAPL', 'META']
stock_data = yf.download(tickers, start='2010-01-01', end='2024-01-01')

# Handle missing values
stock_data = stock_data.dropna()

# Create moving average features for AAPL
stock_data[('AAPL', 'MA_50')] = stock_data[('Close', 'AAPL')].rolling(window=50).mean()
stock_data[('AAPL', 'MA_200')] = stock_data[('Close', 'AAPL')].rolling(window=200).mean()

# Create moving average features for FB
stock_data[('META', 'MA_50')] = stock_data[('Close', 'META')].rolling(window=50).mean()
stock_data[('META', 'MA_200')] = stock_data[('Close', 'META')].rolling(window=200).mean()

# Drop rows with NaN values created by rolling window
stock_data = stock_data.dropna()

# Define features and target for AAPL
X_aapl = stock_data[[('AAPL', 'MA_50'), ('AAPL', 'MA_200')]]
y_aapl = stock_data[('Close', 'AAPL')]

# Split the data for AAPL
X_aapl_train, X_aapl_test, y_aapl_train, y_aapl_test = train_test_split(X_aapl, y_aapl, test_size=0.2, random_state=42)

# Define features and target for FB
X_fb = stock_data[[('META', 'MA_50'), ('META', 'MA_200')]]
y_fb = stock_data[('Close', 'META')]

# Split the data for FB
X_fb_train, X_fb_test, y_fb_train, y_fb_test = train_test_split(X_fb, y_fb, test_size=0.2, random_state=42)

# Initialize and train the model for AAPL
model_aapl = LinearRegression()
model_aapl.fit(X_aapl_train, y_aapl_train)

# Initialize and train the model for FB
model_fb = LinearRegression()
model_fb.fit(X_fb_train, y_fb_train)

# Predict on the test set for AAPL
y_aapl_pred = model_aapl.predict(X_aapl_test)

# Calculate RMSE for AAPL
rmse_aapl = mean_squared_error(y_aapl_test, y_aapl_pred, squared=False)
print('AAPL RMSE:', rmse_aapl)

# Predict on the test set for FB
y_fb_pred = model_fb.predict(X_fb_test)

# Calculate RMSE for FB
rmse_fb = mean_squared_error(y_fb_test, y_fb_pred, squared=False)
print('FB RMSE:', rmse_fb)

# Plot the historical data for AAPL
plt.figure(figsize=(14, 7))
sns.lineplot(data=stock_data[('Close', 'AAPL')], label='AAPL Actual')

# Plot the predictions for AAPL
predicted_data_aapl = X_aapl_test.copy()
predicted_data_aapl['Predicted_Close'] = y_aapl_pred
predicted_data_aapl = predicted_data_aapl.sort_index()

sns.lineplot(data=predicted_data_aapl['Predicted_Close'], label='AAPL Predicted')

# Plot the historical data for FB
sns.lineplot(data=stock_data[('Close', 'META')], label='FB Actual')

# Plot the predictions for FB
predicted_data_fb = X_fb_test.copy()
predicted_data_fb['Predicted_Close'] = y_fb_pred
predicted_data_fb = predicted_data_fb.sort_index()

sns.lineplot(data=predicted_data_fb['Predicted_Close'], label='FB Predicted')

plt.title('Stock Price Prediction for AAPL and FB')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()