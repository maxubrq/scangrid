"""Bộ ghi lịch sử phía client, JSONL theo contracts/jsonschema/history_event.v1.json.

TODO(Block 10, bước 4): ghi bằng time.monotonic_ns(); một file mỗi (battle, seed, run).
Oracle không bao giờ đọc log của SUT, chỉ đọc file này.
"""
