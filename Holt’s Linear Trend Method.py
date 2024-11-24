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
def holt_linear(data, alpha, beta):
    l = [data[0]]  # Level
    b = [(data[1] - data[0])]  # Trend
    forecast = [l[0] + b[0]]  # Initial forecast
    
    for t in range(1, len(data)):
        l.append(alpha * data[t] + (1 - alpha) * (l[t-1] + b[t-1]))
        b.append(beta * (l[t] - l[t-1]) + (1 - beta) * b[t-1])
        forecast.append(l[t] + b[t])
    return forecast

periods, _, beta, _, alpha = initialize_periods()
demands = get_demands(len(periods))
holt_forecast = holt_linear(demands, alpha, beta)
print("Holt's Linear Forecast:", holt_forecast)
