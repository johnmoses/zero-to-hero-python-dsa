"""
Finance Algorithm
"""

def intro_tax(price: float, tax_rate: float) -> float:
    return price * (1 + tax_rate)

price = 100
tax_rate = 0.24
print(f"{intro_tax(price, tax_rate) = }")