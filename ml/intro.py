"""
Data Normalization and Standardization
"""

from statistics import mean, stdev

def normalize(data: list, ndigits: int=3) -> list:
    """
    Returns normalized list
    """
    x_min = min(data)
    x_max = max(data)
    return [round((x-x_min) / (x_max-x_min), ndigits) for x in data]

def standardize(data: list, ndigits: int=3)-> list:
    mu = mean(data)
    sigma = stdev(data)
    return [round((x-mu) / (sigma), ndigits) for x in data]

data = [2, 7, 10, 20, 30, 50]
print(normalize(data))
print(standardize(data))