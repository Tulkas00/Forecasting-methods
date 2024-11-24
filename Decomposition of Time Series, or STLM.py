import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def initialize_periods():
    periods = []
    while True:
        try:
            num_periods = int(input('Enter the number of periods (between 6 and 24): '))
            if 6 <= num_periods <= 24:
                break
            else:
                print("Please enter a value between 6 and 24.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    seasonal_order = int(input("Enter the seasonal order: "))
    for i in range(1, num_periods + 1):
        periods.append(i)
    
    beta = float(input('Enter the trend correction factor (beta): '))
    gamma = float(input('Enter the seasonality correction factor (gamma): '))
    alpha = float(input('Enter the smoothing factor (alpha): '))

    return periods, seasonal_order, beta, gamma, alpha

def get_demands(num_periods):
    demands = []
    for i in range(1, num_periods + 1):
        while True:
            try:
                demand = float(input(f'Enter the product demand for period {i}: '))
                demands.append(demand)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return demands

def decomposition_method(data, seasonal_period):
        data_series = pd.Series(data)
    
    
    decomposition = seasonal_decompose(data_series, model='additive', period=seasonal_period)
    
    trend = decomposition.trend.dropna()  # Removing NaN values
    seasonal = decomposition.seasonal.dropna()
    residual = decomposition.resid.dropna()

    plt.figure(figsize=(10,8))
    plt.subplot(411)
    plt.plot(data, label='Original Data')
    plt.legend(loc='upper left')
    plt.subplot(412)
    plt.plot(trend, label='Trend Component')
    plt.legend(loc='upper left')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonal Component')
    plt.legend(loc='upper left')
    plt.subplot(414)
    plt.plot(residual, label='Residual Component')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

    return trend, seasonal, residual

periods, seasonal_order, _, _, _ = initialize_periods()
demands = get_demands(len(periods))

trend, seasonal, residual = decomposition_method(demands, seasonal_order)

print("Trend Component:", trend)
print("Seasonal Component:", seasonal)
print("Residual Component:", residual)
