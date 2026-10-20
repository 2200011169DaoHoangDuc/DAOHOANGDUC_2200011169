# src/check_path.py
import os

print(f"Thư mục đang đứng: {os.getcwd()}")

# Định vị tương đối đến file dữ liệu trong data/raw/
file_path = os.path.join("..", "data", "raw", "students.csv")
abs_path = os.path.abspath(file_path)

print(f"Đường dẫn tuyệt đối: {abs_path}")
print(f"Kiểm tra file tồn tại: {os.path.exists(abs_path)}")