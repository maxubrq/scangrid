"""Engine giải nén (Extractor). TODO(Block 3, bước 3; Block 5; mục 8.7).

Giới hạn phải có: tổng kích thước giải nén, số file, độ sâu lồng, tỷ lệ nén; chặn zip slip (../).
File con: ID xác định (scan_id + đường dẫn trong archive + hash), gửi theo lô,
kết thúc bằng "xong, tổng N file con". Property test bằng hypothesis.
"""
