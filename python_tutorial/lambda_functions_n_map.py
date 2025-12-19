""" Đề bài: Viết một hàm clean_temp chỉ làm 1 nhiệm vụ: Nhận vào chuỗi (VD: "77F") -> Trả về số Float độ C. Nếu lỗi hoặc rác thì trả về None.

Sử dụng hàm map() và filter() kết hợp với lambda (nếu cần) để xử lý list raw_data."""
raw_data = ["25C", "77F", "30C", "invalid", "100F", "abc", "20C"]
def clean_temp_regularly(raw_data: str) -> float | None:
    return (float(raw_data[:-1]) - 32) * 5 / 9 if raw_data.endswith("F") else float(raw_data[:-1]) if raw_data.endswith("C") else None

print(clean_temp_regularly("77F"))    

def clean_temp_by_lambda(raw_data: list[str]) -> list[float]:
    # Bước 1 & 2 kết hợp: Map trước -> ra kết quả có lẫn None -> Filter sau để bỏ None
    result_iterator = filter(lambda x: x is not None, map(clean_temp_regularly, raw_data))

    # Bước 3: "Hứng" kết quả ra List để dùng
    final_result = list(result_iterator)
    return final_result
    # Output: [25.0, 25.0, 30.0, 37.77777777777778, 20.0]

print(f'Lambda Version: {clean_temp_by_lambda(raw_data)}')