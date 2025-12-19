raw_data = [
    "25C", "77F", "30C", "invalid", "100F", "abc", "20C"
]

""" Yêu cầu: Viết hàm trả về một list các số thực (float) là nhiệt độ đã quy đổi hết về độ C.

Công thức: C=(F-32)*5/9

Bỏ qua các dữ liệu rác ("invalid", "abc").

Gợi ý: Bạn cần viết một hàm phụ convert_to_celsius(value: str) rồi dùng List Comprehension để gọi nó. """

#1. LIST COMPREHENSION
def convert_to_celsius_sub_func(value: str) -> float:
    if value.endswith('C'):
        return float(value[:-1])
    elif value.endswith('F'):
        return (float(value[:-1]) - 32) * 5 / 9
    else:
        return None

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
