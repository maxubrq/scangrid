# ADR cần viết

Chưa viết ADR nào. Mỗi ADR phải có phương án bị loại kèm số liệu (gate Block 17).

| # | Câu hỏi | Block | Số đo lấy từ |
|---|---------|-------|--------------|
| 0001 | Vì sao Kafka cho intake, RabbitMQ cho task engine | 9 | B10 (head-of-line) |
| 0002 | Khi Redis mất trạng thái scan: chạy lại từ yêu cầu gốc hay đánh dấu lỗi | 8 | Thí nghiệm mất ghi, B4 |
| 0003 | Tách làn file gốc và làn file con archive | 4, 5 | B8, B16 |
| 0004 | MongoDB cho Result Store, PostgreSQL cho tenant, audit, registry | 7 | B13, Block 7 |
| 0005 | Cùng một file qua hai cổng là một scan hay hai | 4 | B13 |
| 0006 | Result Store chung hay tách cluster với Policy | 4 | B13 |
| 0007 | Phạm vi cache verdict theo hash (trong scan / trong tenant / toàn cục) | 4 | Bộ archive có file trùng |
| 0008 | Đỉnh 15 phút: cấp sẵn, scale theo lịch hay nới SLO | 12 | B16 |
| 0009 | Kết quả muộn của lần thử cũ: lấy lần nào | 4 | B15 |
