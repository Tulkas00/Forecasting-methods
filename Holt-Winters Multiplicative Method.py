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
def holt_winters_multiplicative(data, alpha, beta, gamma, season_length):
    n = len(data)
    l = [data[0]]  # Initial level
    b = [(data[1] / data[0])]  # Initial trend
    s = [data[i] / data[0] for i in range(season_length)]  # Seasonal components
    forecast = []

    for t in range(n):
        if t < season_length:
            forecast.append(data[t])  # Use observed data for initialization
        else:
            forecast.append((l[t-1] + b[t-1]) * s[t-season_length])
        l.append(alpha * (data[t] / s[t-season_length]) + (1 - alpha) * (l[t-1] + b[t-1]))
        b.append(beta * (l[t] - l[t-1]) + (1 - beta) * b[t-1])
        s.append(gamma * (data[t] / l[t]) + (1 - gamma) * s[t-season_length])
    return forecast

periods, seasonal_order, beta, gamma, alpha = initialize_periods()
demands = get_demands(len(periods))
holt_winters_mult_forecast = holt_winters_multiplicative(demands, alpha, beta, gamma, seasonal_order)
print("Holt-Winters Multiplicative Forecast:", holt_winters_mult_forecast)
