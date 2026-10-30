# ScanGrid (SUT)

## Tên (mục 8.10)

Code dùng tên mới. Kể hệ thống cũ bằng tên cũ, vẽ lại bằng tên mới.

| Context | Thư mục | Ý định một câu | Tên cũ |
|---------|---------|----------------|--------|
| Intake | `services/intake` | Nhận mỗi yêu cầu quét đúng một lần, khi hệ thống còn sức | Request Handler, REST API (scan) |
| Orchestration | `services/orchestrator` | Đưa mỗi scan từ lúc nhận tới verdict | lõi Result Handler, Redis aggregate store |
| Engine Execution | `engines/` | Chạy task trên engine bên thứ ba qua một hợp đồng chung | Engine |
| Policy | `services/policy` | Cho biết cấu hình hiệu lực của tenant kèm lý do | Configuration Service |
| Delivery | `services/delivery` | Đưa verdict tới mọi kênh khách đã chọn | phần phát kết quả của Result Handler |

Ngôn ngữ chung: `packages/domain/src/index.ts`.

## Đã có (khung)

- Workspace npm, TypeScript strict, vitest + fast-check.
- Kiểu domain; chữ ký `planNextStage` (hàm thuần) và `it.todo` cho bảng workflow và thuộc tính.
- Interface `ScanStateStore` với các kết quả `applyOutcome` mà oracle cần phân biệt.
- `lua/apply_outcome.lua`: chỉ có các bất biến script phải thỏa và một câu hỏi thiết kế còn mở.
- `engines/`: uv, mypy strict, ruff; `Engine` Protocol; stub YARA, Extractor, watcher cgroup.
- `infra/compose.dev.yml`: Kafka, RabbitMQ, Redis, MongoDB (replica set), PostgreSQL, LocalStack, mỗi thứ **một node**.

## Việc của bạn

### Block 4 · lõi (11 giờ)
- [ ] Schema trạng thái scan + 3 workflow (`av_only`, `av_cdr_dlp`, `av_then_sandbox`)
- [ ] `planNextStage` + bảng test + property test (fast-check)
- [ ] Intake/Kafka: đọc topic, cache policy, `createScan`, publish stage 1 có confirm, **rồi** commit offset
- [ ] `apply_outcome.lua` + Orchestrator: gộp, tính stage, chốt verdict, publish; quét deadline, retry
- [ ] Compose toàn hệ thống + `make demo`
- [ ] Intake/REST (Fastify): `POST /scans` + Idempotency-Key, 202 chỉ khi đã bền; `GET /scans/:id` (410 sau 24 giờ)
- [ ] Delivery: Result Store MongoDB (TTL `expireAt`) trước, rồi Kafka + webhook (HMAC, backoff), tiến trình gửi lại kênh thiếu
- [ ] `ScanStateStore` v1 (theo loại engine) và v2 (theo task); trần task mỗi scan; hai làn queue; filetype trong tiến trình; cache verdict theo hash
- Gate: `make demo` < 10 phút trên máy sạch; property test đạt; outcome gửi hai lần → không publish stage hai lần, verdict chốt một lần; engine im lặng → scan vẫn đóng.

### Block 5 · engine (5 giờ)
- [ ] Adapter ClamAV (clamd); YARA với luật chuỗi đánh dấu tự đặt; libmagic
- [ ] Watcher cgroup v2 (chạy trong container Linux)
- [ ] Tách hàng đợi file đơn và archive, pool riêng
- Gate: EICAR, YARA bị phát hiện, file sạch không báo nhầm; thêm engine giả chỉ bằng một adapter; watcher hủy trước OOM.

### Block 8 · Redis Cluster (5 giờ)
- [ ] `infra/compose.ha.yml`: 3 master + 3 replica; ioredis Cluster
- [ ] Thí nghiệm mất ghi (chặn replication, kill master); đo lại với `WAIT`
- [ ] Phát hiện + khôi phục scan mất trạng thái; ADR-0002

### Block 9 · Kafka, RabbitMQ (6 giờ)
- [ ] `infra/compose.ha.yml`: Kafka 3 broker KRaft, RabbitMQ 3 node quorum queue; ghi từng tham số chịu lỗi và lý do
- [ ] ADR-0001

### Block 6, 7 · MongoDB, PostgreSQL
- [ ] Policy Service trên PostgreSQL theo mục 8.8: registry chỉ thêm, override thưa, resolver, upcaster, dry-run, audit chuỗi hash

## Chỗ mình cố tình chưa quyết

1. Lua tính stage hay Node tính stage (xem đầu `apply_outcome.lua`).
2. `task_id`, `item_id` sinh thế nào (`contracts/README.md`).
3. Proto codegen: buf hay protoc (`protoc` chưa cài).
