# ScanGrid × Arena Battle World

Bản dựng lại độc lập một nền tảng quét file đa engine, đa tenant (SUT), đặt trong một thế giới
mô phỏng bất định (Arena) để chấm bằng bất biến.

> Đây là bản dựng lại độc lập để đo những vấn đề tôi từng gặp; không chứa gì của công ty cũ.
> Engine mã nguồn mở (ClamAV, YARA, libmagic). Chỉ dùng EICAR và luật YARA khớp chuỗi tự đặt.

## Cấu trúc

```
contracts/   ranh giới SUT ↔ Arena (DRAFT, vùng chặt)
SUT/         ScanGrid: TypeScript (Intake, Orchestrator, Delivery, Policy) + engine Python
Arena/       Python: population, faults, mock engine, recorder, oracles, battles
docs/        ADR, nhật ký dự đoán
DEBT.md      gate chưa đạt
```

## Chạy

```
make install   # npm + uv
make check     # typecheck, lint, test
make up        # hạ tầng dev một node
make battle B=B1 SEED=42
```

## Trạng thái

Mới là khung. Bảng việc theo Block nằm ở `SUT/README.md` và `Arena/README.md`.
Chỉ kết quả có bên xác nhận ngoài (mục 7 lộ trình) mới được ghi vào đây.
