students: list[str] = ["An", "Binh", "Chi"]

for student in students:
    print(f"khang {student}")

for idx, student in enumerate(students, start= 1):
    print(f"{idx}. {student}")
