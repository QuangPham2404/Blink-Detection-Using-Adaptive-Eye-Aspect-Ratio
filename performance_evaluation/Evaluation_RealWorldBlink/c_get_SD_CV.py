import math

#function to calculate mean value
def calculate_mean(measurements):
    """
    Calculate the mean for a list of measurements.
    Parameters:
        measurements (list): A list of numerical values.
    Returns:
        float: The mean of the measurements.
    """
    return round(sum(measurements)/len(measurements), 4)

# function to calculate SD
def calculate_standard_deviation(measurements):
    """
    Calculate the standard deviation for a list of measurements.
    Parameters:
        measurements (list): A list of numerical values.
    Returns:
        float: The standard deviation of the measurements.
    """
    # Step 1: Calculate the mean
    mean = sum(measurements) / len(measurements)
    
    # Step 2: Calculate the squared differences from the mean
    squared_differences = [(x - mean) ** 2 for x in measurements]
    
    # Step 3: Calculate the variance
    variance = sum(squared_differences) / (len(measurements) - 1)  # Sample variance (n - 1)
    
    # Step 4: Take the square root of the variance
    standard_deviation = math.sqrt(variance)  # Do not round here to preserve precision
    
    return round(standard_deviation, 4)  # Round the final result for clarity

# function to calculate CV
def calculate_cv(values, standard_deviation):
    """
    Calculate the Coefficient of Variation (CV) for a dataset.
    Parameters:
        values (list): List of numerical values.
        standard_deviation (float): Standard deviation of the values.
    Returns:
        float: CV as a percentage.
    """
    mean_value = sum(values) / len(values)  # Mean without rounding for precision
    cv = (standard_deviation / mean_value) * 100  # Calculate CV
    
    return round(cv, 4)  # Round the final result for clarity

# Example usage
measurements = [0.0933,
0.0925,
0.0989,
0.1364,
0.11,
0.119,
0.0934,
0.0923,
0.1187,
0.0905]
mean = calculate_mean(measurements)
std_dev = calculate_standard_deviation(measurements)
CV = calculate_cv(measurements, std_dev)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
print("CV:", CV)
