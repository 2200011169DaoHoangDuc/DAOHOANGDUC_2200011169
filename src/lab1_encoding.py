# lab1_encoding.py
text_en = "Hello Data"
text_vi = "Xin chào Dữ liệu"

bytes_en = text_en.encode('utf-8')
bytes_vi = text_vi.encode('utf-8')

print("=" * 60)
print(f"Chuỗi: '{text_en}' | Số ký tự: {len(text_en)} | Số byte UTF-8: {len(bytes_en)}")
print(f"Chuỗi: '{text_vi}' | Số ký tự: {len(text_vi)} | Số byte UTF-8: {len(bytes_vi)}")
print("=" * 60)

char = 'A'
print(f"Ký tự '{char}': Mã ASCII = {ord(char)} | Mã nhị phân = {bin(ord(char))}")