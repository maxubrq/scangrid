"""Kịch bản battle: YAML có seed, ghép lịch tải và lịch lỗi. Phần schema đã có; phần chạy là của bạn."""

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class TenantProfile(Strict):
    id: str
    weight: float = Field(gt=0)
    workflows: list[str]


class FileMix(Strict):
    """Tỷ lệ loại file. Population sinh đáp án (expected) cho oracle 4 từ đây."""

    clean: float = 0.9
    eicar: float = 0.02
    yara_marker: float = 0.02
    archive: float = 0.02
    zip_bomb: float = 0.0
    corrupt: float = 0.01
    near_limit: float = 0.0


class LoadPhase(Strict):
    """Open model: tốc độ đến không phụ thuộc SUT trả lời nhanh hay chậm."""

    duration_s: int = Field(gt=0)
    rate_per_s: float = Field(ge=0)
    channel: Literal["kafka", "rest", "mixed"] = "kafka"
    burst: bool = False


class FaultSpec(Strict):
    at_s: float = Field(ge=0)
    kind: str  # xem faults.FaultKind
    target: str
    duration_s: float | None = None
    params: dict[str, object] = Field(default_factory=dict)


class Battle(Strict):
    id: str
    title: str
    seed: int
    runs: int = 5
    scale: float = Field(default=0.1, gt=0, description="1/10 trên local")
    tenants: list[TenantProfile]
    file_mix: FileMix = FileMix()
    load: list[LoadPhase]
    faults: list[FaultSpec] = Field(default_factory=list)
    oracles: list[str]


def load_battle(path: Path) -> Battle:
    return Battle.model_validate(yaml.safe_load(path.read_text()))
