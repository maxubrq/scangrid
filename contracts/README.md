# Contracts: ranh giới giữa SUT và Arena

Đây là vùng dung sai **chặt**: Arena chấm SUT chỉ qua những hợp đồng này, nên đổi chúng là đổi
cả hai phía. Mọi file ở đây đang là **DRAFT v0**: mình phác các field tối thiểu từ lộ trình, bạn chốt.

| File | Ai ghi | Ai đọc | Chốt ở |
|------|--------|--------|--------|
| `jsonschema/intake_request.v1.json` | client (Arena), qua Kafka hoặc REST | Intake | Block 4 |
| `proto/scangrid/v1/engine.proto` | Orchestrator (Task), Engine (Outcome) | Engine, Orchestrator | Block 4–5 |
| `jsonschema/history_event.v1.json` | Arena recorder (phía client) | Oracle | Block 10 |

Luật:
- Chỉ thêm field, không đổi nghĩa field cũ. Đổi phá vỡ thì tăng `v2` và giữ `v1` song song.
- Tên theo ngôn ngữ chung mục 8.10 (Scan, Item, Task, Outcome, Stage, Verdict). Một khái niệm một tên.
- Oracle chỉ đọc `history_event`, không đọc log của SUT.

TODO của bạn trước khi code Block 4:
- [ ] Chốt `task_id` sinh thế nào để idempotent (gợi ý: hàm xác định của scan_id, item_id, engine, attempt).
- [ ] Chốt `item_id` của file con (đường dẫn trong archive + hash).
- [ ] Chọn công cụ sinh code từ proto (buf / protoc + ts-proto / betterproto). `protoc` chưa cài trên máy.
