"""Watcher bộ nhớ cgroup v2. TODO(Block 5, bước 3).

Đọc memory.current, memory.max, memory.events của cgroup hiện tại.
Vượt ngưỡng: hủy quét, trả Outcome RESOURCE_HAZARD, ack message thay vì để nó quay lại hàng đợi
(file độc OOM rồi được giao lại sẽ giết dần cả pool).
Lưu ý: macOS không có cgroup; chạy và test trong container Linux.
"""
