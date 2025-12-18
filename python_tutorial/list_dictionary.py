numbers: list[int] = [1, 2, 3, 4, 5]

print(numbers[0:3])
print(numbers[::-1])

numbers.append(6)
print(numbers)

#define a dictionary
profile: dict[str, any] = {
    "name": "Khang",
    "age": 21,
    "is_student": True,
    "gpa": 4.0
}
print(profile['age'])

salary = profile.get("salary", False)
print(salary)