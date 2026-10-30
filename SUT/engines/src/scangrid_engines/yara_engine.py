"""Engine YARA. TODO(Block 3, bước 2).

- Luật chỉ khớp chuỗi đánh dấu tự đặt (quy tắc NDA). Không dùng mẫu mã độc thật.
- Nhận task từ RabbitMQ (manual ack, prefetch), tải file từ S3 bằng boto3, trả Outcome.
- Đo bằng py-spy (bước 5) để trả lời câu GIL bằng chính flamegraph.
"""
