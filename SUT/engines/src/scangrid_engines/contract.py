"""Interface engine chung (anti-corruption layer). Thêm engine mới = thêm một adapter.

Gate Block 5: thêm engine giả lập chỉ bằng một adapter, không sửa Intake và Orchestrator.
Kiểu ở đây phản chiếu contracts/proto/scangrid/v1/engine.proto cho tới khi bạn sinh code từ proto.
"""

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
from typing import Protocol


class OutcomeStatus(StrEnum):
    CLEAN = "clean"
    SUSPICIOUS = "suspicious"
    INFECTED = "infected"
    ERROR = "error"
    RESOURCE_HAZARD = "resource_hazard"


@dataclass(frozen=True, slots=True)
class Task:
    task_id: str
    scan_id: str
    item_id: str
    engine: str
    attempt: int
    object_key: str


@dataclass(frozen=True, slots=True)
class Outcome:
    task_id: str
    scan_id: str
    item_id: str
    engine: str
    attempt: int
    status: OutcomeStatus
    detail: str = ""


class Engine(Protocol):
    name: str

    def scan(self, task: Task, path: Path) -> Outcome:
        """Quét một file đã tải về. Không tự ack, không tự publish."""
        ...
