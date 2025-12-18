print("Hello World")
#
def calculate_total(items:List[float], tax_rate:float)->float:
    return (sum(items) * (1 + tax_rate))

print(calculate_total([1, 2], 0.1))
    