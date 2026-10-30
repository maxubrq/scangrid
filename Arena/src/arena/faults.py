"""Bộ bơm lỗi. TODO(Block 10, bước 3).

Mỗi lỗi có start/stop, ghi fault_start/fault_end vào lịch sử để oracle 8 đo MTTR.
"""

from enum import StrEnum
from typing import Protocol


class FaultKind(StrEnum):
    KILL_CONTAINER = "kill_container"
    PAUSE_CONTAINER = "pause_container"
    NETWORK_PARTITION = "network_partition"  # toxiproxy
    LATENCY = "latency"  # toxiproxy / tc netem
    PACKET_LOSS = "packet_loss"
    DISK_FULL = "disk_full"
    MEMORY_LIMIT = "memory_limit"
    CLOCK_SKEW = "clock_skew"
    ENGINE_HANG = "engine_hang"  # qua mock engine
    MONGO_STEPDOWN = "mongo_stepdown"
    S3_503 = "s3_503"  # LocalStack
    REDIS_BLOCK_REPLICATION = "redis_block_replication"  # B4: ép mất ghi


class Fault(Protocol):
    kind: FaultKind

    def start(self) -> None: ...
    def stop(self) -> None: ...
