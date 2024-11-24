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
from statsmodels.tsa.arima.model import ARIMA

def arima_forecasting(data, order):
    model = ARIMA(data, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=5)  # Forecast 5 steps ahead
    return forecast

periods, _, _, _, _ = initialize_periods()
demands = get_demands(len(periods))
order = tuple(map(int, input("Enter the ARIMA order (p, d, q) separated by spaces: ").split()))
arima_forecast = arima_forecasting(demands, order)
print("ARIMA Forecast:", arima_forecast)
