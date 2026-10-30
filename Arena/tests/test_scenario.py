from pathlib import Path

import pytest

from arena.scenario import load_battle

BATTLES = sorted((Path(__file__).parent.parent / "battles").glob("*.yaml"))


@pytest.mark.parametrize("path", BATTLES, ids=lambda p: p.stem)
def test_battle_file_is_valid(path: Path) -> None:
    battle = load_battle(path)
    assert battle.load, "battle phải có ít nhất một phase tải"
