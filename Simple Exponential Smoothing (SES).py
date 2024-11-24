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
    """Collect demand data for each period."""
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
def simple_exponential_smoothing(data, alpha):
    forecast = [data[0]]
    for t in range(1, len(data)):
        forecast.append(alpha * data[t-1] + (1 - alpha) * forecast[t-1])
    return forecast

periods, _, _, _, alpha = initialize_periods()
demands = get_demands(len(periods))
ses_forecast = simple_exponential_smoothing(demands, alpha)
print("SES Forecast:", ses_forecast)
