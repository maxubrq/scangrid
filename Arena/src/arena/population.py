"""Bộ sinh dân số. TODO(Block 10, bước 2).

- Job đến theo Poisson cộng đợt dồn dập; kích thước file log-normal.
- Sinh file: sạch, EICAR, khớp luật YARA tự đặt, archive lồng, zip bomb, hỏng, sát giới hạn.
- Mỗi job mang `expected` (đáp án) để oracle 4 chấm, không hỏi SUT.
- Hồ sơ tải chuẩn: nền 104 file/s, đỉnh 520 file/s trong 15 phút; local chạy 1/10.
- Archive: phần lớn vài chục file con, một phần >1.000, hiếm khi 10.000; tỷ lệ mặc định 2%.
"""
