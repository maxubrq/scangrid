"""Tám oracle, viết TRƯỚC khi chạy battle. Mỗi oracle đọc lịch sử, trả kết quả kèm bằng chứng.

Gate Block 10: tắt cập nhật có điều kiện khi gộp verdict thì oracle "không trùng" báo hỏng đúng file.
"""

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from typing import Any

Event = Mapping[str, Any]


@dataclass(frozen=True)
class OracleResult:
    name: str
    passed: bool
    evidence: list[str] = field(default_factory=list)


def no_loss(history: Iterable[Event]) -> OracleResult:
    """1. Mọi yêu cầu đã nhận (vào topic, hoặc REST trả 202) có đúng một verdict cuối, đúng kênh, trong hạn."""
    raise NotImplementedError


def no_duplicate_effect(history: Iterable[Event]) -> OracleResult:
    """2. Chốt verdict một lần; verdict trùng trên result topic được đếm và có cùng nội dung."""
    raise NotImplementedError


def complete_engine_list(history: Iterable[Event]) -> OracleResult:
    """3. Verdict có kết quả hoặc đánh dấu timeout cho đúng mọi engine mong đợi: không thừa, không thiếu."""
    raise NotImplementedError


def correct_verdict(history: Iterable[Event]) -> OracleResult:
    """4. EICAR và file khớp YARA bị phát hiện; file sạch không báo nhầm; zip bomb bị chặn, worker không sập."""
    raise NotImplementedError


def correct_stages(history: Iterable[Event]) -> OracleResult:
    """5. Chuỗi stage thực tế khớp planNextStage(policy, snapshot) chạy lại offline.

    Câu hỏi: oracle Python chạy planner TypeScript thế nào? (gọi node? xuất bảng? cần chốt sớm)
    """
    raise NotImplementedError


def tenant_isolation(history: Iterable[Event]) -> OracleResult:
    """6. Tải dồn của một tenant không làm tenant khác vượt SLO quá ngưỡng."""
    raise NotImplementedError


def slo(history: Iterable[Event]) -> OracleResult:
    """7. p95, p99 thời gian từ submit tới verdict, theo workflow, đo phía client, open model."""
    raise NotImplementedError


def recovery(history: Iterable[Event]) -> OracleResult:
    """8. Sau khi lỗi dừng, số scan mở về mức nền trong thời gian tính trước; báo MTTR."""
    raise NotImplementedError


ALL = {
    "no_loss": no_loss,
    "no_duplicate_effect": no_duplicate_effect,
    "complete_engine_list": complete_engine_list,
    "correct_verdict": correct_verdict,
    "correct_stages": correct_stages,
    "tenant_isolation": tenant_isolation,
    "slo": slo,
    "recovery": recovery,
}
