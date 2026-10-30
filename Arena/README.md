# Arena Battle World

Sinh tải và file như người dùng thật, gây sự cố như hạ tầng thật, ghi lịch sử **phía client**,
chấm bằng oracle viết trước. Mỗi battle chạy theo seed, 5 lần, báo phương sai.
Giới hạn: Docker và mạng không tất định, nên đây là kịch bản tái lập được, chưa phải mô phỏng tất định từng bit.

## Đã có (khung)

| File | Trạng thái |
|------|-----------|
| `scenario.py` | Schema battle (pydantic, cấm field lạ) + `load_battle`. **Dùng được.** |
| `cli.py` | `arena run --battle ... --seed ...`: đọc battle, dừng ở TODO runner |
| `oracles/__init__.py` | 8 chữ ký + docstring bất biến; thân `NotImplementedError` |
| `faults.py` | `FaultKind` + `Fault` Protocol |
| `mock_engine/behaviors.py` | Danh mục hành vi theo bảng mục 3 |
| `controller.py` | FastAPI start/stop/status trả 501 |
| `rng.py`, `population.py`, `recorder.py`, `report.py` | Chỉ có đặc tả |
| `battles/B1`, `B2` | Mẫu YAML không lỗi và có lỗi |

## Việc của bạn

### Block 3 · khung (1,5 giờ)
- [ ] Controller: start, stop, status đọc YAML

### Block 10 · dựng Arena (8 giờ)
- [ ] `rng.py`: luồng ngẫu nhiên riêng cho từng thành phần
- [ ] Population (Poisson + dồn dập, log-normal, các loại file, `expected`)
- [ ] Faults: Docker SDK, toxiproxy, netem, LocalStack, Mongo stepdown
- [ ] Recorder JSONL theo `contracts/jsonschema/history_event.v1.json`; OpenTelemetry
- [ ] Test oracle trước (lịch sử tay), rồi 8 oracle; báo cáo Markdown
- [ ] Mock engine chạy được (Block 5)
- Gate: tắt cập nhật có điều kiện khi gộp verdict → oracle 2 báo đúng file; cùng seed hai lần → cùng lịch tải và lịch lỗi.

### Battle
| # | Tên | YAML | Đạt |
|---|-----|------|-----|
| B1 | Ngày thường | ✓ mẫu | |
| B2 | Đổi leader | ✓ mẫu | |
| B3 | Thỏ ngã | | |
| B4 | Redis failover giữa chừng | | |
| B5 | Engine im lặng | | |
| B6 | Kết quả trùng | | |
| B7 | Lệch phiên bản schema | | |
| B8 | Lũ file độc | | |
| B9 | Hàng xóm ồn ào | | |
| B10 | Message hỏng và bão rebalance | | |
| B11 | Đám mây (AWS, Block 12) | | |
| B12 | Ngày tận thế | | |
| B13 | Hai cổng, một lõi | | |
| B14 | Deploy giữa trận | | |
| B15 | Kết quả muộn | | |
| B16 | Đỉnh 15 phút | | |
| B17 | Đổi schema phá vỡ giữa giờ cao điểm | | |

## Câu hỏi còn mở

- Oracle 5 chạy planner TypeScript từ Python thế nào? Chốt trước khi viết planner, vì nó quyết định planner có cần xuất được dạng dữ liệu không.
- `history_event` đủ cho 8 oracle chưa? Thử viết tay lịch sử cho oracle 1 và 3 trước khi code recorder.
