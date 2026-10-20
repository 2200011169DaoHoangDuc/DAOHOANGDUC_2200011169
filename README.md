# DỰ ÁN: TỪ DỮ LIỆU ĐẾN PHÂN TÍCH VỚI PYTHON
- **Họ và tên:** Đào Hoàng Đức
- **MSSV:** 2200011169
- **Lớp:** [Điền mã lớp của bạn vào đây]

---

## BÁO CÁO THU HOẠCH (5 CÂU HỎI TRẢ LỜI)

### Câu 1: Vì sao chuỗi tiếng Việt có dấu tốn nhiều byte hơn chuỗi tiếng Anh có cùng số ký tự?
- Chuỗi tiếng Anh sử dụng các ký tự nằm trong bảng mã **ASCII chuẩn** (từ 0 đến 127). Khi mã hóa theo chuẩn **UTF-8**, mỗi ký tự này chỉ tốn đúng **1 byte** (8 bits).
- Chuỗi tiếng Việt chứa các ký tự có dấu (như `á`, `à`, `ệ`, `ư`, `ơ`,...) thuộc dải ký tự mở rộng của mã Unicode. Chuẩn mã hóa UTF-8 là mã hóa độ dài biến đổi (variable-length encoding): các ký tự Unicode này cần từ **2 đến 3 bytes** để biểu diễn thay vì 1 byte.
- **Ví dụ:** Trong file `lab1_encoding.py`, chuỗi `"Hello Data"` (10 ký tự) tốn đúng **10 bytes**, trong khi chuỗi `"Xin chào Dữ liệu"` (16 ký tự) tốn tới **21 bytes** vì các ký tự `à`, `ữ`, `ệ` chiếm nhiều byte hơn.

---

### Câu 2: So sánh file CSV và JSON. Khi dữ liệu phân cấp lồng nhau (nested), ta nên dùng định dạng nào?

| Tiêu chí | CSV (Comma-Separated Values) | JSON (JavaScript Object Notation) |
| :--- | :--- | :--- |
| **Cấu trúc** | Dạng bảng 2 chiều đơn giản (dòng và cột). | Dạng cây, cấu trúc Key-Value hoặc Array. |
| **Dung lượng** | Nhẹ hơn (chỉ chứa giá trị, không lưu lại tên thuộc tính ở mỗi dòng). | Nặng hơn một chút (lặp lại tên thuộc tính ở mọi đối tượng). |
| **Tính linh hoạt** | Kém linh hoạt với dữ liệu không đồng nhất hoặc phức tạp. | Rất linh hoạt, hỗ trợ mảng (Array) và đối tượng (Object) lồng nhau. |
| **Phần mềm đọc** | Dễ dàng mở và chỉnh sửa bằng MS Excel, Google Sheets. | Phù hợp trao đổi dữ liệu API, lập trình Web/App. |

- **Kết luận:** Khi dữ liệu có cấu trúc **phân cấp lồng nhau (nested structure)** (ví dụ: một sinh viên có nhiều môn học, mỗi môn học có danh sách điểm chi tiết), ta **bắt buộc/nên dùng định dạng JSON**. Lý do là CSV không thể biểu diễn trực tiếp các quan hệ 1-nhiều lồng nhau nếu không tách thành nhiều bảng hoặc làm phẳng dữ liệu (flattening).

---

### Câu 3: Hiện tượng gì xảy ra khi mở một file ảnh bằng Notepad? Giải thích nguyên nhân.
- **Hiện tượng:** Khi mở file ảnh (ví dụ `.png`, `.jpg`) bằng Notepad, màn hình hiển thị hàng loạt ký tự lạ, vô nghĩa, biểu tượng mã máy, hoặc bị lỗi văng ứng dụng/đơ màn hình.
- **Nguyên nhân:**
  - File văn bản (`.txt`, `.py`, `.csv`) là **Text File**, chứa các điểm mã (code points) đại diện cho văn bản có thể đọc được bằng người.
  - File ảnh là **Binary File** (file nhị phân). Dữ liệu bên trong bao gồm tiêu đề định dạng, bảng màu, dữ liệu nén pixel... được biểu diễn dưới dạng các chuỗi byte thô (00 đến FF).
  - Notepad là một trình soạn thảo văn bản thuần (Text Editor). Nó cố gắng ép các byte nhị phân thô của file ảnh chuyển thành các ký tự văn bản tương ứng theo bảng mã mặc định (như UTF-8/ANSI). Do nhiều chuỗi byte nhị phân không tương ứng với ký tự văn bản hợp lệ nào, Notepad sẽ hiển thị các ký tự tượng hình rối rối/mã lạ.

---

### Câu 4: Vì sao trong Khoa học Dữ liệu phải tách `data/raw/` với `data/processed/` và phải có file `.gitignore`?
1. **Tách `data/raw/` và `data/processed/`:**
   - **Bảo vệ nguyên vẹn dữ liệu gốc (`data/raw/`):** Dữ liệu thô là "nguồn chân lý" (Source of Truth). Mọi thao tác xử lý lỗi hoặc làm sạch sai lầm đều có thể tái tạo lại từ đầu nếu dữ liệu gốc không bị ghi đè.
   - **Minh bạch quy trình làm sạch (`data/processed/`):** Giúp phân định rõ ràng giữa dữ liệu nguyên bản chưa qua xử lý và dữ liệu đã qua tiền xử lý (đã lọc trích, làm sạch, sẵn sàng cho huấn luyện mô hình hay vẽ báo cáo).
2. **Sử dụng file `.gitignore`:**
   - **Tránh đẩy dữ liệu/file rác lên GitHub:** Loại bỏ các file tạm (`__pycache__/`, `.ipynb_checkpoints/`), môi trường ảo (`venv/`), hoặc cấu hình cá nhân (`.vscode/`).
   - **Bảo mật thông tin:** Ngăn chặn việc lỡ tay commit các file chứa khoá bí mật (`.env`, API keys).
   - **Tối ưu dung lượng Repository:** Giữ cho Repository nhẹ, lịch sử Git sạch sẽ và thao tác `git push/pull` nhanh chóng.

---

### Câu 5: Nhận xét ngắn về điểm GPA rút ra từ biểu đồ phân tích ở Buổi 2
Dựa trên phân tích 5 sinh viên trong tập dữ liệu:
- **Điểm GPA trung bình:** 3.56 (cho thấy mức học lực chung của nhóm khá cao).
- **Điểm GPA cao nhất:** 3.90 (sinh viên **Vu Hai Yen**, ngành *Computer Science*).
- **Điểm GPA thấp nhất:** 3.10 (sinh viên **Le Van C**, ngành *Information Technology*).
- **Nhận xét chung:**
  1. Các sinh viên thuộc ngành *Computer Science* và *Data Science* có mức GPA áp đảo (từ 3.4 đến 3.9).
  2. 80% sinh viên (4/5 bạn) đạt điểm GPA từ 3.4 trở lên và thuộc nhóm sinh viên có học lực Giỏi/Xuất sắc (GPA >= 3.5).