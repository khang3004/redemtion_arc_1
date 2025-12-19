raw_data = [
    "25C", "77F", "30C", "invalid", "100F", "abc", "20C"
]

"""
Requirement: Write a function that returns a list of floats representing temperatures converted to Celsius.

Formula: C = (F - 32) * 5 / 9

Ignore invalid data ("invalid", "abc").

Hint: You should write a helper function convert_to_celsius(value: str) and then use List Comprehension to call it.
"""

#1. LIST COMPREHENSION
def convert_to_celsius_sub_func(value: str) -> float:
    return float(value[:-1]) if value.endswith('C') else (float(value[:-1]) - 32) * 5 / 9 if value.endswith('F') else None

def convert_to_celsius_by_list_comprehension(values: list[str]) -> list[str]:
    return [f'{convert_to_celsius_sub_func(value)}C' for value in values if convert_to_celsius_sub_func(value) is not None]

print(convert_to_celsius_by_list_comprehension(raw_data))

#2. RETURN

def convert_to_celsius_by_return(values: list[str]) -> list[str]:
    result = []
    for value in values:
        if value.endswith("C"):
            result.append(f'{float(value[:-1])}C')
        elif value.endswith("F"):
            result.append(f'{(float(value[:-1]) - 32) * 5 / 9}C')
    return result
print(convert_to_celsius_by_return(raw_data))

#3. YIELD GENERATOR
def convert_to_celsius_by_yield(values: list[str]) -> list[str]:
    for value in values:
        if value.endswith("C"): 
            yield f'{float(value[:-1])}C'
        elif value.endswith("F"):
            yield f'{(float(value[:-1]) - 32) * 5 / 9}C'

print(list(convert_to_celsius_by_yield(raw_data)))
