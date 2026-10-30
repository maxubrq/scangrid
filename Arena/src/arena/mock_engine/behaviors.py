"""Hành vi của engine giả, bật theo tỷ lệ hoặc theo lịch, lấy từ seed. TODO(Block 5, bước 2).

Engine giả nói đúng giao thức của engine thật; SUT không được biết nó là giả.
"""

from enum import StrEnum


class Behavior(StrEnum):
    # Thời gian
    LATENCY_LONG_TAIL = "latency_long_tail"
    HANG = "hang"
    SLOW_DRIFT = "slow_drift"
    # Vòng đời
    CRASH_BEFORE_RESULT = "crash_before_result"
    CRASH_AFTER_RESULT_BEFORE_ACK = "crash_after_result_before_ack"
    RESTART_LOOP = "restart_loop"
    COLD_START = "cold_start"  # 2–10 phút
    UNCLEAN_SHUTDOWN = "unclean_shutdown"
    # Kết quả
    DUPLICATE_RESULT = "duplicate_result"
    MALFORMED_RESULT = "malformed_result"
    UNKNOWN_SCAN = "unknown_scan"
    CONFLICTING_RETRY = "conflicting_retry"
    LATE_RESULT = "late_result"  # B15
    # Phiên bản
    BREAKING_SCHEMA = "breaking_schema"  # đổi tên, đổi kiểu, xóa field, đổi mặc định
    CONCURRENT_REGISTER = "concurrent_register"
    # Tài nguyên
    EAT_MEMORY = "eat_memory"
    EAT_CPU = "eat_cpu"
    LEAK_FD = "leak_fd"
    # Archive giả
    CHILDREN_STAGGERED = "children_staggered"
    CHILDREN_DUPLICATE = "children_duplicate"
    NEVER_SEND_DONE = "never_send_done"
    DONE_BEFORE_CHILDREN = "done_before_children"
    HOLD_PAST_CONSUMER_TIMEOUT = "hold_past_consumer_timeout"
    NESTED_DEEP = "nested_deep"
